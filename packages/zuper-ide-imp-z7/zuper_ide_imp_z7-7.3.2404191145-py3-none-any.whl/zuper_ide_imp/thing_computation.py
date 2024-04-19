import asyncio
import traceback
from asyncio import CancelledError, Queue, Task
from dataclasses import dataclass
from functools import partial
from typing import Any, Generic, Optional, TYPE_CHECKING, TypeVar

import zuper_html as zh
from mcdp import DPInternalError, MCDPExceptionWithWhere
from mcdp_lang import FinalFunction, KnownAlready, add_error_from_exception, get_dependencies, get_suggestions_mcdp
from mcdp_lang_spec import h_library_name, h_thing_name
from mcdp_lang_utils import (
    PP_ParseFailure,
    PP_RefineFailure,
    PP_RefineResult,
    PP_Result,
)
from mcdp_library import specs
from mcdp_posets import get_copy_with_entity
from zuper_commons.text import normalize_textlines
from zuper_commons.types import TM, ZAssertionError, ZValueError, add_context, check_isinstance
from zuper_ide_interface import (
    CODE,
    CONTENT,
    ECreated,
    ERemoved,
    Identities,
    LibrariesEventPacket,
    ShelfViewSession,
    SpecEventPacket,
)
from zuper_utils_asyncio import (
    EventOrder,
    GenericWatchable,
    OrderHelper,
    SingleView,
    SubscriberInfo,
    SyncTaskInterface,
    UpdateNoPrevious,
    WatchControl,
    async_errors,
    my_create_task,
    my_run_task,
    queue_get_multiple,
)
from zuper_utils_asyncio.wait_verbose import await_with_message
from zuper_utils_augres import (
    AR,
    EntityThing,
    LocationContext,
    LocationImportSource,
    LocationUnknown,
    SideInfo,
)
from zuper_utils_language import EvalFailure, EvalSuccess, NotExisting, ParseFailure, ThingResult


@dataclass
class ThingComputationDependency:
    single_view: SingleView[AR[ThingResult[Any]]]
    watch_control: WatchControl


X = TypeVar("X")

if TYPE_CHECKING:
    from .loader_imp import Loader, LoaderSession


@dataclass
class AskCompute(Generic[X]):
    desc: str
    # session: "LoaderSession"
    identity: Identities
    result_here: "Queue[UpdateNoPrevious[AR[ThingResult[X]]]]"


@dataclass
class SomeUpdate:
    trigger: EventOrder
    desc: str


@dataclass
class CodeUpdated(SomeUpdate):
    code: Optional[bytes]


@dataclass
class DependenciesUpdated(SomeUpdate):
    dep: EntityThing
    value: AR[ThingResult[Any]]


@dataclass
class LibraryUpdated(SomeUpdate):
    packet: LibrariesEventPacket


@dataclass
class ThingUpdated(SomeUpdate):
    packet: SpecEventPacket


class Exit:
    pass


QueueContent = AskCompute[X] | SomeUpdate | Exit


