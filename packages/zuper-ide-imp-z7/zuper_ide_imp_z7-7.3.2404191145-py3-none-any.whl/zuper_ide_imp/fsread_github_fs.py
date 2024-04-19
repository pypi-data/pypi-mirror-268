from typing import cast

import zuper_db_gh
from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_commons.fs import DirPath
from zuper_commons.text import AccountName, GitBranchName, GitRepoName
from zuper_db_ev import EventID
from zuper_db_gh import read_org_inst
from zuper_github_api import get_gh_app_id_from_env
from zuper_github_services import RepoLowLevelDBMaster
from zuper_utils_fs import listfiles
from zuper_utils_git_fs import FSGitTranslation, get_translation
from zuper_utils_pg import get_pgpool
from zuper_zapp import ZappEnv, zapp1

__all__ = [
    "fsread_main_github_fs",
]


@zapp1()
async def fsread_main_github_fs(ze: ZappEnv) -> ExitCode:
    sti = ze.sti
    sti.started()
    desc = "fsread_main_github_fs"
    parser = ZArgumentParser()
    parser.add_argument("--org", required=True, help="Orgname")
    parser.add_argument("--repo", required=True, help="Repo name")
    parser.add_argument("--branch", required=True, help="Branch name")
    parsed = parser.parse_args(args=ze.args)

    org = cast(AccountName, parsed.org)
    repo = cast(GitRepoName, parsed.repo)
    branch_name = cast(GitBranchName, parsed.branch)
    gh_app_id = get_gh_app_id_from_env()
    pool = await get_pgpool(ze.sti)
    async with pool.connection(desc) as c:
        gh_inst_id = await read_org_inst(c, gh_app_id, org)
        repo_details = await zuper_db_gh.read_repo_by_name(c, gh_app_id, org, repo)

    lr = RepoLowLevelDBMaster(gh_inst_id, repo_details.gh_repo_node_id, org, repo, EventID(1), pool)
    await lr.init(sti)
    fs_git: FSGitTranslation
    async with get_translation(sti, lr, branch_name) as fs_git:
        async with fs_git.session("list") as fs:
            root = cast(DirPath, ".")
            s = await listfiles(sti, fs, root)
            sti.logger.user_info(s)
    return ExitCode.OK
