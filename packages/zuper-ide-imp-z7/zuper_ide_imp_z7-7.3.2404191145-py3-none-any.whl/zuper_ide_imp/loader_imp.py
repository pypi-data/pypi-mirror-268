import asyncio
import contextlib
import copy
import multiprocessing
import os
import time
from typing import Any, AsyncContextManager, AsyncIterator, Optional, Sequence, TYPE_CHECKING, TypeVar, cast

import zuper_html as zh
from mcdp import DPSemanticError
from mcdp_lang import EvalContext, LoadedCodeSpec, add_where_information, find_load_parts, get_subnotes, get_suggestions_mcdp
from mcdp_lang_spec import h_library_name, h_thing_name
from mcdp_lang_utils import (
    PP_ParseFailure,
    PP_RefineFailure,
    PP_RefineResult,
    PP_Result,
    SpecLibThing,
)
from mcdp_library import specs
from mcdp_ndp import NamedDPAny
from mcdp_posets import get_copy_with_entity, get_default_context
from zuper_commons.text import LibraryName, MarkdownStr, SpecName, ThingName, URLString
from zuper_commons.types import ZAssertionError, ZKeyError, ZValueError, add_context, check_isinstance
from zuper_ide_interface import (
    CDEInterface,
    CDEInterfaceSession,
    CDEView,
    CODE,
    CONTENT,
    Identities,
    LibraryView,
    LoaderInterface,
    LoaderSessionInterface,
    PRODUCT_INTERPRETED,
    ProductName,
    ProductsView,
    SERVICE_LOADER,
    ShelfViewMaster,
    Specnames,
    available_visualizations,
    get_cde_interface,
)
from zuper_utils_asyncio import (
    MyAsyncExitStack,
    SingleView,
    SyncTaskInterface,
    async_errors,
    coord_customkey,
    coord_first_key,
)
from zuper_utils_augres import (
    AR,
    EntityLibrary,
    EntityThing,
    ImportSource,
    LocationInString,
)
from zuper_utils_language import (
    EntityFound,
    EvalFailure,
    EvalSuccess,
    NMWhere,
    NotExisting,
    ParseFailure,
    ThingResult,
    add_filename_to_where,
)
from zuper_zapp_interfaces import ServiceConfig
from . import logger as logger0
from .visualization_proxies import ThingVisualization

X = TypeVar("X")


@contextlib.asynccontextmanager
async def loader(sti: SyncTaskInterface, _: ServiceConfig) -> AsyncIterator[None]:

    cde = await get_cde_interface(sti)
    use = Loader(cde)
    await use.init(sti)

    try:

        async def generate(_sti_: SyncTaskInterface) -> LoaderInterface:
            return use

        await sti.set_interface_gen(SERVICE_LOADER, generate)

        yield
    finally:
        await use.aclose()


from .thing_computation import ThingComputation


def initializer() -> None:
    from zpsyntax_mcdp.parse_interface import ZPFunction
    from . import logger

    _ = ZPFunction  # KEEP, we need to import
    logger.info(f"worker {os.getpid()} initialized ")


