import asyncio
import hashlib
import os
import socket
from typing import Any, Optional, cast

from immutabledict import immutabledict
from mcdp import InPortName, OutPortName
from mcdp_dp import get_dp_bounds2
from mcdp_lang import should_compile
from mcdp_maps_ul1 import CannotConvergeAfterManyIterations
from mcdp_ndp import NamedDPAny
from mcdp_posets import UpperSet
from mcdp_utils_misc import ByAttributes, yaml_dump_pretty, yaml_repr1
from numpy.random import default_rng
from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_commons.fs import DirPath, joind, joinf, write_ustring_to_utf8_file
from zuper_commons.text import LibraryName, SpecName, ThingName
from zuper_commons.types import add_context
from zuper_ide_interface import (
    CODE,
    Identities,
    PRODUCT_INTERPRETED,
    SPEC_MODELS,
    Specnames,
    get_cde_interface,
    get_loader_interface,
)
from zuper_utils_augres import (
    AR,
    ImportSourceLocalFS,
    parse_import,
)
from zuper_utils_language import EvalSuccess, ThingResult
from zuper_zapp import ZappEnv, zapp1

__all__ = [
    "create_test_cases_main",
]


@zapp1()
async def create_test_cases_main(ze: ZappEnv) -> ExitCode:
    """Create the test cases."""
    desc = "create_test_cases"
    sti = ze.sti
    # logger = sti.logger
    sti.started()
    parser = ZArgumentParser()
    parser.add_argument("--github-username", default="anonymous", help="Github username")
    parser.add_argument("--source", required=True, help="URL of repository")
    parser.add_argument("--only-libraries", required=False, action="append", default=[])
    parser.add_argument(
        "--only-single-output",
        default=False,
        action="store_true",
        help="Only generate test cases with a single output",
    )
    parser.add_argument(
        "--only-exact",
        default=False,
        action="store_true",
        help="Only generate test cases only for exact",
    )
    parser.add_argument("-o", "--output", required=False, help="destination dir", default="tmp-downloaded")
    parsed = parser.parse_args(args=ze.args)
    source_spec = parsed.source
    only_single_output = parsed.only_single_output
    dest = cast(DirPath, parsed.output)

    if os.path.exists(source_spec):
        path = os.path.abspath(source_spec)
        machine = socket.gethostname()
        source_res = AR.pure(ImportSourceLocalFS(machine, path))
    else:
        source_res = parse_import(source_spec)
    import_source = source_res.get_result()

    cde = await get_cde_interface(sti)
    loader = await get_loader_interface(sti)

    if parsed.github_username == "anonymous":
        github_username = None
    else:
        github_username = parsed.github_username

    identity = Identities(github_username=github_username)

    os.makedirs(dest, exist_ok=True)

    only_libs = parsed.only_libraries
    only_exact = parsed.only_exact

    errors: list[str] = []

    async with cde.session(identity, desc) as cde_session:
        view = await cde_session.get_view()
        shelf = await view.get_shelf_view(import_source)

        async with shelf.session(desc) as shelf_session:
            libraries_view = await shelf_session.libraries()
            libraries = await libraries_view.lists()
            for o in only_libs:
                if o not in libraries:
                    raise ValueError(f"Could not find library {o} in {libraries}")
            for library_name in libraries:
                logger.info(f"library {library_name}")

                use = not only_libs or library_name in only_libs
                if not use:
                    logger.info(f"Skipping {library_name}")
                    continue

                library_view = await libraries_view.get(library_name)
                specs_view = await library_view.specs()
                specs_to_use = [
                    Specnames.SPEC_MODELS,
                    Specnames.SPEC_TEMPLATES,
                    Specnames.SPEC_POSETS,
                    Specnames.SPEC_PRIMITIVEDPS,
                    Specnames.SPEC_VALUES,
                ]
                for spec_name in specs_to_use:
                    spec_view = await specs_view.get(spec_name)
                    for thing_name in await spec_view.lists():
                        job_name = f"{library_name}/{spec_name}/{thing_name}"
                        # logger.info(job_name)

                        thing = await spec_view.get(thing_name)
                        code_view = await thing.get(CODE)
                        code: Optional[bytes] = await code_view.get(desc=desc)
                        if code is None:
                            msg = f"Could not get code for {job_name}"
                            raise ValueError(msg)

                        should = should_compile(code.decode())
                        if not should:
                            continue

                        async with loader.session_from_cde_session(cde_session, identity, desc) as loader_session:
                            products = await loader_session.get_products(import_source, library_name, spec_name, thing_name)
                            product = await products.get(PRODUCT_INTERPRETED)
                            result = await product.get(desc=desc)
                            tr: ThingResult[Any]
                            si, tr = result.split()

                            match tr.result:
                                case EvalSuccess(object=ob):
                                    with add_context(
                                        ob=ob, library_name=library_name, spec_name=spec_name, thing_name=thing_name
                                    ):
                                        try:
                                            await do1(
                                                ob,
                                                dest,
                                                library_name,
                                                spec_name,
                                                thing_name,
                                                only_single_output,
                                                only_exact=only_exact,
                                            )
                                        except CannotConvergeAfterManyIterations as e:
                                            logger.error(f"Could not evaluate {job_name}: {e}", res=tr)
                                            errors.append(job_name)
                                        else:
                                            logger.info(job_name)

                                case _:
                                    logger.error(f"Could not evaluate {job_name}")
                                    errors.append(job_name)

                        # logger.info(job_name)
                        # logger.info(jobs=results)
    if errors:
        logger.error(f"Could not evaluate {len(errors)} jobs", errors=errors)
        return ExitCode.OTHER_EXCEPTION

    return ExitCode.OK


