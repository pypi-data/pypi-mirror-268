import os

from zuper_commons.apps import ZArgumentParser
from zuper_commons.cmds import ExitCode
from zuper_commons.types import check_isinstance
from zuper_ide_interface import ShelfViewMaster, mcdp_spec_config
from zuper_shelf_fs import ShelfViewFSMaster, ShelfViewFSSession
from zuper_utils_asyncio import MyAsyncExitStack
from zuper_utils_fs import FSJumpManager
from zuper_zapp import ZappEnv, zapp1
from zuper_zapp_interfaces import get_fs2

from .utils import list_shelf_view

__all__ = [
    "fsread_main_fs",
]


@zapp1()
async def fsread_main_fs(ze: ZappEnv) -> ExitCode:
    sti = ze.sti
    sti.started()
    parser = ZArgumentParser()
    parser.add_argument("--dir", required=True, help="Directory on filesystem")
    parsed = parser.parse_args(args=ze.args)

    root = parsed.dir

    root = os.path.expanduser(root)
    fs20 = await get_fs2(sti)
    async with MyAsyncExitStack(sti) as S:
        fs2 = await S.init(FSJumpManager(fs20, root))
        shelf_view: ShelfViewMaster = await S.init(ShelfViewFSMaster(fs2, mcdp_spec_config, get_shelf_editing_status=None))  # XXX
        # sti.logger.info(shelf_view=shelf_view)
        async with shelf_view.session("fsread_main_fs") as session:
            check_isinstance(session, ShelfViewFSSession)
            await list_shelf_view(sti, session)
    return ExitCode.OK
