import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator, Sequence, cast

from zuper_commons.fs import DirPath
from zuper_commons.types import ZAssertionError, ZKeyError, ZNotImplementedError, add_context
from zuper_ide_interface import (
    CDEInterface,
    CDEInterfaceSession,
    CDEView,
    GenRO,
    Identities,
    ProviderName,
    ProviderView,
    ProvidersView2,
    SERVICE_CDE,
    ShelfViewMaster,
    mcdp_spec_config,
)
from zuper_ipce import IPCE
from zuper_shelf_fs import ShelfViewFSMaster
from zuper_utils_asyncio import (
    EventOrder,
    GenericWatchable,
    MyAsyncExitStack,
    NotEditable,
    OrderHelper,
    SingleView,
    SubscriberInfo,
    SyncTaskInterface,
    UpdateNoPrevious,
    WatchControl,
)
from zuper_utils_augres import (
    ImportSource,
    ImportSourceGit,
    ImportSourceLocalFS,
)
from zuper_utils_fs import FSJumpManager
from zuper_utils_git_fs import FSGitTranslationSession
from zuper_zapp_interfaces import GitEditingStatus, ServiceConfig, get_fs2

__all__ = [
    "local",
]


@asynccontextmanager
async def local(sti: SyncTaskInterface, sc: ServiceConfig) -> AsyncIterator[None]:
    _conf_string = cast(IPCE, sc.extra_config)
    # conf = object_from_ipce(conf_string, Config)

    use = CDEInterfaceLocal()
    await use.init(sti)

    try:

        async def generate(_sti_: SyncTaskInterface) -> CDEInterface:
            return use

        await sti.set_interface_gen(SERVICE_CDE, generate)

        yield
    finally:
        await use.aclose()


class ShelfViewStatusMaster:
    gw: GenericWatchable[UpdateNoPrevious[GitEditingStatus]]
    last: GitEditingStatus

    def __init__(self, last: GitEditingStatus) -> None:
        self.last = last
        self.oh = OrderHelper("ShelfViewStatusMaster")
        self.gw = GenericWatchable("ShelfViewStatusMaster", send_last_on_subscribe=True)

    async def init(self, sti: SyncTaskInterface) -> None:
        pass

    async def aclose(self) -> None:
        await self.gw.finish()

    async def update(self, status: GitEditingStatus, order: EventOrder) -> None:
        self.last = status
        order = self.oh.add_to(order)
        i = order.origins[self.oh.name]

        up = UpdateNoPrevious(i, status, order)
        await self.gw.distribute(None, up)

    def view(self, session: FSGitTranslationSession) -> "StatusView":
        return StatusView(self, session)

    def watch(self, si: SubscriberInfo[UpdateNoPrevious[GitEditingStatus]]) -> WatchControl:
        return self.gw.watch(si)


class StatusView(SingleView[GitEditingStatus]):
    def __init__(self, master: ShelfViewStatusMaster, session: "FSGitTranslationSession") -> None:
        self.master = master
        self.session = session

    def watch(self, si: SubscriberInfo[UpdateNoPrevious[GitEditingStatus]]) -> WatchControl:
        return self.master.watch(si)

    def watch_and_get_first(self, subscriber: "SubscriberInfo[UpdateNoPrevious[GitEditingStatus]]", /) -> WatchControl:
        raise ZNotImplementedError(me=self)  # FIXME: finish implement watch_and_get_first

    async def get(self, *, desc: str) -> GitEditingStatus:
        return self.master.last

    def is_editable(self) -> bool:
        return False  # OK

    async def set(self, x: GitEditingStatus, /, *, order: EventOrder) -> None:
        raise NotEditable()