from . import logger


async def do1(
    ob: ByAttributes,
    dest0: DirPath,
    library_name: LibraryName,
    spec_name: SpecName,
    thing_name: ThingName,
    only_single_output: bool,
    only_exact: bool,
) -> None:
    as_yaml = ob.yaml_repr1()
    destlib = joind(dest0, library_name)
    raw_content = yaml_dump_pretty(as_yaml)
    fn_mcdp = joinf(destlib, f"{library_name}.{spec_name}.{thing_name}.mcdpr1.yaml")
    write_ustring_to_utf8_file(raw_content, fn_mcdp)
    if spec_name != SPEC_MODELS:
        return
    ndp = cast(NamedDPAny, ob)

    dp = ndp.flatten().get_dp()

    logger.info(f"Running for {library_name}/{thing_name}")
    fn_dp = f"{library_name}.primitivedps.{thing_name}.mcdpr1.yaml"
    fn2 = joinf(destlib, fn_dp)
    as_yaml = dp.yaml_repr1()

    raw_content = yaml_dump_pretty(as_yaml)
    write_ustring_to_utf8_file(raw_content, fn2)

    F = dp.get_F()
    R = dp.get_R()
    fnames = ndp.get_fnames()
    rnames = ndp.get_rnames()

    def convert_r(r: Any) -> "immutabledict[InPortName, Any]":
        if len(rnames) == 1:
            return immutabledict({rnames[0]: r})
        else:
            return immutabledict({k: v for k, v in zip(rnames, r)})

    def convert_f(f: Any) -> "immutabledict[OutPortName, Any]":
        if len(fnames) == 1:
            return immutabledict({fnames[0]: f})
        else:
            return immutabledict({k: v for k, v in zip(fnames, f)})

    # UR = dp.get_UR()
    # solve_f = dp.get_solve_f_map()
    # solve_r = dp.get_solve_r_map()

    rng = default_rng(string_to_int(fn_dp))
    F_test_chain = F.get_test_chain(10, rng)
    # logger.info(solve_f=solve_f,
    #             test_chain=F_test_chain, )
    n_opt = n_pess = 10

    # if exact := solve_f.get_exact():
    #     for i, f_min_i in enumerate(F_test_chain):
    #         solve_result = exact.u1map_call(f_min_i)
    #         the_interval = Interval(pessimistic=solve_result,
    #                                 optimistic=solve_result)
    #         test_data = {
    #             'dp': pmbm,
    #             'query': 'FixFunMinRes',
    #             'approximated': False,
    #             'f_min': yaml_repr1(f_min_i),
    #             'result': yaml_repr1(the_interval),
    #         }
    #         logger.info(test_data=test_data)
    #         queryname = f'{library_name}.queries.FixFunMinRes.{thing_name}-{i:04d}.mcdpr1.yaml'
    #         fn3 = joinf(dest, queryname)
    #         raw_content = yaml_dump_pretty(test_data)
    #         write_ustring_to_utf8_file(raw_content, fn3)
    # else:
    opb = get_dp_bounds2(dp, n_opt, n_pess)

    if only_single_output:
        do_fixfunminres = len(rnames) == 1
        do_fixresmaxfun = len(fnames) == 1
    else:
        do_fixfunminres = True
        do_fixresmaxfun = True

    solve_r_map = dp.get_solve_r_map()
    if only_exact and not solve_r_map.is_exact():
        logger.warn("Not exact", library_name=library_name, thing_name=thing_name, solve_r_map=solve_r_map)
        do_fixresmaxfun = False
    solve_f_map = dp.get_solve_f_map()
    if only_exact and not solve_f_map.is_exact():
        logger.warn("Not exact", library_name=library_name, thing_name=thing_name, solve_f_map=solve_f_map)
        do_fixfunminres = False
    qname = "FixFunMinRes"
    if do_fixfunminres:
        solve_f_map_opt = opb.opt.get_solve_f_map().get_exact_or_raise()
        solve_f_map_pess = opb.pess.get_solve_f_map().get_exact_or_raise()

        for i, f_min_i in enumerate(F_test_chain):
            solve_result_opt = solve_f_map_opt.u1map_call(f_min_i)

            # approximated = solve_f_map_opt != solve_f_map_pess
            solve_result_pess = solve_f_map_pess.u1map_call(f_min_i)
            the_interval: Interval = Interval(pessimistic=solve_result_pess, optimistic=solve_result_opt)
            approximated = solve_result_pess != solve_result_opt

            test_data = {
                "dp": fn_dp,
                "query": qname,
                "approximated": approximated,
                "value": yaml_repr1(f_min_i),
                "result": yaml_repr1(the_interval),
            }
            logger.info(test_data=test_data)
            queryname = f"{library_name}.dp-queries.{qname}.{thing_name}-{i:04d}.mcdpr1.yaml"
            fn3 = joinf(destlib, queryname)
            raw_content = yaml_dump_pretty(test_data)
            logger.info(
                queryname=queryname,
                test_data=test_data,
                f_min_i=F.format(f_min_i),
                result_pess=solve_result_pess,
                result_opt=solve_result_opt,
            )
            write_ustring_to_utf8_file(raw_content, fn3)

            solve_result_pess2 = UpperSet.from_collection([convert_r(_) for _ in solve_result_pess.minimals])
            solve_result_opt2 = UpperSet.from_collection([convert_r(_) for _ in solve_result_opt.minimals])
            the_interval2 = Interval(pessimistic=solve_result_pess2, optimistic=solve_result_opt2)
            test_data = {
                "mcdp": fn_mcdp,
                "query": qname,
                "approximated": approximated,
                "value": yaml_repr1(convert_f(f_min_i)),
                "result": yaml_repr1(the_interval2),
            }

            queryname = f"{library_name}.mcdp-queries.{qname}.{thing_name}-{i:04d}.mcdpr1.yaml"
            fn3 = joinf(destlib, queryname)
            raw_content = yaml_dump_pretty(test_data)
            write_ustring_to_utf8_file(raw_content, fn3)
            logger.info(test_data=test_data)

            await asyncio.sleep(0)

    qname = "FixResMaxFun"
    R_test_chain = R.get_test_chain(10, rng)

    if do_fixresmaxfun:
        solve_r_map_opt = opb.opt.get_solve_r_map().get_exact_or_raise()
        solve_r_map_pess = opb.pess.get_solve_r_map().get_exact_or_raise()

        for i, r_max_i in enumerate(R_test_chain):
            # approximated = solve_r_map_opt != solve_r_map_pess
            #
            # if approximated:
            #     logger.warning(
            #         f"Approximated {library_name}/{thing_name}",
            #         solve_r_map_opt=solve_r_map_opt,
            #         solve_r_map_pess=solve_r_map_pess,
            #     )
            #     await asyncio.sleep(0)

            solve_r_result_opt = solve_r_map_opt.l1map_call_one(r_max_i).to_lower_set(F)

            solve_r_result_pess = solve_r_map_pess.l1map_call_one(r_max_i).to_lower_set(F)
            approximated = solve_r_result_opt != solve_r_result_pess
            the_interval = Interval(pessimistic=solve_r_result_pess, optimistic=solve_r_result_opt)

            test_data = {
                "dp": fn_dp,
                "query": qname,
                "approximated": approximated,
                "value": yaml_repr1(r_max_i),
                "result": yaml_repr1(the_interval),
            }
            logger.info(test_data=test_data)
            queryname = f"{library_name}.dp-queries.{qname}.{thing_name}-{i:04d}.mcdpr1.yaml"
            fn3 = joinf(destlib, queryname)
            raw_content = yaml_dump_pretty(test_data)
            write_ustring_to_utf8_file(raw_content, fn3)
            await asyncio.sleep(0)

            rnames = ndp.get_rnames()

            if len(rnames) == 1:
                dict_value = {rnames[0]: r_max_i}
            else:
                dict_value = {k: v for k, v in zip(rnames, r_max_i)}

            test_data = {
                "mcdp": fn_mcdp,
                "query": qname,
                "approximated": approximated,
                "value": yaml_repr1(dict_value),
                "result": yaml_repr1(the_interval),
            }
            logger.info(test_data=test_data)
            queryname = f"{library_name}.mcdp-queries.{qname}.{thing_name}-{i:04d}.mcdpr1.yaml"
            fn3 = joinf(destlib, queryname)
            raw_content = yaml_dump_pretty(test_data)
            write_ustring_to_utf8_file(raw_content, fn3)


def string_to_int(seed: str) -> int:
    return int(hashlib.sha256(seed.encode("utf-8")).hexdigest(), 16)


class Interval(ByAttributes):
    def __init__(self, *, pessimistic: object, optimistic: object):
        self.pessimistic = pessimistic
        self.optimistic = optimistic
