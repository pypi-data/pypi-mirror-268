from typing import Callable, Generic, TypeVar, cast

import zuper_html as zh
from mcdp_dp import PrimitiveDP, PrimitiveDPAny
from mcdp_figures import DataFormats, MakeFiguresNDP, MakeFigures_Formatter, ndp_figure2function
from mcdp_gdc import NoImages
from mcdp_library import MCDPLibrary, specs
from mcdp_ndp import NamedDP, NamedDPAny, QueryDefinition
from mcdp_utils_misc import Representable, yaml_dump_pretty, yaml_repr1
from zuper_commons.text import SpecName
from zuper_commons.types import check_isinstance
from zuper_html import console_pre, contents_from_ansi
from zuper_html_plus import html_from_object
from zuper_ide_interface import (
    Specnames,
    VisualizationContext,
    VisualizationFunction,
    VisualizationInfo,
    VisualizationResult,
    available_visualizations,
)
from zuper_ide_interface.interface_spec import ImageProduct2

if True:
    # note: need to import this
    import mcdp_figures as need_to_import

    _ = need_to_import

__all__ = [
    "available_visualizations",
]

X = TypeVar("X")


class DefaultSpecVisualization(VisualizationFunction[X]):
    def __init__(self, specname: SpecName):
        self.specname = specname

    def __call__(self, vc: VisualizationContext[X]) -> VisualizationResult:
        image_source = NoImages()
        library = MCDPLibrary()
        spec = specs[self.specname]
        assert spec.get_png_data is not None
        png_data: bytes = spec.get_png_data(
            image_source=image_source,
            name=vc.thing_name,
            thing=vc.thing,
            data_format="png",
            library=library,
        )
        ip = ImageProduct2(data=png_data, mime="image/png")
        return VisualizationResult(ip, None)


class InternalVisualization(Generic[X], VisualizationFunction[X]):
    def __call__(self, vc: VisualizationContext[X]) -> VisualizationResult:
        as_tag = html_from_object(vc.thing)
        return VisualizationResult(None, as_tag)


class YAMLRepresentation(Generic[X], VisualizationFunction[X]):
    def __call__(self, vc: VisualizationContext[X]) -> VisualizationResult:
        as_data = yaml_repr1(vc.thing)
        yaml_data = yaml_dump_pretty(as_data)
        as_tag = zh.pre(yaml_data)
        return VisualizationResult(None, as_tag)


class DPYAMLRepresentation(Generic[X], VisualizationFunction[X]):
    def __call__(self, vc: VisualizationContext[X]) -> VisualizationResult:
        t: NamedDPAny = check_isinstance(vc.thing, NamedDP)

        dp = cast(PrimitiveDPAny, t.get_dp())
        as_data = yaml_repr1(dp)
        yaml_data = yaml_dump_pretty(as_data)
        as_tag = zh.pre(yaml_data)
        return VisualizationResult(None, as_tag)


class ReprVisualization(Generic[X], VisualizationFunction[X]):
    def __init__(self, compact: bool):
        self.compact = compact

    def which_piece(self, x: X) -> Representable:
        return cast(Representable, x)

    def __call__(self, vc: VisualizationContext[X]) -> VisualizationResult:
        piece = self.which_piece(vc.thing)
        r = check_isinstance(piece, Representable)
        if self.compact:
            as_str = r.repr_compact()
        else:
            as_str = r.repr_long()
        as_tag = console_pre(*contents_from_ansi(as_str))
        return VisualizationResult(None, as_tag)


class ReprDP(ReprVisualization[NamedDPAny]):
    def which_piece(self, x: NamedDPAny) -> Representable:
        return x.get_dp()


class ReprDPDetail(ReprVisualization[NamedDPAny]):
    def __init__(self, compact: bool, which: Callable[[PrimitiveDPAny], Representable]):
        super().__init__(compact)
        self.which = which

    def which_piece(self, x: NamedDPAny) -> Representable:
        dp = x.get_dp()
        return self.which(dp)


class ReprLegacy(VisualizationFunction[NamedDPAny]):
    data_format: DataFormats

    def __init__(self, which: str, data_format: DataFormats):
        self.data_format = data_format
        self.constructors, self.params = ndp_figure2function[which]

    def __call__(self, vc: VisualizationContext[NamedDPAny]) -> VisualizationResult:
        x = cast(MakeFigures_Formatter, self.constructors(**self.params))
        # logger.info(x=x)
        ndp = vc.thing
        mf = MakeFiguresNDP(ndp=ndp, yourname=vc.thing_name, image_source=None)
        (data,) = x.get(mf, (self.data_format,))
        # assert isinstance(data, bytes), data
        if isinstance(data, str):
            data = data.encode("utf8")

        ip = ImageProduct2(data=data, mime="image/svg+xml")
        return VisualizationResult(ip, None)


