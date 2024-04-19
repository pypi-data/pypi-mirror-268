import os

from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_commons.types import check_isinstance
from zuper_ide_interface import ShelfViewMaster, mcdp_spec_config
from zuper_shelf_fs import ShelfViewFSMaster, ShelfViewFSSession
from zuper_utils_asyncio import MyAsyncExitStack
from zuper_utils_git import LocalRepo, get_dir_info
from zuper_utils_git_fs import get_translation
from zuper_zapp import ZappEnv, zapp1

from .utils import list_shelf_view

__all__ = [
    "fsread_main_git",
]


@zapp1()
async def fsread_main_git(ze: ZappEnv) -> ExitCode:
    sti = ze.sti
    sti.started()
    parser = ZArgumentParser()
    parser.add_argument("--dir", required=True, help="Repository on filesystem")
    parsed = parser.parse_args(args=ze.args)

    root = parsed.dir
    root = os.path.expanduser(root)

    di = await get_dir_info(sti, root)
    lr = LocalRepo(root)
    await lr.init(sti)

    branch_name = di.branch
    async with get_translation(sti, lr, branch_name) as fs_git:
        async with MyAsyncExitStack(sti) as S:
            shelf_view: ShelfViewMaster = await S.init(ShelfViewFSMaster(fs_git, mcdp_spec_config, get_shelf_editing_status=None))

            # sti.logger.info(shelf_view=shelf_view)
            async with shelf_view.session("fsread_main_git") as session:
                check_isinstance(session, ShelfViewFSSession)
                await list_shelf_view(sti, session)
    return ExitCode.OK
