import asyncio
import traceback
from typing import Any, Optional, TypeVar, cast

import zuper_html as zh
from mcdp_ndp import NamedDPAny
from zuper_commons.types import add_context
from zuper_ide_interface import (
    Identities,
    ImageProductResult,
    ImageRenderFailure,
    LoaderInterface,
    LoaderSessionInterface,
    PRODUCT_INTERPRETED,
    ProductName,
    SourceFailure,
    SourceNotExisting,
    VisualizationContext,
    VisualizationFunction,
    VisualizationInfo,
    VisualizationResult,
    available_visualizations,
)
from zuper_ide_interface.interface_spec import HTMLProduct, ImageProduct2
from zuper_utils_asyncio import (
    GenericWatchable,
    OrderHelper,
    SingleView,
    SubscriberInfo,
    SyncTaskInterface,
    UpdateNoPrevious,
    WatchControl,
    async_errors,
)
from zuper_utils_augres import (
    AR,
    EntityThing,
    LocationContext,
    LocationImportSource,
    LocationUnknown,
    SideInfo,
    ThingInShelf,
)
from zuper_utils_language import (
    EvalFailure,
    EvalSuccess,
    NotExisting,
    ParseFailure,
    ThingResult,
)

X = TypeVar("X")

__all__ = [
    "ThingVisualization",
    "ThingVisualizationProxy",
]


class ThingVisualization:
    address: EntityThing
    _last: Optional[AR[ImageProductResult]]
    _last_source: Optional[AR[ThingResult[Any]]]
    gw: GenericWatchable[UpdateNoPrevious[AR[ImageProductResult]]]
    loader: LoaderInterface
    code_watch: WatchControl
    sti: SyncTaskInterface

    def __init__(self, loader: LoaderInterface, identity: Identities, address: EntityThing, visualizaton_name: str):
        self.loader = loader
        self.address = address
        self.identity = identity
        self._last = None
        self.gw = GenericWatchable(str(address), send_last_on_subscribe=True)
        self.visualization_name = visualizaton_name
        self.tis = ThingInShelf(address.library_name, address.spec_name, address.thing_name)
        self._last_source = None
        self.oh = OrderHelper(f"ThingVisualization:{address.thing_name}")

    async def init(self, sti: SyncTaskInterface) -> None:
        self.sti = sti

    async def aclose(self) -> None:
        await self.gw.finish()

    async def proxy(self, session: LoaderSessionInterface) -> "ThingVisualizationProxy":
        return ThingVisualizationProxy(self, session)

    async def get(self, session: LoaderSessionInterface, *, desc: str) -> AR[ImageProductResult]:
        desc += "/ThingVisualization:get"
        if self._last is None:
            self._last = await self._obtain(session, desc)
        return self._last

    async def on_product_change(self, _: int, x0: UpdateNoPrevious[AR[ThingResult[Any]]]) -> None:
        if self._last_source == x0.current:
            msg = "Ignoring update because it is the same as the last one."
            return

        self._last_source = x0.current

        res = self._last = await self._obtain_from_product(x0.current)
        order = self.oh.add_to(x0.order)
        i = order.origins[self.oh.name]

        up = UpdateNoPrevious(i, res, order)
        await self.gw.distribute(i, up)

    async def _obtain(self, session: LoaderSessionInterface, desc: str) -> AR[ImageProductResult]:
        desc += "/ThingVisualization:_obtain"
        si = SideInfo.empty()
        creator = "_obtain"
        with add_context(address=self.address):
            try:
                products = await session.get_products_address(self.address)
            except KeyError as e:
                tr = ImageProductResult(SourceNotExisting())
                msg = f'Could not find "{self.address.thing_name}" in "{self.address.spec_name}".'
                msg += f": {e}"
                si.notes.note_error(msg, created_file=__file__, created_module=__name__, created_function=creator)
                return si % tr

            product = await products.get(PRODUCT_INTERPRETED)

            self.code_watch = product.watch(SubscriberInfo(self.on_product_change))

            first_product = await product.get(desc=desc)

            res = await self._obtain_from_product(first_product)

            si, ob = res.split_even_errors()
            a = self.address
            context_desc = zh.p("While loading ", zh.code(a.thing_name), " from library ", zh.code(a.library_name), ".")
            l1 = LocationImportSource(self.address.import_source, LocationUnknown())
            lc = LocationContext(context_desc, l1)
            si2 = si.wrap_location(lc)

            return si2.add_to_result(ob)

    @async_errors
    async def _obtain_from_product(self, interpreted: AR[ThingResult[Any]]) -> AR[ImageProductResult]:
        si = SideInfo.empty()
        logger = self.sti.logger

        ires = si << interpreted

        match ires.result:
            case NotExisting():
                return si % ImageProductResult(SourceNotExisting())
            case ParseFailure():
                return si % ImageProductResult(SourceFailure())
            case EvalFailure():
                return si % ImageProductResult(SourceFailure())
            case EvalSuccess(object=the_ob):
                # could be template or NamedDP
                thing = cast(NamedDPAny, the_ob)
            case _:
                raise AssertionError

        for_us = available_visualizations[self.tis.spec_name]
        visualization = cast(ProductName, self.visualization_name)
        to_use: VisualizationInfo[Any] = for_us[visualization]
        vc = VisualizationContext(thing_name=self.tis.thing_name, thing=thing)
        f: VisualizationFunction[Any] = to_use.function
        # noinspection PyBroadException
        try:
            vr: VisualizationResult = await asyncio.to_thread(f, vc)
        except Exception:
            as_str = traceback.format_exc()
            # logger.error(as_str)
            # as_tag = console_pre(*contents_from_ansi(as_str))
            # TODO: add error here
            return si % ImageProductResult(ImageRenderFailure(as_str))

        if vr.figure is None and vr.contents is None:
            msg = "The visualization function did not return a figure or some html."
            logger.error(msg, vr=vr)
        if vr.figure is not None:
            ip = ImageProduct2(vr.figure.data, vr.figure.mime)
        elif vr.contents is not None:
            ip = HTMLProduct(vr.contents)
            # raise DPInternalError(msg, visualization=visualization, to_use=to_use, f=f, vr=vr)  # FIXME: DEV-278:
        else:
            raise AssertionError
        return si % ImageProductResult(ip)


class ThingVisualizationProxy(SingleView[AR[ImageProductResult]]):
    def __init__(self, master: ThingVisualization, session: LoaderSessionInterface):
        self.master = master
        self.session = session

    async def get(self, *, desc: str) -> AR[ImageProductResult]:
        return await self.master.get(self.session, desc=desc)

    def watch(self, info: SubscriberInfo[UpdateNoPrevious[AR[ImageProductResult]]]) -> WatchControl:
        return self.master.gw.watch(info)
