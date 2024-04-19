from typing import Optional

from zuper_commons.types import check_isinstance
from zuper_ide_interface import ShelfViewSession
from zuper_shelf_fs import ShelfViewFSSession
from zuper_utils_asyncio import SyncTaskInterface


async def list_shelf_view(sti: SyncTaskInterface, shelf_view: ShelfViewSession) -> None:
    logger = sti.logger
    desc = "list_shelf_view"
    check_isinstance(shelf_view, ShelfViewFSSession)
    libraries = await shelf_view.libraries()
    libraries_list = await libraries.lists()
    sti.logger.info(libraries=libraries_list)
    for l in libraries_list:
        lib = await libraries.get(l)
        specs = await lib.specs()
        for s in await specs.lists():
            things = await specs.get(s)
            nthings = list(await things.lists())
            logger.info(f"library {l} spec {s} nthings {nthings}")
            async for t, thing in things.items():
                async for k, v in thing.items():
                    data: Optional[bytes] = await v.get(desc=desc)
                    if data is None:
                        data = b""

                    logger.info(f"{l}/{s}/{t}:{k}  {len(data)} {type(data)}")