FT = TypeVar("FT")
RT = TypeVar("RT")


class ReprLegacyQuery(VisualizationFunction[QueryDefinition[FT, RT]]):
    vs: VisualizationFunction[NamedDPAny]

    def __init__(self, vs: VisualizationFunction[NamedDPAny]):
        self.vs = vs

    def __call__(self, vc: VisualizationContext[QueryDefinition[FT, RT]]) -> VisualizationResult:
        ndp = vc.thing.model
        vc2 = VisualizationContext(thing_name=vc.thing_name, thing=ndp)
        return self.vs(vc2)


for specname_, spec_ in specs.items():
    for_this = {}
    if spec_.get_png_data is not None:
        for_this["default"] = VisualizationInfo(
            zh.span("Graphical"),  #
            DefaultSpecVisualization(specname_),  # type: ignore
        )

    for_this["repr_long"] = VisualizationInfo(
        zh.span("Long representation"),  #
        ReprVisualization(compact=False),  # type: ignore
    )

    for_this["repr_compact"] = VisualizationInfo(
        zh.span("Compact representation"),  #
        ReprVisualization(compact=True),  # type: ignore
    )

    for_this["internal"] = VisualizationInfo(zh.span("Raw internal representation"), InternalVisualization())
    for_this["yaml_repr_v1"] = VisualizationInfo(zh.span("YAML representation"), YAMLRepresentation())

    if specname_ == Specnames.SPEC_MODELS:
        for_this["dp"] = VisualizationInfo(zh.span("Compiled DP"), ReprDP(compact=True))
        for_this["dp_repr_v1"] = VisualizationInfo(zh.span("Compiled DP - YAML representation"), DPYAMLRepresentation())

        for_this["space_F"] = VisualizationInfo(
            zh.span("Poset F"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_F),  # type: ignore
        )
        for_this["space_R"] = VisualizationInfo(
            zh.span("Poset R"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_R),  # type: ignore
        )
        for_this["space_I"] = VisualizationInfo(
            zh.span("Poset I (implementations)"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_I),  # type: ignore
        )
        for_this["space_B"] = VisualizationInfo(
            zh.span("Space B (blueprint-relevant implementations)"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_B),  # type: ignore
        )
        for_this["map_I_to_B"] = VisualizationInfo(
            zh.span("Map I → B"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_b_from_i_map),  # type: ignore
        )
        for_this["solve_f_map"] = VisualizationInfo(
            zh.span("Map F → UR"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_solve_f_map),  # type: ignore
        )
        for_this["solve_r_map"] = VisualizationInfo(
            zh.span("Map R → LF"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_solve_r_map),  # type: ignore
        )
        for_this["prov_map"] = VisualizationInfo(
            zh.span("Map provides: I → F"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_prov_map),  # type: ignore
        )
        for_this["req_map"] = VisualizationInfo(
            zh.span("Map requires: I → R"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_req_map),  # type: ignore
        )
        for_this["fopr_feasibility"] = VisualizationInfo(
            zh.span("Map feasibility: F x R' → Bool"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_fopr_feasibility),  # type: ignore
        )

        for_this["i_availability"] = VisualizationInfo(
            zh.span("Map availability: I → Bool"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_i_availability_map),  # type: ignore
        )

        for_this["sc_f_b_r_map"] = VisualizationInfo(
            zh.span("Map F → UR[B]"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_sc_f_b_r_map),  # type: ignore
        )
        for_this["sc_r_b_f_map"] = VisualizationInfo(
            zh.span("Map R → LF[B]"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_sc_r_b_f_map),  # type: ignore
        )
        for_this["sc_f_i_r_map"] = VisualizationInfo(
            zh.span("Map F → UR[I]"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_sc_f_i_r_map),  # type: ignore
        )
        for_this["sc_r_i_f_map"] = VisualizationInfo(
            zh.span("MapRF → LF[I]"),  #
            ReprDPDetail(compact=True, which=PrimitiveDP.get_sc_r_i_f_map),  # type: ignore
        )

        for k in ndp_figure2function:
            for_this[k + "-svg"] = VisualizationInfo(zh.span(f"Figure: {k}"), ReprLegacy(k, "svg"))

    if specname_ == Specnames.SPEC_QUERIES:
        for k in ndp_figure2function:
            for_this["model-" + k + "-svg"] = VisualizationInfo(zh.span(f"Figure: {k}"), ReprLegacyQuery(ReprLegacy(k, "svg")))

    available_visualizations[specname_] = for_this  # type: ignore
# logger.info(a=ndp_figure2function
#             , available_visualizations=available_visualizations)