class Loader(LoaderInterface):
    cde: CDEInterface
    sti: SyncTaskInterface
    S: MyAsyncExitStack

    computation: dict[EntityThing, ThingComputation[Any]]
    address2products: "dict[EntityThing, dict[ProductName, ThingVisualization]]"

    def __init__(self, cde: CDEInterface):
        # self.version_views = {}
        self.cde = cde
        # ctx = multiprocessing.get_context()
        # ctx.reducer = dill.reducer
        mp_context = multiprocessing.get_context("spawn")
        mp_context_default = multiprocessing.get_context()
        logger0.info(f"Using multiprocessing context {mp_context.__dict__} (default: {mp_context_default.__dict__})")
        # self.process_pool = ProcessPoolExecutor(mp_context=mp_context)
        # self.process_pool = ProcessPoolExecutor(initializer=initializer,
        #                                         max_tasks_per_child=1)
        self.process_pool = None
        # self.process_pool = None
        self.computation = {}
        self.address2products = {}
        self.lock_products_init = asyncio.Lock()
        self.lock_get_thing_computation = asyncio.Lock()

    async def init(self, sti: SyncTaskInterface) -> None:
        self.sti = sti
        self.S = MyAsyncExitStack(sti)

    async def aclose(self) -> None:
        await self.S.aclose()

    async def get_thing_computation(self, address: EntityThing) -> ThingComputation[Any]:
        async with self.lock_get_thing_computation:
            if address not in self.computation:
                tc: ThingComputation[Any] = ThingComputation(self, address)
                self.computation[address] = tc
                await self.S.init(tc)
            return self.computation[address]

    if TYPE_CHECKING:

        def session(self, identity: Identities, desc: str) -> "AsyncContextManager[LoaderSession]": ...

    else:

        @contextlib.asynccontextmanager
        async def session(self, identity: Identities, desc: str) -> "AsyncIterator[LoaderSession]":
            desc2 = f"loader_session:{desc}"
            async with self.cde.session(identity, desc2) as s:
                async with self.session_from_cde_session(s, identity, desc) as res:
                    yield res

    if TYPE_CHECKING:

        def session_from_cde_session(
            self, s: CDEInterfaceSession, identity: Identities, desc: str
        ) -> "AsyncContextManager[LoaderSession]": ...

    else:

        @contextlib.asynccontextmanager
        async def session_from_cde_session(
            self, s: CDEInterfaceSession, identity: Identities, desc: str
        ) -> "AsyncIterator[LoaderSession]":
            res = LoaderSession(self, s, identity, desc)
            await res.init(self.sti)
            try:
                yield res
            finally:
                await res.aclose()


