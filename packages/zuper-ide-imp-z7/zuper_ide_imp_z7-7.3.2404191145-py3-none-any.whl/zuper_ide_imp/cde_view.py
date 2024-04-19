from typing import cast

from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_commons.text import GitCommitSHA, GitUsername
from zuper_ide_interface import BranchView, BranchesView, Identities, OrgsView, ReposView, get_cde_interface
from zuper_zapp import ZappEnv, zapp1

from .utils import list_shelf_view

__all__ = [
    "cde_view_main",
]


@zapp1()
async def cde_view_main(ze: ZappEnv) -> ExitCode:
    sti = ze.sti
    sti.started()
    parser = ZArgumentParser()
    parser.add_argument("--github-username", required=True)
    parser.add_argument("--deep", default=False, action="store_true")
    parsed = parser.parse_args(args=ze.args)
    deep = parsed.deep
    user_name = cast(GitUsername, parsed.github_username)

    cde = await get_cde_interface(sti)

    if user_name == "anonymous":
        github_username = None
    else:
        github_username = user_name
    identity = Identities(github_username=github_username)
    async with cde.session(identity, "cde_view_main") as session:
        view = await session.get_view()
        providers = await view.providers()
        sti.logger.info("list of providers", providers=await providers.lists())
        async for provider_name, provider in providers.items():
            orgs: OrgsView = await provider.orgs()

            sti.logger.info(f"provider {provider_name}", orgs=await orgs.lists())

            async for org_name, org in orgs.items():
                repos: ReposView = await org.repos()

                sti.logger.info(f"|- org {org_name}", repos=await repos.lists())
                async for repo_name, repo in repos.items():
                    sti.logger.info(f"|  |-repo {repo_name}")
                    branches: BranchesView = await repo.branches()
                    branch: BranchView
                    async for branch_name, branch in branches.items():
                        # cur_view: VersionView = await branch.cur()
                        # cur_version = await cur_view.version()

                        last_commit: GitCommitSHA = await branch.last()

                        sti.logger.info(f"|  |  |-branch {branch_name} last {last_commit} ")

                        if deep:
                            view2 = await branch.get_commit(last_commit)
                            shelf = await view2.shelf()
                            async with shelf.session("main") as s1:
                                await list_shelf_view(sti, s1)

    return ExitCode.OK
