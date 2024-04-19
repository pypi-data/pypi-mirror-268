import asyncio
import os
import socket
import traceback
from asyncio import CancelledError
from typing import Any, Optional, cast

from mcdp import MCDPConstants
from mcdp_lang import should_compile
from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_commons.text import ThingName
from zuper_commons.types import ZValueError, add_context
from zuper_ide_interface import CODE, Identities, ProductsView, Specnames, get_loader_interface
from zuper_utils_asyncio import UpdateNoPrevious
from zuper_utils_augres import (
    AR,
    EntityThing,
    ImportSourceLocalFS,
    parse_import,
)
from zuper_utils_language import ThingResult
from zuper_zapp import ZappEnv, zapp1

__all__ = [
    "mcdp_repo_load_all_main",
]


@zapp1()
async def mcdp_repo_load_all_main(ze: ZappEnv) -> ExitCode:
    """Load all specs in a repo."""
    sti = ze.sti
    logger = sti.logger
    sti.started()
    parser = ZArgumentParser()
    parser.add_argument("--github-username", default="anonymous", help="Github username")
    parser.add_argument("--source", required=True, help="local directory or URL of repository")
    parser.add_argument("--only", default=None, help="thing name")
    parser.add_argument("--raise", dest="raise_exceptions", default=False, action="store_true", help="Raise exceptions")
    parser.add_argument("--editing", action="store_true", default=False, help="Editing mode")
    parser.add_argument("--no-products", action="store_true", default=False, help="do not load the products")
    parser.add_argument("--streaming", action="store_true", default=False, help="use streaming")

    parsed = parser.parse_args(args=ze.args)
    no_products = parsed.no_products
    use_streaming = parsed.streaming
    source_spec = parsed.source
    raise_exceptions = parsed.raise_exceptions

    if os.path.exists(source_spec):
        path = os.path.abspath(source_spec)
        machine = socket.gethostname()
        source_res = AR.pure(ImportSourceLocalFS(machine, path))
    else:
        source_res = parse_import(source_spec)

    # cde = await get_cde_interface(sti)

    if parsed.github_username == "anonymous":
        github_username = None
    else:
        github_username = parsed.github_username

    identity = Identities(github_username=github_username)
    loader = await get_loader_interface(sti)

    async with loader.session(identity, "mcdp_repo_load_all_main") as session:
        source = source_res.get_result()
        logger.info(source=source)
        shelf_view = await session.get_shelf_view(source)

        errors: dict[tuple[str, ...], Any] = {}

        async def load_job(
            address: EntityThing,
        ) -> Optional[UpdateNoPrevious[AR[ThingResult[Any]]]]:
            key: tuple[str, ...] = ("load_job", address.library_name, address.spec_name, address.thing_name)
            with add_context(address=address):
                desc = f"load_job:{address.thing_name}"
                logger.info("load job", address=address)
                try:
                    view = await session.obtain_address(address)
                    logger.info("get_eo", address=address)
                    # logger.info(library=the_library, spec=the_spec, thing=the_thing, res=res)
                    res = await view.get_eo(desc=desc)
                    # logger.info("obtained", address=address, res=res)
                    cur = res.current
                    cur.assert_no_error()
                    return res
                except CancelledError:
                    raise
                except Exception:  # OK
                    if raise_exceptions:
                        raise
                    errors[key] = traceback.format_exc()
                    logger.error(errors[key])
                    return None

        async def products_job(
            address: EntityThing,
        ) -> None:
            key: tuple[str, ...] = ("products_job", address.library_name, address.spec_name, address.thing_name)
            desc = f"producs_job:{address.thing_name}"
            with add_context(address=address):
                logger.info("considering", address=address)
                try:
                    products_view: ProductsView = await session.get_products_address(address)
                    products = await products_view.lists()
                    logger.info(f"products", the_thing=address, products=products)

                    for p in products:
                        product = await products_view.get(p)
                        res = await product.get(desc=desc)
                        logger.info("ok", product=p, address=address, res=res)
                except CancelledError:
                    raise
                    # logger.info(library=the_library, spec=the_spec, thing=the_thing, res=res)
                except Exception:
                    if raise_exceptions:
                        raise
                    errors[key] = traceback.format_exc()
                    logger.error(errors[key])
                    return None

        # jobs: list[Awaitable[Any]] = []
        async with shelf_view.session("cde") as shelf_session:
            libraries_view = await shelf_session.libraries()
            libraries = await libraries_view.lists()
            for library_name in libraries:
                logger.info(f"library {library_name}")
                library_view = await libraries_view.get(library_name)
                specs_view = await library_view.specs()

                all_files = await specs_view.get(Specnames.SPEC_ALL_FILES)
                if await all_files.exists(cast(ThingName, MCDPConstants.TEST_IGNORE_FILE)):
                    logger.info(f"Skipping {library_name} because of .mcdp_test_ignore")
                    continue

                specs_to_use = [
                    Specnames.SPEC_MODELS,
                    Specnames.SPEC_TEMPLATES,
                    Specnames.SPEC_POSETS,
                    Specnames.SPEC_PRIMITIVEDPS,
                    Specnames.SPEC_VALUES,
                    Specnames.SPEC_QUERIES,
                ]
                for spec_name in specs_to_use:
                    spec_view = await specs_view.get(spec_name)
                    for thing_name in await spec_view.lists():
                        job_name = f"{library_name}/{spec_name}/{thing_name}"

                        if parsed.only is not None:
                            if parsed.only not in thing_name:
                                logger.debug(f"{job_name} skipped")
                                continue
                            else:
                                logger.info(f"{job_name} selected")

                        thing = await spec_view.get(thing_name)
                        code_view = await thing.get(CODE)
                        code: Optional[bytes] = await code_view.get(desc="loading")
                        if code is None:
                            raise ZValueError(f"Could not get code for {job_name}")

                        address0 = EntityThing(source, library_name, spec_name, thing_name)
                        if should_compile(code.decode()):
                            logger.info(job_name)
                            await asyncio.sleep(0)
                            j = load_job(address0)
                            await j
                            await asyncio.sleep(0)

                            if not no_products:
                                j2 = products_job(address0)
                                await j2
                        else:
                            logger.info(f"{job_name} - skipping")
                logger.info(f"library {library_name} - finished")
            logger.info(f"libraries - finished")
            # jobs.append(j)
            # jobs.append(job)

        # _results = await asyncio.gather(*jobs, return_exceptions=True)

        if errors:
            logger.error(errors=errors)
            return ExitCode.OTHER_EXCEPTION
        # for r in results:
        #     if isinstance(r, Exception):
        #         logger.error(str(r))

        # logger.info(jobs=results)
    return ExitCode.OK