class CDEInterfaceLocal(CDEInterface):
    sti: SyncTaskInterface
    S: MyAsyncExitStack

    shelf_masters: dict[DirPath, ShelfViewMaster]

    __print_order__ = ["shelf_masters"]

    def __init__(
        self,
    ) -> None:
        self.shelf_masters = {}
        self.shelf_masters_lock = asyncio.Lock()

    async def init(self, sti: SyncTaskInterface) -> None:
        self.sti = sti

        self.S = MyAsyncExitStack(sti)

    async def aclose(self) -> None:
        await self.S.aclose()

    async def get_shelf_view(self, import_source: ImportSource) -> ShelfViewMaster:
        match import_source:
            case ImportSourceGit():
                msg = "Git loading not implemented for this type of import_source"
                raise ZKeyError(msg, import_source=import_source)
                #
                # msg = "Git loading not supported"
                # raise DPNotImplementedError(msg, import_source=import_source, me=self)
                # return await self._get_version_view_git(import_source)
            case ImportSourceLocalFS():
                return await self._get_version_view_local(import_source)
            case _:
                msg = "Not implemented for this type of import_source"
                raise ZKeyError(msg, import_source=import_source)

    async def _get_version_view_local(self, import_source: ImportSourceLocalFS) -> ShelfViewMaster:
        async with self.shelf_masters_lock:
            if import_source.path not in self.shelf_masters:
                fs = await get_fs2(self.sti)
                root = import_source.path
                # TODO: check existing
                fs2 = await self.S.init(FSJumpManager(fs, root))
                shelf_view: ShelfViewMaster = await self.S.init(
                    ShelfViewFSMaster(fs2, mcdp_spec_config, get_shelf_editing_status=None)
                )  # XXX
                self.shelf_masters[import_source.path] = shelf_view

        return self.shelf_masters[import_source.path]

    # noinspection PyProtocol
    @asynccontextmanager
    async def session(self, identities: Identities, desc: str) -> "AsyncIterator[CDEInterfaceLocalSession]":
        with add_context(CDEInterfaceLocal_desc=desc):
            the_session = CDEInterfaceLocalSession(self, desc, identities)
            try:
                yield the_session
            finally:
                # raise Exception()
                # self.sti.logger.debug(f'Closing session {desc}')
                the_session.set_invalid()


class CDEInterfaceLocalSession(CDEInterfaceSession):
    cde: CDEInterfaceLocal
    identities: Identities

    __print_order__ = ["cde", "identities"]

    def __init__(self, cde: CDEInterfaceLocal, desc: str, identities: Identities) -> None:
        self.cde = cde
        self.lock = asyncio.Lock()
        self.invalid = False
        self.desc = desc
        self.identities = identities

    def set_invalid(self) -> None:
        self.invalid = True

    async def get_view(self) -> CDEView:
        if self.invalid:
            raise ZAssertionError("invalid session")
        return ProvidersViewLocal(self, self.identities)


class ProvidersViewLocal(CDEView):
    identities: Identities
    cde_session: CDEInterfaceLocalSession

    def __init__(self, cde_session: CDEInterfaceLocalSession, identities: Identities):
        self.cde_session = cde_session
        self.identities = identities

    __print_order__ = ["identities", "cde_session"]

    async def providers(self) -> GenRO[ProviderName, ProviderView]:
        return CDELocalProvidersView(self.cde_session, self.identities)

    async def get_shelf_view(self, import_source: ImportSource) -> ShelfViewMaster:
        return await self.cde_session.cde.get_shelf_view(import_source)


LOCAL_PROVIDER_NAME = cast(ProviderName, "fs")


class CDELocalProvidersView(ProvidersView2):
    cde_session: CDEInterfaceLocalSession
    identities: Identities

    __print_order__ = ["identities", "cde_session"]

    def __init__(self, cde_session: CDEInterfaceLocalSession, identities: Identities):
        self.cde_session = cde_session
        self.identities = identities

    async def exists(self, name: ProviderName) -> bool:
        return False
        # return name == LOCAL_PROVIDER_NAME

    async def get(self, name: ProviderName) -> ProviderView:
        raise KeyError(name)

        # return ProviderViewL/ocal(self, self.cde_session)

    async def lists(self) -> Sequence[ProviderName]:
        return []

    async def items(self) -> AsyncIterator[tuple[ProviderName, ProviderView]]:
        if False:
            yield ...
            # yield LOCAL_PROVIDER_NAME, await self.get(LOCAL_PROVIDER_NAME)