class LoaderSession(LoaderSessionInterface):
    cde_session: CDEInterfaceSession
    identity: Identities
    view: CDEView
    sti: SyncTaskInterface
    master: Loader
    S: MyAsyncExitStack
    library_views: dict[tuple[ImportSource, LibraryName], LibraryView]

    def __init__(self, master: Loader, s: CDEInterfaceSession, identity: Identities, desc: str):
        self.master = master
        self.identity = identity
        self.cde_session = s
        self.library_views = {}  #
        self.invalid = False
        self.desc = desc

    async def get_shelf_view(self, import_source: ImportSource) -> ShelfViewMaster:
        return await self.get_version_view(import_source)

    async def init(self, sti: SyncTaskInterface) -> None:
        self.S = MyAsyncExitStack(sti)
        self.sti = sti

        s = self.cde_session
        self.view = await s.get_view()

    async def aclose(self) -> None:
        # self.invalid = True
        await self.S.aclose()

    def _check_valid(self) -> None:
        if self.invalid:
            msg = f"This session is no longer valid: {self.desc}"
            raise ZAssertionError(msg)

    @coord_first_key
    async def get_version_view(self, import_source: ImportSource) -> ShelfViewMaster:
        return await self.view.get_shelf_view(import_source)
        # self._check_valid()
        # if import_source not in self.master.version_views:
        #     self.master.version_views[import_source] = await self._get_version_view(import_source)
        # return self.master.version_views[import_source]

    @coord_customkey(("import_source", "library_name", "spec_name", "thing_name"))
    async def get_source(
        self,
        *,
        import_source: ImportSource,
        library_name: LibraryName,
        spec_name: SpecName,
        thing_name: ThingName,
    ) -> str:
        desc = "get_source:{thing_name}"
        self._check_valid()
        library_view: LibraryView = await self.get_library_view(import_source=import_source, library_name=library_name)
        specs_view = await library_view.specs()
        spec_view = await specs_view.get(spec_name)
        try:
            thing_view = await spec_view.get(thing_name)
        except KeyError as e:
            msg = MarkdownStr(f"Could not find `{thing_name}` among {spec_name}.")
            raise DPSemanticError(msg) from e
        code = await thing_view.get(CODE)
        source = await code.get(desc=desc)
        assert isinstance(source, bytes), source
        return source.decode("utf8")

    @coord_customkey(("import_source", "library_name"))
    async def get_library_view(self, *, import_source: ImportSource, library_name: LibraryName) -> LibraryView:
        self._check_valid()
        key = (import_source, library_name)
        if key not in self.library_views:  # Note: we cache the library view
            shelf_view: ShelfViewMaster = await self.get_version_view(import_source)
            shelf_session = await self.S.enter_async_context(shelf_view.session("mcdp_view_main"))
            libraries = await shelf_session.libraries()
            try:
                library_view = await libraries.get(library_name)
            except KeyError as e:
                msg = MarkdownStr(f"Could not find library `{library_name}` in `{import_source}`.")
                raise DPSemanticError(msg) from e
            self.library_views[key] = library_view
            self.sti.logger.debug("get_library_view", key=key, res=library_view)

        return self.library_views[key]

    @async_errors
    async def load(
        self,
        import_source: ImportSource,
        library_name: LibraryName,
        spec_name: SpecName,
        thing_name: ThingName,
    ) -> AR[ThingResult[Any]]:
        self._check_valid()
        source = await self.get_source(
            import_source=import_source, library_name=library_name, spec_name=spec_name, thing_name=thing_name
        )
        return await self.load_source(
            import_source=import_source,
            library_name=library_name,
            spec_name=spec_name,
            thing_name=thing_name,
            source=source,
        )

    @async_errors
    @coord_customkey(("import_source", "library_name", "spec_name", "thing_name", "source"))
    async def load_source(
        self,
        *,
        import_source: ImportSource,
        library_name: LibraryName,
        spec_name: SpecName,
        thing_name: Optional[ThingName],
        source: str,
    ) -> AR[ThingResult[Any]]:
        self._check_valid()
        desc = f"load_source:{thing_name or 'source'}"
        # ppr: PP_Result[Any]
        filepath = f"{library_name}/{spec_name}/{thing_name}"
        # ppr = self.parse_source(spec_name, source, filepath=filepath)
        loop = asyncio.get_event_loop()
        executor = self.master.process_pool
        self.sti.logger.debug(f"load_source {filepath}")
        await asyncio.sleep(0)
        logger = self.sti.logger
        ppr0 = await loop.run_in_executor(executor, parse_source, spec_name, source, filepath)

        pr: PP_Result[Any]
        si, pr = ppr0.split()

        ppr: PP_RefineResult[Any]
        result: ThingResult[Any]
        match pr:
            case PP_ParseFailure(display=display):
                result = ThingResult(ParseFailure(source=source, display=display))
                return si % result
            case PP_RefineFailure(display=display):
                result = ThingResult(ParseFailure(source=source, display=display))
                return si % result
            case PP_RefineResult() as x:
                ppr = copy.deepcopy(x)  # we are going to modify it later
            case _:
                raise AssertionError

        # TODO: handle errors
        # self.sti.logger.debug(f"load_source {filepath} OK")

        parse_eval = specs[spec_name].final_function
        var2model: dict[str, AR[NamedDPAny]] = {}
        data_sources: dict[URLString, AR[NMWhere]] = {}
        extra_resolved: dict[SpecLibThing, AR[object]] = {}
        var2thing: dict[tuple[SpecName, str], AR[object]] = {}
        flp = ppr.flp

        links: list[EntityFound] = []

        msg: str | zh.Tag

        # Note: this while is ok because at each iteration we are going to update data_sources
        while set(data_sources) != set(flp.data_resources):

            for url, v1 in flp.data_resources.items():
                if url in data_sources:
                    continue
                with add_where_information(where=v1.elements[0].where):
                    library_view = await self.get_library_view(import_source=import_source, library_name=library_name)
                    specs_view = await library_view.specs()
                    spec = await specs_view.get(Specnames.SPEC_ALL_FILES)
                    try:
                        data = await spec.get(cast(ThingName, url))
                    except ZKeyError as e:
                        msgs = f'Could not find resource "{url}" in "{library_name}"'
                        # TODO: note instead of raise
                        raise DPSemanticError(msgs) from e
                    et = EntityThing(
                        import_source=import_source,
                        library_name=library_name,
                        spec_name=Specnames.SPEC_ALL_FILES,
                        thing_name=cast(ThingName, url),
                    )
                    for element in v1.elements:
                        links.append(EntityFound(entity=et, where=element.where))

                    content: SingleView[Optional[bytes]] = await data.get(CONTENT)

                    source_b: Optional[bytes] = await content.get(desc=desc)

                    if source_b is None:
                        raise ZValueError("TODO: this should never happen but I guess we should do something")
                    source = source_b.decode("utf8")
                    wsi, wdata = v1.parse_function(source).split()
                    filepath = url
                    wdata2 = add_filename_to_where(wdata, source, filepath)

                    wres = wsi % wdata2

                    data_sources[url] = wres
                    si.merge(wres.get_side_info())
                    res = wres.get_result()
                    flp2 = si << find_load_parts(res)
                    flp.merge(flp2)

        resolved_libraries: dict[LibraryName, tuple[ImportSource, LibraryName]] = {}

        for v2 in flp.import_libraries.values():
            # with add_where_information(where=v2.elements[0].where):
            if v2.alias not in resolved_libraries:
                resolved_libraries[v2.alias] = v2.import_source or import_source, v2.library_name
                etl = EntityLibrary(
                    source=v2.import_source or import_source,
                    library_name=v2.library_name,
                )
                for el in v2.elements:
                    links.append(EntityFound(el.where, etl))

        for v in flp.import_things.values():
            w = v.elements[0].where
            with add_where_information(where=w):

                et = EntityThing(
                    import_source=v.import_source or import_source,
                    library_name=v.library_name or library_name,
                    spec_name=v.spec_name,
                    thing_name=v.thing_name,
                )
                for el in v.elements:
                    links.append(EntityFound(el.where, et))

                thing0 = await self.load(et.import_source, et.library_name, et.spec_name, et.thing_name)
                thing_si, thing = thing0.split_even_errors()
                match thing.result:
                    case NotExisting():
                        msg = zh.span(
                            f"Could not find ",
                            h_thing_name(et.thing_name, et.spec_name),
                            " in library ",
                            h_library_name(et.library_name),
                            ".",
                        )
                        si.notes.note_error(msg, locations=LocationInString.from_where(w), subnotes=get_subnotes(thing_si))
                        result = ThingResult(
                            EvalFailure(
                                source=source,
                                display=ppr.display,
                                parsed=ppr.expr,
                                refined=ppr.refined,
                                links=links,
                            )
                        )
                        return si % result
                    case ParseFailure():
                        msg = zh.span(
                            f"Could not parse ",
                            h_thing_name(et.thing_name, et.spec_name),
                            " in library ",
                            h_library_name(et.library_name),
                            ".",
                        )
                        si.notes.note_error(msg, locations=LocationInString.from_where(w), subnotes=get_subnotes(thing_si))
                        result = ThingResult(
                            EvalFailure(
                                source=source,
                                display=ppr.display,
                                parsed=ppr.expr,
                                refined=ppr.refined,
                                links=links,
                            )
                        )
                        return si % result
                    case EvalFailure():
                        msg = zh.span(
                            f"Could not evaluate ",
                            h_thing_name(et.thing_name, et.spec_name),
                            " in library ",
                            h_library_name(et.library_name),
                            ".",
                        )
                        si.notes.note_error(msg, locations=LocationInString.from_where(w), subnotes=get_subnotes(thing_si))
                        result = ThingResult(
                            EvalFailure(
                                source=source,
                                display=ppr.display,
                                parsed=ppr.expr,
                                refined=ppr.refined,
                                links=links,
                            )
                        )
                        return si % result
                    case EvalSuccess() as es:
                        th = thing_si % es.object

                        var2thing[(v.spec_name, v.alias)] = th

                        if v.spec_name == Specnames.SPEC_MODELS:
                            var2model[v.alias] = th
                        # else:
                        #     si.warn_language2(w, "?", "Don't know what to do with this import")
                    case _:
                        raise AssertionError

        for sls, where_needed in flp.extra.items():
            spec_name2, library_name2, thing_name2 = sls
            where = where_needed.elements[0].where

            if library_name2 is None and (spec_name2, thing_name2) in var2thing:
                the_res = var2thing[(spec_name2, thing_name2)]
            else:
                if library_name2 in resolved_libraries:
                    use_import, use_name = resolved_libraries[library_name2]
                    the_res0: AR[ThingResult[Any]]
                    the_res0 = await self.load(use_import, use_name, spec_name2, thing_name2)
                    et = EntityThing(
                        import_source=use_import,
                        library_name=use_name,
                        spec_name=spec_name2,
                        thing_name=thing_name2,
                    )
                    for el in where_needed.elements:
                        links.append(EntityFound(el.where, et))

                else:
                    if library_name2 is None:
                        library_name2 = library_name

                    # with add_context(var2thing=var2thing, var2model=var2model):
                    with add_where_information(where):
                        the_res0: AR[ThingResult[Any]]
                        the_res0 = await self.load(import_source, library_name2, spec_name2, thing_name2)

                        et = EntityThing(
                            import_source=import_source,
                            library_name=library_name2,
                            spec_name=spec_name2,
                            thing_name=thing_name2,
                        )
                        # links.append(EntityFound(where, et))
                        for el in where_needed.elements:
                            links.append(EntityFound(el.where, et))

                logger.debug(the_res=the_res0)
                the_res_thing: ThingResult[Any]
                the_res_si, the_res_thing = the_res0.split_even_errors()
                match the_res_thing.result:
                    case NotExisting():
                        msg = zh.span(
                            f"Could not find ",
                            h_thing_name(thing_name2, spec_name2),
                            " in library ",
                            h_library_name(library_name2),
                            ".",
                        )
                        si.notes.note_error(
                            msg,
                            locations=LocationInString.from_where(where),
                            subnotes=get_subnotes(the_res_si),
                        )
                        result = ThingResult(
                            EvalFailure(
                                source=source,
                                display=ppr.display,
                                parsed=ppr.expr,
                                refined=ppr.refined,
                                links=links,
                            )
                        )
                        return si % result
                    case ParseFailure():
                        msg = zh.span(
                            f"Could not parse ",
                            h_thing_name(thing_name2, spec_name2),
                            " in library ",
                            h_library_name(library_name2),
                            ".",
                        )
                        si.notes.note_error(
                            msg,
                            locations=LocationInString.from_where(where),
                            subnotes=get_subnotes(the_res_si),
                        )
                        result = ThingResult(
                            EvalFailure(
                                source=source,
                                display=ppr.display,
                                parsed=ppr.expr,
                                refined=ppr.refined,
                                links=links,
                            )
                        )
                        return si % result
                    case EvalFailure():
                        msg = zh.span(
                            f"Could not evaluate ",
                            h_thing_name(thing_name2, spec_name2),
                            " in library ",
                            h_library_name(library_name2),
                            ".",
                        )
                        si.notes.note_error(
                            msg,
                            locations=LocationInString.from_where(where),
                            subnotes=get_subnotes(the_res_si),
                        )
                        result = ThingResult(
                            EvalFailure(
                                source=source,
                                display=ppr.display,
                                parsed=ppr.expr,
                                refined=ppr.refined,
                                links=links,
                            )
                        )
                        return si % result
                    case EvalSuccess() as es:
                        the_res = the_res_si % es.object
                    case _:
                        raise AssertionError

            assert the_res is not None
            # logger.info(sls=sls, the_res=the_res)
            check_isinstance(the_res, AR)

            ob_si, ob_res = the_res.split_even_errors()
            ob_si = ob_si.wrap_where(f"While loading {thing_name2}:", where)
            si.merge(ob_si)
            extra_resolved[sls] = ob_si % ob_res
        extra_codespecs_resolved: dict[str, AR[LoadedCodeSpec]] = {}

        if flp.extra_code_specs:
            library_view = await self.get_library_view(import_source=import_source, library_name=library_name)

            specs_view = await library_view.specs()
            spec_view = await specs_view.get(Specnames.SPEC_PYTHON)
            python_files = await spec_view.lists()
            fns: dict[str, str] = {}
            for bn in python_files:
                thing = await spec_view.get(bn)
                code_view = await thing.get(CODE)
                code: Optional[bytes] = await code_view.get(desc=desc)
                if code is None:
                    raise DPSemanticError(f"Could not find code for {bn}")

                fns[bn + ".py"] = code.decode()

            for function_name, where_needed in flp.extra_code_specs.items():
                # where = where_needed.elements[0].where

                res = LoadedCodeSpec(fns, function_name)
                fres = AR.pure(res)
                extra_codespecs_resolved[function_name] = fres

        eval_context = EvalContext(
            dpc=get_default_context(),
            extra=extra_resolved,
            extra_codespecs_resolved=extra_codespecs_resolved,
            var2model=var2model,
            constants={},
            uncertain_constants={},
            data_sources=data_sources,
            var2thing=var2thing,
            notes=si.notes,  # recent, not sure
        )
        with add_context(
            needed=list(flp.extra),
            extra_codespecs_resolved=extra_codespecs_resolved,
            eval_context=eval_context,
        ):
            # res = parse_eval(ppr, eval_context)
            self.sti.logger.debug(f"interpret {filepath}")
            await asyncio.sleep(0)
            final = si << await loop.run_in_executor(executor, parse_eval, ppr, eval_context)
            self.sti.logger.debug(f"interpret {filepath} OK")

            if thing_name is not None:
                final = get_copy_with_entity(final, EntityThing(import_source, library_name, spec_name, thing_name))

            res2 = ThingResult(
                EvalSuccess(
                    source=source,
                    object=final,
                    display=ppr.display,
                    parsed=ppr.expr,
                    refined=ppr.refined,
                    suggestions=get_suggestions_mcdp(ppr.refined),
                    links=links,
                )
            )

        # check_isinstance(res2, AR)
        # check_isinstance(res2.get_result(), ThingResult)

        return si % res2

    async def obtain(
        self,
        import_source: ImportSource,
        library_name: LibraryName,
        spec_name: SpecName,
        thing_name: ThingName,
    ) -> SingleView[AR[ThingResult[Any]]]:
        address = EntityThing(
            import_source=import_source,
            library_name=library_name,
            spec_name=spec_name,
            thing_name=thing_name,
        )
        thing_computation = await self.master.get_thing_computation(address)
        return await thing_computation.proxy(self)

    async def get_products(
        self,
        import_source: ImportSource,
        library_name: LibraryName,
        spec_name: SpecName,
        thing_name: ThingName,
    ) -> ProductsView:
        address = EntityThing(
            import_source=import_source,
            library_name=library_name,
            spec_name=spec_name,
            thing_name=thing_name,
        )

        the_stuff = await self.obtain(
            import_source=import_source,
            library_name=library_name,
            spec_name=spec_name,
            thing_name=thing_name,
        )
        products = {PRODUCT_INTERPRETED: the_stuff}
        for_us = available_visualizations[spec_name]

        async with self.master.lock_products_init:
            if address not in self.master.address2products:
                the_vis: dict[ProductName, ThingVisualization] = {}
                for visualization_name, v in for_us.items():
                    tv = ThingVisualization(self.master, self.identity, address, visualization_name)
                    await tv.init(self.master.sti)
                    the_vis[visualization_name] = tv

                # logger.info("setting the_vis", address=address, the_vis=the_vis, for_us=for_us)
                self.master.address2products[address] = the_vis

        tv = self.master.address2products[address]
        for k, v in tv.items():
            products[k] = await v.proxy(self)  # type: ignore

        lpv = LoaderProductsView(address, products)

        # logger.info("get_products", master=id(self.master), address=address, for_us=for_us, tv=tv,
        #             pv=lpv.products)
        return lpv


