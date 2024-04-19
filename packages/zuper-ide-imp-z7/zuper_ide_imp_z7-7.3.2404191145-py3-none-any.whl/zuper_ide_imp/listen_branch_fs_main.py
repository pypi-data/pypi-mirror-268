from typing import cast

from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_commons.text import GitBranchName, GitOrgName, GitRepoName, GitUsername
from zuper_ide_interface import GITHUB_PROVIDER_NAME, Identities, get_cde_interface
from zuper_utils_asyncio import (
    MyAsyncExitStack,
)
from zuper_zapp import ZappEnv, zapp1

__all__ = [
    "listen_branch_fs",
]


@zapp1()
async def listen_branch_fs(ze: ZappEnv) -> ExitCode:
    sti = ze.sti
    sti.started()
    parser = ZArgumentParser()
    parser.add_argument("--github-username", required=True, help="Github username")
    parser.add_argument("--org", required=True, help="Orgname")
    parser.add_argument("--repo", required=True, help="Repo name")
    parser.add_argument("--branch", required=True, help="Branch name")
    parser.add_argument("--editing", default=False, action="store_true")
    parsed = parser.parse_args(args=ze.args)
    org_name = cast(GitOrgName, parsed.org)
    repo_name = cast(GitRepoName, parsed.repo)
    branch_name = cast(GitBranchName, parsed.branch)

    # triggered_by = cast(EventID, 1)
    # pri = cast(PriorityLevel, 9.0)
    # pool = await get_pgpool(sti)
    # desc = "listen_branch_fs"

    cde = await get_cde_interface(sti)
    editing = parsed.editing
    # gh_app_id = get_gh_app_id_from_env()
    # async with pool.connection(desc) as c:
    #     # gh_inst_id = await zuper_db_gh.read_org_inst(c, gh_app_id, org_name)
    #     add = await zuper_db_gh.read_repo_address_from_fullname(c, gh_app_id, org_name, repo_name)

    github_username = cast(GitUsername, parsed.github_username)
    identities = Identities(github_username=github_username)

    async with MyAsyncExitStack(sti) as S:
        async with cde.session(identities, "init") as vb:
            view = await vb.get_view()

            providers = await view.providers()
            provider = await providers.get(GITHUB_PROVIDER_NAME)
            orgs = await provider.orgs()
            org = await orgs.get(org_name)
            repos = await org.repos()
            repo = await repos.get(repo_name)
            branches = await repo.branches()
            branch = await branches.get(branch_name)

            if editing:
                version = await branch.cur()
            else:
                version = await branch.follow()

            await version.shelf()

            raise NotImplementedError()
            #
            # async with vb.fs.session("init") as session:
            #     files = await listfiles(sti, session, cast(DirPath, '.'))
            #     sti.logger.info(files=files)
            #
            # async with wait_for_event() as si:
            #     async def on_event(fsp: EventPacket) -> None:
            #         sti.logger.info("got fs event packet", event=fsp)
            #
            #     async with vb.fs.session("watch dir") as fs:
            #         await fs.watch_dir(cast(RelDirPath, "."), on_event, si.astop)

    return ExitCode.OK
