from typing import cast

from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_commons.text import GitBranchName, GitOrgName, GitRepoName
from zuper_db_gh import read_org_inst, read_repo_by_name
from zuper_github_api import get_gh_app_id_from_env, get_ghi
from zuper_github_services import RepoLowLevelHTTPMaster
from zuper_ide_interface import ShelfViewMaster, mcdp_spec_config
from zuper_shelf_fs import ShelfViewFSMaster
from zuper_utils_asyncio import MyAsyncExitStack
from zuper_utils_git import CachedRepoLowLevelMaster, GlobalMemCache
from zuper_utils_git_fs import get_translation
from zuper_utils_pg import get_pgpool
from zuper_zapp import ZappEnv, zapp1

from .utils import list_shelf_view

__all__ = [
    "fsread_main_github",
]


@zapp1()
async def fsread_main_github(ze: ZappEnv) -> ExitCode:
    sti = ze.sti
    logger = sti.logger
    sti.started()
    desc = "fsread_main_github"
    parser = ZArgumentParser()
    parser.add_argument("--org", required=True, help="Orgname")
    parser.add_argument("--repo", required=True, help="Repo name")
    parser.add_argument("--branch", required=True, help="Branch name")
    parsed = parser.parse_args(args=ze.args)

    org = cast(GitOrgName, parsed.org)
    repo = cast(GitRepoName, parsed.repo)
    branch_name = cast(GitBranchName, parsed.branch)

    gh_app_id = get_gh_app_id_from_env()

    pool = await get_pgpool(ze.sti)
    async with pool.connection(desc) as c:
        # app_config = await zuper_db_gh.read_app_config(c, gh_app_id)
        gh_inst_id = await read_org_inst(c, gh_app_id, org)
        repo_details = await read_repo_by_name(c, gh_app_id, org, repo)

    async with MyAsyncExitStack(sti) as S:
        ghi = await get_ghi(sti)
        master1 = await S.init(
            RepoLowLevelHTTPMaster(
                gh_inst_id=gh_inst_id,
                gh_repo_node_id=repo_details.gh_repo_node_id,
                org_name=repo_details.owner_name,
                repo_name=repo_details.repo_name,
                triggered_by=ghi.instance_start_event_id,
                path=None,
                gh_app_id=gh_app_id,
                pool=pool,
                ghi=ghi,
            )
        )
        lr = await S.init(CachedRepoLowLevelMaster(master1, GlobalMemCache))

        # noinspection PyTypeChecker
        fs_git = await S.enter_async_context(get_translation(sti, lr, branch_name))
        shelf_view: ShelfViewMaster = await S.init(
            ShelfViewFSMaster(fs_git, mcdp_spec_config, get_shelf_editing_status=None)
        )  # XXX
        async with shelf_view.session("fsread_main_github") as session:
            logger.info(session=session)
            await list_shelf_view(sti, session)

    return ExitCode.OK


#
# async def list_contents_view(sti: SyncTaskInterface, mcdp_view) -> None:  # type: ignore # XXX
#     logger = sti.logger
#     shelves_view = await mcdp_view.shelves()
#     shelves = await shelves_view.lists()
#     logger.info(shelves=shelves)
#     for shelf_name in shelves:
#         shelf = await shelves_view.get(shelf_name)
#         libraries = await shelf.libraries()
#         logger.info(shelf=shelf_name, libraries=shelves)
#         for l in await libraries.lists():
#             lib = await libraries.get(l)
#             specs = await lib.specs()
#             for s in await specs.lists():
#                 spec = await specs.get(s)
#                 things = await spec.things()
#                 logger.info(library=l, spec=s, things=things)
#                 for t in await things.lists():
#                     thing = await things.get(t)
#                     source = await thing.get_source()
#                     logger.info(thing=t, source=source)