class LoaderProductsView(ProductsView):
    address: EntityThing
    loader_session: LoaderSession
    products: dict[ProductName, SingleView[Any]]

    def __init__(self, address: EntityThing, products: dict[ProductName, SingleView[Any]]):
        self.address = address
        self.products = products

    async def exists(self, name: ProductName, /) -> bool:
        return name in self.products

    async def lists(self) -> Sequence[ProductName]:
        return list(self.products)

    async def items(self) -> AsyncIterator[tuple[ProductName, SingleView[Any]]]:
        for name in self.products:
            yield name, await self.get(name)

    async def get(self, name: ProductName, /) -> SingleView[Any]:
        if name not in self.products:
            msg = f"Could not find product {name}"
            raise ZKeyError(msg, available=list(self.products), address=self.address)
        return self.products[name]


import sys


def parse_source(spec_name: SpecName, source: str, filepath: str) -> AR[PP_Result[Any]]:
    sys.stderr.write(f"parse_source({spec_name}, {len(source)} bytes, {filepath})\n")
    try:

        from zpsyntax_mcdp.parse_interface import ZPFunction

        _ = ZPFunction  # KEEP, we need to import
        parse_func = specs[spec_name].parsing_function
        # logger0.debug("parse_source starting", spec_name=spec_name, filepath=filepath, parse_func=parse_func)
        t0 = time.monotonic()
        with add_context(spec_name=spec_name, source=source):
            ppr0: AR[PP_Result[Any]]
            ppr0 = parse_func(source)
            dt = time.monotonic() - t0
            if dt > 0.5:
                logger0.debug(
                    f"parse_source done in {dt:.3f}s", spec_name=spec_name, filepath=filepath, dt=dt, res=type(ppr0.get_result())
                )
            return ppr0

    except BaseException as e:
        sys.stderr.write(f"parse_source({spec_name}, {len(source)} bytes, {filepath}) - raised Exception:\n{e}\n")
        raise

    finally:
        sys.stderr.write(f"parse_source({spec_name}, {len(source)} bytes, {filepath}) - finished\n")