class ThingComputation(Generic[X]):
    address: EntityThing

    # This is "last valid" - it is set to None if need an update
    _last: Optional[UpdateNoPrevious[AR[ThingResult[X]]]]
    _last_update_order: EventOrder

    gw: GenericWatchable[UpdateNoPrevious[AR[ThingResult[X]]]]
    loader: "Loader"
    my_dependencies: dict[EntityThing, ThingComputationDependency]
    code_watch: WatchControl
    sti: SyncTaskInterface
    internal_log: list[object]

    __print_order__ = ["address", "gw", "my_dependencies", "_last"]

    def __init__(self, l: "Loader", address: EntityThing):
        self.loader = l
        self.oh = OrderHelper(f"ThingComputation:{address.thing_name}")
        self.address = address
        self._last = None
        self._last_update_order = EventOrder.empty()
        self.gw = GenericWatchable(address.thing_name, send_last_on_subscribe=True)
        self.my_dependencies = {}
        self.internal_log = []
        self.process_queue = asyncio.Queue()
        self.send_queue = asyncio.Queue()

    process_queue: "asyncio.Queue[QueueContent[X]]"
    send_queue: "asyncio.Queue[Optional[UpdateNoPrevious[AR[ThingResult[X]]]]]"
    process_loop_task: "Task[None]"
    send_loop_task: "Task[None]"

    async def init(self, sti: SyncTaskInterface) -> None:
        self.sti = sti
        self.process_loop_task = my_run_task("process_loop", self.process_loop)
        self.send_loop_task = my_run_task("send_loop", self.send_loop)

    async def aclose(self) -> None:
        self.process_queue.put_nowait(Exit())
        self.send_queue.put_nowait(None)
        await asyncio.sleep(0)
        self.process_loop_task.cancel("aclose")
        self.send_loop_task.cancel("aclose")
        await self.gw.finish()

    def _internal_log(self, *obs: object) -> None:
        tt: TM[object] = tuple(obs)
        ob: object
        if len(tt) == 1:
            ob = tt[0]
        else:
            ob = tt

        if False:
            self.sti.logger.debug(self.address.thing_name, ob=ob)  # stacklevel=1)
        self.internal_log.append(ob)

    @async_errors
    async def process_loop(self) -> None:  # FIXME: make loop resistant to errors
        while True:
            messages = await queue_get_multiple(self.process_queue)
            self._internal_log(f"process_loop got {len(messages)} messages")

            must_exit = any(isinstance(m, Exit) for m in messages)
            if must_exit:
                self._internal_log("process_loop: must_exit")
                self.send_queue.put_nowait(None)
                break

            for i in range(5):  # FIXME: this is a hack
                try:
                    await self.process_loop_messages(messages)
                except CancelledError:
                    raise

                except Exception as e:
                    self.sti.logger.error("Error in process_loop", traceback=traceback.format_exc())
                    await asyncio.sleep(1)
                    continue
                break

    @async_errors
    async def process_loop_messages(self, messages: list[QueueContent[X]]) -> None:
        # for m in messages:
        #     self._internal_log(m)
        send_requests = [m for m in messages if isinstance(m, AskCompute)]
        updates = [m for m in messages if isinstance(m, SomeUpdate)]

        changed = False
        trigger = EventOrder.empty()
        if updates:

            for m in updates:

                trigger.origins.update(m.trigger.origins)

                changed = False
                if isinstance(m, LibraryUpdated):
                    self._internal_log("library update received")
                    changed |= await self._process_library_change(m)
                elif isinstance(m, ThingUpdated):
                    self._internal_log("thing update received")
                    changed |= await self._process_thing_updated(m)
                elif isinstance(m, CodeUpdated):
                    self._internal_log("code update received")
                    changed = True
                elif isinstance(m, DependenciesUpdated):
                    self._internal_log("dependency update", m.dep)
                    changed = True
                else:
                    raise ZAssertionError(m=m)

        if changed:

            # trigger = updates[-1].trigger
            desc = updates[-1].desc
            if self.gw.watchers:
                self._internal_log("process_loop: updates and we have watchers: recompute")
                async with self.loader.session(self.identity, desc) as s3:

                    await await_with_message(self._recompute(trigger, s3, desc), 2.0, self.sti.logger, "recompute")
                self._internal_log("process_loop: recomputed")

                self._internal_log("process_loop: sending to queue")

                self.send_queue.put_nowait(self._last)

            else:
                self._internal_log("process_loop: updates but no watchers, setting last to None")
                # self.sti.logger.info("no watchers, skipping recomputing, setting last to None", trigger=trigger)
                self._last_update_order = trigger
                self._last = None
        else:
            msg = "process_loop: no changes"
            self._internal_log(msg)

        if send_requests:
            if self._last is not None:
                self._internal_log("process_loop: send_requests and we have last")
                for sr in send_requests:
                    self._internal_log(f"sending old one to {sr.desc}")
                    sr.result_here.put_nowait(self._last)

            else:
                self._internal_log("process_loop: send_requests and we need recompute")

                # session = send_requests[-1].session
                identity = send_requests[-1].identity
                desc = send_requests[-1].desc
                try:
                    async with self.loader.session(identity, desc) as session:
                        await self._recompute(self._last_update_order, session, desc)
                except Exception as e:

                    tb = traceback.format_exc()
                    self._internal_log("Error in process_loop", tb)
                    raise

                self._internal_log("process_loop: recomputed")
                assert self._last is not None
                for sr in send_requests:
                    self._internal_log(f"sending new one to {sr.desc}")
                    sr.result_here.put_nowait(self._last)
                self._internal_log("process_loop: sending to queue")
                self.send_queue.put_nowait(self._last)

    @async_errors
    async def send_loop(self) -> None:
        last_sent = None
        try:
            while True:
                found = await queue_get_multiple(self.send_queue)

                if any(x is None for x in found):
                    self._internal_log("send_loop: exiting")
                    break

                self._internal_log(f"send_loop: found {len(found)} to send")

                to_send = found[-1]
                assert to_send is not None
                if to_send.current == last_sent:
                    self._internal_log("skipping sending because same")
                    continue
                last_sent = to_send.current
                try:
                    self._internal_log(f"send_loop: actually sending", to_send.order)
                    await self.gw.distribute(None, to_send)
                except CancelledError:
                    raise
                except Exception:
                    msg = "Error while sending"
                    self.sti.logger.error(msg, traceback=traceback.format_exc())
        finally:
            self._internal_log("send_loop: exiting")

    async def proxy(self, session: "LoaderSession") -> "ThingProxy[X]":
        return ThingProxy(self, session)

    async def get(self, session: "LoaderSession", *, desc: str) -> UpdateNoPrevious[AR[ThingResult[X]]]:
        q: "Queue[UpdateNoPrevious[AR[ThingResult[X]]]]" = asyncio.Queue()
        self.process_queue.put_nowait(AskCompute(identity=session.identity, desc=desc, result_here=q))
        return await q.get()

    @async_errors
    async def on_code_change(self, _: int, x0: UpdateNoPrevious[Optional[bytes]]) -> None:
        self.process_queue.put_nowait(
            CodeUpdated(trigger=x0.order, code=x0.current, desc=f"{self.address.thing_name}:on_code_change")
        )

    async def on_dependency_change(self, dep: EntityThing, _: int, x0: UpdateNoPrevious[AR[ThingResult[Any]]]) -> None:
        desc = f"{self.address.thing_name}:on_dependency_change({dep.thing_name})"
        self.process_queue.put_nowait(DependenciesUpdated(trigger=x0.order, dep=dep, value=x0.current, desc=desc))

    @async_errors
    async def on_libraries_change(self, _: int, packet: LibrariesEventPacket) -> None:
        self.process_queue.put_nowait(
            LibraryUpdated(trigger=packet.order, packet=packet, desc=f"{self.address.thing_name}:on_libraries_change")
        )

    async def _process_library_change(self, update: LibraryUpdated) -> bool:
        packet = update.packet
        self._internal_log(("on_libraries_change", packet))
        self.oh.acknowledge(packet.order)
        logger = self.sti.logger
        desc = f"{self.address.thing_name}:_process_library_change"
        changed = False
        #     logger.info("on_libraries_change", packet=packet, me=self.address.thing_name)
        for e in packet.events:
            match e:
                case ECreated(created=created):
                    if created == self.address.library_name:
                        logger.info("Now the library is created")
                        self._internal_log("Now my library is created")

                        async with self.loader.session(self.identity, desc) as s2:
                            library = await s2.get_library_view(
                                import_source=self.address.import_source, library_name=self.address.library_name
                            )
                            specs0 = await library.specs()
                            spec = await specs0.get(self.address.spec_name)
                            # noinspection PyTypeChecker
                            spec.watch(
                                SubscriberInfo(
                                    self.on_spec_change, internal_description=f"{self.address.thing_name}:on_spec_change"
                                )
                            )
                            changed = True

                        # self.process_queue.put_nowait(LibraryUpdated(trigger=packet.order, desc=desc))

                    logger.info("on_spec_change", created=created)
                case ERemoved(removed=removed):
                    if removed == self.address.library_name:
                        self._internal_log("Now my library is deleted")
                        changed = True
                        # self.process_queue.put_nowait(LibraryUpdated(trigger=packet.order, desc=desc))
                case _:
                    pass
        return changed

    @async_errors
    async def _obtain(self, session: "LoaderSession", desc: str) -> AR[ThingResult[X]]:

        self.identity = session.identity  # XXX: should we save this?
        desc += f"/{self.address.thing_name}:_obtain"
        si = SideInfo.empty()
        creator = "_obtain"
        with add_context(address=self.address):
            try:
                view_master = await session.get_version_view(self.address.import_source)
            except KeyError:
                msg = f"Could not find import source."
                si.notes.note_error(msg, note_kwargs=dict(import_source=self.address.import_source))
                return si % ThingResult(NotExisting())

            s2: ShelfViewSession
            async with view_master.session(desc) as s2:
                libraries = await s2.libraries()

                # noinspection PyTypeChecker
                libraries.watch(
                    SubscriberInfo(
                        self.on_libraries_change, internal_description=f"{self.address.thing_name}:on_libraries_change"
                    )
                )

                try:
                    library = await libraries.get(self.address.library_name)
                except KeyError:
                    msg2 = zh.span(f"Could not find library ", h_library_name(self.address.library_name), ".")
                    si.notes.note_error(msg2, created_file=__file__, created_module=__name__, created_function=creator)
                    return si % ThingResult(NotExisting())
                specs_view = await library.specs()
                spec = await specs_view.get(self.address.spec_name)
                # noinspection PyTypeChecker
                spec.watch(SubscriberInfo(self.on_spec_change, internal_description=f"{self.address.thing_name}:on_spec_change"))

                if await spec.exists(self.address.thing_name):
                    thing = await spec.get(self.address.thing_name)
                else:
                    self.sti.logger.debug("thing does not exist yet")

                    tag = zh.span("Could not find ", h_thing_name(self.address.thing_name, self.address.spec_name), ".")
                    available = await spec.lists()
                    si.notes.note_error(
                        tag,
                        created_file=__file__,
                        created_module=__name__,
                        created_function=creator,
                        note_kwargs=dict(available=sorted(available)),
                    )
                    return si % ThingResult(NotExisting())

                if await thing.exists(CODE):
                    code_view = await thing.get(CODE)
                elif await thing.exists(CONTENT):
                    code_view = await thing.get(CONTENT)
                else:
                    msg = f"Could not find data streams `{CODE}` or `{CONTENT}` in {thing}"
                    raise ZValueError(msg)

                internal_description = f"{self.address.thing_name}:_obtain/code_view.watch"
                self.code_watch = code_view.watch(SubscriberInfo(self.on_code_change, internal_description=internal_description))

                content = await code_view.get(desc=desc)

            if content is None:
                return si % ThingResult(NotExisting())
            else:
                return await self._obtain_from_content(session, content)

    # @asynccontextmanager
    # async def lock_state(self, desc: str) -> AsyncIterator[None]:
    #     logger = self.sti.logger
    #     if self._lock_state.locked():
    #         logger.warn("Only one get at a time", address=self.address, operation=desc, operation_in_processing=self._cur_desc)
    #         # raise ZValueError("Only one get at a time")
    #     async with self._lock_state:
    #         # cur_last = self._last
    #         self._internal_log(f"lock_state: {desc}")
    #         logger.debug("lock_state", address=self.address, operation=desc)
    #         self._cur_desc = desc
    #         try:
    #             yield
    #         finally:
    #             self._cur_desc = None
    #             self._internal_log(f"unlock_state: {desc}")

    @async_errors
    # @serialize_operation
    async def on_spec_change(self, _: int, packet: SpecEventPacket) -> None:

        m = ThingUpdated(trigger=packet.order, packet=packet, desc=f"{self.address.thing_name}:on_spec_change")
        self.process_queue.put_nowait(m)

    async def _process_thing_updated(self, m: ThingUpdated) -> bool:
        packet = m.packet
        self._internal_log(("on_spec_change", packet))
        desc = f"{self.address.thing_name}:on_spec_change"
        logger = self.sti.logger
        changed = False
        self.oh.acknowledge(packet.order)
        #  logger.info("on_spec_change", packet=packet, me=self.address.thing_name)
        for e in packet.events:
            match e:
                case ECreated(created=created):
                    if created == self.address.thing_name:
                        logger.info("Now I am created", packet_order=packet.order)
                        self._internal_log("I am now created")
                        # async with self.lock_state(desc):  # XXX: probably useless at this point
                        changed = True
                        async with self.loader.session(self.identity, desc) as s2:
                            library = await s2.get_library_view(
                                import_source=self.address.import_source, library_name=self.address.library_name
                            )
                            allspecs = await library.specs()
                            spec = await allspecs.get(self.address.spec_name)

                            thing = await spec.get(self.address.thing_name)
                            if await thing.exists(CODE):
                                code_view = await thing.get(CODE)
                            elif await thing.exists(CONTENT):
                                code_view = await thing.get(CONTENT)
                            else:
                                msg = f"Could not find data streams `{CODE}` or `{CONTENT}` in {thing}"
                                raise ZValueError(msg)
                            internal_description = f"{self.address.thing_name}:on_code_change"
                            self.code_watch = code_view.watch(
                                SubscriberInfo(self.on_code_change, internal_description=internal_description)
                            )

                            self._internal_log("I am now created: finished")
                            # self.process_queue.put_nowait(ThingUpdated(trigger=packet.order, desc=desc))

                case ERemoved(removed=removed):
                    if removed == self.address.thing_name:
                        self._internal_log("I am now deleted")
                        # self.process_queue.put_nowait(ThingUpdated(trigger=packet.order, desc=desc))
                        changed = True
                case _:
                    pass
        return changed

    @async_errors
    async def _obtain_from_content(self, session: "LoaderSession", content: bytes) -> AR[ThingResult[X]]:
        desc = f"{self.address.thing_name}:_obtain_from_content"
        si = SideInfo.empty()

        logger = self.sti.logger

        a = self.address
        filepath = f"{a.library_name}/{a.spec_name}/{a.thing_name}"
        loop = asyncio.get_event_loop()
        executor = self.loader.process_pool
        source = content.decode("utf-8")
        source = normalize_textlines(source)

        # self.sti.logger.debug(f"load_source {filepath}", source=source[:100] + " ...")
        await asyncio.sleep(0)
        from .loader_imp import parse_source

        # RUN_SYNC = False
        try:
            r0: AR[PP_Result[Any]]
            # if RUN_SYNC:
            #     r0 = parse_source(a.spec_name, source, filepath)
            # else:
            r0 = await loop.run_in_executor(executor, parse_source, a.spec_name, source, filepath)

            self._internal_log(f"load_source {filepath} done")
        except MCDPExceptionWithWhere as e:
            self._internal_log(f"load_source {filepath} failed  ")
            add_error_from_exception(si, e)
            tr: ThingResult[Any] = ThingResult(ParseFailure(source=source, display=[source]))
            return si % tr
        except Exception as e:
            self._internal_log(f"load_source {filepath} failed with unexpected error")
            self.sti.logger.error("Error while parsing", filepath=filepath, traceback=traceback.format_exc())

            # TODO: should this be DPInternalError?
            si.notes.note_error(
                "Unexpected error while parsing",
                note_kwargs=dict(traceback=traceback.format_exc()),
                locations=LocationUnknown(),
                tags=(type(e).__name__,),
            )
            tr = ThingResult(ParseFailure(source=source, display=[source]))
            return si % tr

        r0_si, r = r0.split_even_errors()
        si.merge(r0_si)
        match r:
            case PP_ParseFailure(display=display):
                tr = ThingResult(ParseFailure(display=display, source=source))
                return si % tr
            case PP_RefineFailure(display=display):
                # For now, PP_ParseFailure and PP_RefineFailure are the same
                tr = ThingResult(ParseFailure(display=display, source=source))
                return si % tr
            case PP_RefineResult() as okres:
                prr = okres

            case _:
                raise AssertionError

        # if ppr0.has_errors():
        #     si.merge(ppr_si)
        #
        #     tr: ThingResult[Any] = ThingResult( ParseFailure(display=display, source=source))
        #     return  si % tr

        known_already = KnownAlready({})
        # self._internal_log("now getting dependencies")
        # await asyncio.sleep(0.01)

        # Get the dependencies
        da = si << get_dependencies(a.import_source, a.library_name, prr.flp, known_already)
        now_deps = da.dependencies
        # remove old dependencies
        for k, v1 in list(self.my_dependencies.items()):
            if k not in now_deps:
                self._internal_log("removing dependency", k)
                v1.watch_control.unwatch()
                self.my_dependencies.pop(k)

        # add new dependencies
        for k, v2 in now_deps.items():
            if k not in self.my_dependencies:
                if k == a:
                    msg = f"Cannot depend on oneself."
                    raise ZAssertionError(msg, k=k, a=a)  # FIXME: DEV-300: give better error when this happens

                # logger.info("adding dependency", me=a, dep=k)
                view = await session.obtain(k.import_source, k.library_name, k.spec_name, k.thing_name)
                internal_description = f"{a.thing_name}:_obtain_from_content/dep.get({k.thing_name})"
                wc = view.watch(SubscriberInfo(partial(self.on_dependency_change, k), internal_description=internal_description))

                self.my_dependencies[k] = ThingComputationDependency(view, wc)

        resolved: dict[EntityThing, AR[ThingResult[Any]]] = {}
        for k, v3 in self.my_dependencies.items():
            with add_context(address=a, dependency=k):
                desck = desc + f"/dep.get({k.thing_name})"
                r = await v3.single_view.get(desc=desck)

            if not r.has_result():
                msg = f"Dependency has no result."
                raise ZAssertionError(msg, k=k, v=v3)

            si_k, ob = r.split_even_errors()
            context_desc = zh.p(
                "While loading ",
                h_thing_name(k.thing_name, k.spec_name),
                " from the library ",
                h_library_name(k.library_name),
                ".",
            )
            # todo: only add if import source is different
            if self.address.import_source != k.import_source:
                l1 = LocationImportSource(k.import_source, LocationUnknown())
                lc = LocationContext(context_desc, l1)
            else:
                lc = LocationContext(context_desc, LocationUnknown())
            si2 = si_k.wrap_location(lc)
            r2 = si2 % ob

            resolved[k] = r2

        known_already.resolved.update(resolved)
        da2 = si << get_dependencies(a.import_source, a.library_name, prr.flp, known_already)
        if da2.missing:
            msg = "There should not be any missing dependencies."
            raise ZAssertionError(msg, da=da, resolved=resolved, da2=da2)

        parse_eval: FinalFunction[Any] = specs[a.spec_name].final_function
        eval_context = da2.eval_context

        if da2.cannot_proceed:
            ev = EvalFailure(source=source, display=prr.display, parsed=prr.expr, refined=prr.refined, links=da2.links)
            tr = ThingResult(result=ev)
        else:
            with add_context(da=da, da2=da2, known_already=known_already, eval_context=eval_context, prr=prr, si=si):
                # TODO: check errors
                try:
                    res_ = parse_eval(prr, eval_context)
                except CancelledError:  # TODO: more exceptions to filter?
                    raise
                except MCDPExceptionWithWhere as e:
                    add_error_from_exception(si, e)
                    ev = EvalFailure(
                        source=source,
                        display=prr.display,
                        parsed=prr.expr,
                        refined=prr.refined,
                        links=da2.links,
                    )
                except Exception:
                    si.notes.note_error(
                        "Unexpected error while evaluating",
                        note_kwargs=dict(traceback=traceback.format_exc()),
                        locations=LocationUnknown(),
                        tags=(DPInternalError.__name__,),
                    )
                    ev = EvalFailure(
                        source=source,
                        display=prr.display,
                        parsed=prr.expr,
                        refined=prr.refined,
                        links=da2.links,
                    )
                else:
                    final = si << res_

                    final = get_copy_with_entity(final, a)
                    ev = EvalSuccess(
                        source=source,
                        object=final,
                        display=prr.display,
                        parsed=prr.expr,
                        refined=prr.refined,
                        suggestions=get_suggestions_mcdp(prr.refined),
                        links=da2.links,
                    )
            tr = ThingResult(result=ev)

            # logger.debug(
            #     "_obtain_from_content",
            #     address=a,
            #     da=da,
            #     da2=da2,
            #     known_already=known_already,
            #     eval_context=eval_context,
            #     tr=tr,
            # )

        return si % tr

    @async_errors
    async def _recompute(self, trigger: EventOrder, session: "LoaderSession", desc: str) -> None:
        # logger = self.sti.logger
        desc += f"/{self.address.thing_name}:_recompute()"
        self._internal_log(("_recompute", desc, trigger))
        try:
            thingr = await self._obtain(session, desc)
        except CancelledError:
            raise
        # except Exception as e:
        #     self.sti.logger.error("Error while recomputing", traceback=traceback.format_exc())
        #

        order2 = self.oh.add_to(trigger)
        i = order2.origins[self.oh.name]
        self._last = UpdateNoPrevious(i, thingr, order2)

        self._internal_log("_recompute done")


