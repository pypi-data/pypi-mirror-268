import asyncio
from typing import Any

from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_ide_interface import (
    GITHUB_PROVIDER_NAME,
    Identities,
    get_loader_interface,
)
from zuper_utils_asyncio import SubscriberInfo
from zuper_utils_augres import (
    EntityThing,
    ImportGitBranchVersion,
    ImportGitDefaultBranch,
    ImportGitGithubRepo,
    ImportSourceGit,
    ImportVersion,
)
from zuper_zapp import ZappEnv, zapp1

__all__ = [
    "mcdp_view_main_cde",
]


@zapp1()
async def mcdp_view_main_cde(ze: ZappEnv) -> ExitCode:
    desc = "mcdp_view_main_cde"
    sti = ze.sti
    sti.started()
    logger = sti.logger
    parser = ZArgumentParser()
    parser.add_argument("--github-username", default="anonymous", help="Github username")
    parser.add_argument("--provider", default=GITHUB_PROVIDER_NAME, help="Provider")
    parser.add_argument("--org", required=False, help="Orgname")
    parser.add_argument("--repo", required=False, help="Repo name")
    parser.add_argument("--branch", required=False, help="Branch name")
    parser.add_argument("--editing", action="store_true", default=False, help="Editing mode")
    parser.add_argument("--library", required=False, help="Library name")
    parser.add_argument("--spec", required=False, help="Spec name")
    parser.add_argument("--thing", required=False, help="Thing name")

    parsed = parser.parse_args(args=ze.args)
    provider = parsed.provider  # TODO: assemble from provider
    org = parsed.org
    repo = parsed.repo
    branch = parsed.branch
    library = parsed.library
    spec = parsed.spec
    thing = parsed.thing
    editing = parsed.editing
    # cde = await get_cde_interface(sti)

    if parsed.github_username == "anonymous":
        github_username = None
    else:
        github_username = parsed.github_username

    identity = Identities(github_username=github_username)

    version: ImportVersion
    if branch is None:
        version = ImportGitDefaultBranch(editing)
    else:
        version = ImportGitBranchVersion(branch, editing)

    import_source = ImportSourceGit(ImportGitGithubRepo("github.com", org, repo), version)

    loader = await get_loader_interface(sti)

    address = EntityThing(
        import_source=import_source,
        library_name=library,
        spec_name=spec,
        thing_name=thing,
    )
    async with loader.session(identity, "cde_view_main1") as loader_session:
        products = await loader_session.get_products_address(address)

        logger.info(products=products)
        product_names = await products.lists()
        for product_name in product_names:
            product = await products.get(product_name)

            stuff = await product.get(desc=desc)

            async def listen(i: int, x: Any) -> None:
                logger.info("listen", i=i, x=x)

            product.watch(SubscriberInfo(listen, internal_description="listen"))
            logger.info(stuff=stuff)

        logger.info("now sleeping")
        await asyncio.sleep(100000)

    # loader = Loader(cde)
    # await loader.init(sti)
    # async with loader.session(identity) as session:
    #
    #
    #     source_repo = ImportGitGithubRepo("github.com", org, repo)
    #     version = ImportGitBranchVersion(branch, editing=parsed.editing)
    #     import_source = ImportSourceGit(source_repo, version)
    #     res = await session.obtain(
    #         import_source=import_source, library_name=library, spec_name=spec, thing_name=thing
    #     )
    #     logger.info(res=res)
    #     the_thing = await res.get()
    #
    #     logger.info(the_thing=the_thing)
    #

    return ExitCode.OK