# class ProviderViewLocal(ProviderView):
#     cde_session: CDEInterfaceLocalSession
#     ps: CDELocalProvidersView
#
#     def __init__(self, ps: CDELocalProvidersView, cde_session: CDEInterfaceLocalSession):
#         self.ps = ps
#         self.cde_session = cde_session
#
#     async def orgs(self) -> OrgsView:
#         return ProviderViewLocalOrgs(self.cde_session, self)
#
#
# use_hostname = cast(AccountName, "localhost")
#
#
# class ProviderViewLocalOrgs(OrgsView):
#     cde_session: CDEInterfaceLocalSession
#     ps: ProviderViewLocal
#
#     def __init__(
#         self,
#         cde_session: CDEInterfaceLocalSession,
#         ps: ProviderViewLocal,
#     ):
#         self.ps = ps
#         self.cde_session = cde_session
#
#     async def exists(self, name: AccountName) -> bool:
#         return name == LOCAL_PROVIDER_NAME
#
#     async def get(self, name: AccountName) -> OrgView:
#         if name != use_hostname:
#             msg = f"Expected {use_hostname} but got {name}"
#             raise ZKeyError(msg, name=name, use_hostname=use_hostname)
#
#         return ProviderViewLocal(self, self.cde_session)
#
#     async def lists(self) -> Sequence[AccountName]:
#         return [use_hostname]
#
#     async def items(self) -> AsyncIterator[tuple[AccountName, OrgView]]:
#         yield use_hostname, await self.get(LOCAL_PROVIDER_NAME)
#
#
# class ProviderViewLocalFs(OrgView):
#     ps: ProviderViewGithubOrgsDB
#
#     def __init__(self, ps: ProviderViewGithubOrgsDB, inst_info: InstInfo2):
#         self.ps = ps
#         self.inst_info = inst_info
#
#     async def repos(self) -> ReposView:
#         return ProviderViewGithubOrgsDB_ReposView(
#             self.ps.cde_session,
#             self,
#             self.inst_info.gh_inst_id,  # self.ps.ps.github_username
#         )
#
#
# class ProviderViewGithubOrgsDB_ReposView(ReposView):
#     cde_session: CDEInterfaceDBSession
#     ps: ProviderViewGithubOrgsDB_OrgView
#
#     def __init__(
#         self,
#         cde_session: CDEInterfaceDBSession,
#         ps: ProviderViewGithubOrgsDB_OrgView,
#         gh_inst_id: GHInstID,
#     ):
#         self.cde_session = cde_session
#         self.gh_inst_id = gh_inst_id
#         self.ps = ps
#
#     def watch(self, si: SubscriberInfo[ReposViewEventPacket], /) -> WatchControl:
#         raise ZNotImplementedError(T=type(self))
#
#     async def get_list(self) -> dict[GitRepoName, RepoDetails]:
#         cde = self.cde_session.cde
#         ro = cde.repos_interface
#
#         identities = self.ps.ps.ps.ps.identities
#
#         async with ro.session(identities, "get_list") as ro:
#             rs = await ro.get_repos(self.gh_inst_id)
#
#         byname: dict[GitRepoName, RepoDetails]
#         byname = {v.repo_details.repo_name: v.repo_details for _, v in rs.repos.items()}
#
#         return byname
#
#     async def exists(self, name: GitRepoName) -> bool:
#         available = await self.get_list()
#         return name in available
#
#     async def get(self, name: GitRepoName) -> RepoView:
#         available = await self.get_list()
#         if name not in available:
#             msg = f"Could not find repo `{name}` among {list(available.keys())}"
#             raise ZKeyError(msg, identites=self.ps.ps.ps.ps.identities)
#         data = available[name]
#         return RepoViewDB(self, data.gh_repo_node_id)
#
#     async def lists(self) -> Sequence[GitRepoName]:
#         available = await self.get_list()
#
#         return list(available.keys())
#
#     async def items(self) -> AsyncIterator[tuple[GitRepoName, RepoView]]:
#         available = await self.get_list()
#         for name, _details in available.items():
#             yield name, await self.get(name)
#
#     async def create(self, name: GitRepoName, initial: InitRepoInfo, *, order: EventOrder) -> RepoView:
#         raise NotImplementedError(type(self))
#
#     async def remove(self, name: GitRepoName, *, order: EventOrder) -> None:
#         raise NotImplementedError(type(self))
#
#     async def rename(self, name: GitRepoName, name2: GitRepoName, *, order: EventOrder) -> None:
#         raise NotImplementedError(type(self))