class ThingProxy(Generic[X], SingleView[AR[ThingResult[X]]]):
    __print_order__ = ["master", "session", "internal_log"]
    task_first: Optional[Task[None]]

    def __init__(self, master: ThingComputation[X], session: "LoaderSession"):
        self.master = master
        self.session = session
        self.task_first = None
        self.logger = self.master.sti.logger
        self.internal_log = self.master.internal_log

    async def get(self, *, desc: str) -> AR[ThingResult[X]]:
        res = await self.master.get(self.session, desc=desc)
        check_isinstance(res, UpdateNoPrevious)
        check_isinstance(res.current, AR)
        return res.current

    async def get_eo(self, *, desc: str) -> UpdateNoPrevious[AR[ThingResult[X]]]:
        return await self.master.get(self.session, desc=desc)

    def watch_and_get_first(self, subscriber: "SubscriberInfo[UpdateNoPrevious[AR[ThingResult[X]]]]", /) -> WatchControl:
        w = self.watch(subscriber)
        if self.master.gw.last is None:
            self.logger.debug("there was no last")
            if self.task_first is None:
                self.logger.debug("creating a task")
                desc = subscriber.internal_description or "watch_and_get_first"
                self.task_first = my_create_task(self.task_first_f(desc), "task_first")

        return w

    def watch(self, info: SubscriberInfo[UpdateNoPrevious[AR[ThingResult[X]]]]) -> WatchControl:
        # self.logger.debug("new watch request", info=info)
        return self.master.gw.watch(info)

    @async_errors
    async def task_first_f(self, for_who: str) -> None:
        # self.logger.debug("task_first started")
        res = await self.master.get(self.session, desc=f"{for_who}/task_first")
        # self.logger.debug("task_first done", res=res)
        # self.master.gw.distribute(None, UpdateNoPrevious(self.master.gw.last, 0))
