from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_ide_interface import Identities, get_loader_interface
from zuper_utils_augres import (
    ImportGitBranchVersion,
    ImportGitGithubRepo,
    ImportSourceGit,
)
from zuper_zapp import ZappEnv, zapp1

__all__ = [
    "mcdp_view_main",
]


@zapp1()
async def mcdp_view_main(ze: ZappEnv) -> ExitCode:
    sti = ze.sti
    sti.started()
    logger = sti.logger
    parser = ZArgumentParser()
    parser.add_argument("--github-username", default="anonymous", help="Github username")
    parser.add_argument("--provider", default="gh", help="Provider")
    parser.add_argument("--org", required=False, help="Orgname")
    parser.add_argument("--repo", required=False, help="Repo name")
    parser.add_argument("--branch", required=False, help="Branch name")
    parser.add_argument("--editing", action="store_true", default=False, help="Editing mode")
    parser.add_argument("--library", required=False, help="Library name")
    parser.add_argument("--spec", required=False, help="Spec name")
    parser.add_argument("--thing", required=False, help="Thing name")

    parsed = parser.parse_args(args=ze.args)
    provider = parsed.provider
    org = parsed.org
    repo = parsed.repo
    branch = parsed.branch
    library = parsed.library
    spec = parsed.spec
    thing = parsed.thing

    if parsed.github_username == "anonymous":
        github_username = None
    else:
        github_username = parsed.github_username

    identity = Identities(github_username=github_username)
    loader = await get_loader_interface(sti)
    desc = "mcdp_view_main"
    async with loader.session(identity, desc) as session:
        source_repo = ImportGitGithubRepo("github.com", org, repo)
        version = ImportGitBranchVersion(branch, editing=parsed.editing)
        import_source = ImportSourceGit(source_repo, version)
        res = await session.obtain(import_source=import_source, library_name=library, spec_name=spec, thing_name=thing)
        logger.info(res=res)
        the_thing = await res.get(desc=desc)

        logger.info(the_thing=the_thing)
        #
        # logger.info("now sleeping")
        # await asyncio.sleep(100000)
    return ExitCode.OK
