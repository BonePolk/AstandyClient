import common_message_pb2 as _common_message_pb2
import player_message_pb2 as _player_message_pb2
import friends_message_pb2 as _friends_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ANY: LobbyPlayerType
CLOSE: LobbyDistanceFilter
DEFAULT: LobbyDistanceFilter
DESCRIPTOR: _descriptor.FileDescriptor
FAR: LobbyDistanceFilter
FRIENDS_ONLY: LobbyType
INVISIBLE: LobbyType
MEMBER: LobbyPlayerType
PRIVATE: LobbyType
PUBLIC: LobbyType
SPECTATOR: LobbyPlayerType
WORLDWIDE: LobbyDistanceFilter

class ChangeLobbyOtherPlayerTypeRequest(_message.Message):
    __slots__ = ["gpid", "playerType"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    playerType: LobbyPlayerType
    def __init__(self, gpid: _Optional[str] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ...) -> None: ...

class ChangeLobbyOtherPlayerTypeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ChangeLobbyPlayerTypeRequest(_message.Message):
    __slots__ = ["playerType"]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    playerType: LobbyPlayerType
    def __init__(self, playerType: _Optional[_Union[LobbyPlayerType, str]] = ...) -> None: ...

class ChangeLobbyPlayerTypeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateLobbyWithSpectatorsRequest(_message.Message):
    __slots__ = ["data", "dataVisibleInSearch", "lobbyType", "maxMembers", "maxSpectators", "name"]
    DATAVISIBLEINSEARCH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOBBYTYPE_FIELD_NUMBER: _ClassVar[int]
    MAXMEMBERS_FIELD_NUMBER: _ClassVar[int]
    MAXSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    data: _common_message_pb2.Dictionary
    dataVisibleInSearch: _containers.RepeatedScalarFieldContainer[str]
    lobbyType: LobbyType
    maxMembers: int
    maxSpectators: int
    name: str
    def __init__(self, name: _Optional[str] = ..., lobbyType: _Optional[_Union[LobbyType, str]] = ..., maxMembers: _Optional[int] = ..., maxSpectators: _Optional[int] = ..., dataVisibleInSearch: _Optional[_Iterable[str]] = ..., data: _Optional[_Union[_common_message_pb2.Dictionary, _Mapping]] = ...) -> None: ...

class CreateLobbyWithSpectatorsResponse(_message.Message):
    __slots__ = ["lobby"]
    LOBBY_FIELD_NUMBER: _ClassVar[int]
    lobby: Lobby
    def __init__(self, lobby: _Optional[_Union[Lobby, _Mapping]] = ...) -> None: ...

class DeleteLobbyDataRequest(_message.Message):
    __slots__ = ["keys"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteLobbyDataResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GameServerDetails(_message.Message):
    __slots__ = ["botPlayers", "currentPlayers", "doNotRefresh", "gameServer", "id", "map", "maxPlayers", "requirePassword", "successfulResponse", "version"]
    BOTPLAYERS_FIELD_NUMBER: _ClassVar[int]
    CURRENTPLAYERS_FIELD_NUMBER: _ClassVar[int]
    DONOTREFRESH_FIELD_NUMBER: _ClassVar[int]
    GAMESERVER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    MAXPLAYERS_FIELD_NUMBER: _ClassVar[int]
    REQUIREPASSWORD_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFULRESPONSE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    botPlayers: int
    currentPlayers: int
    doNotRefresh: bool
    gameServer: _common_message_pb2.GameServer
    id: str
    map: str
    maxPlayers: int
    requirePassword: bool
    successfulResponse: bool
    version: str
    def __init__(self, id: _Optional[str] = ..., gameServer: _Optional[_Union[_common_message_pb2.GameServer, _Mapping]] = ..., map: _Optional[str] = ..., currentPlayers: _Optional[int] = ..., maxPlayers: _Optional[int] = ..., botPlayers: _Optional[int] = ..., requirePassword: bool = ..., version: _Optional[str] = ..., successfulResponse: bool = ..., doNotRefresh: bool = ...) -> None: ...

class GetGameServerDetailsRequest(_message.Message):
    __slots__ = ["gameServerId"]
    GAMESERVERID_FIELD_NUMBER: _ClassVar[int]
    gameServerId: str
    def __init__(self, gameServerId: _Optional[str] = ...) -> None: ...

class GetGameServerDetailsResponse(_message.Message):
    __slots__ = ["gameServerDetails"]
    GAMESERVERDETAILS_FIELD_NUMBER: _ClassVar[int]
    gameServerDetails: GameServerDetails
    def __init__(self, gameServerDetails: _Optional[_Union[GameServerDetails, _Mapping]] = ...) -> None: ...

class GetGameServerPlayersRequest(_message.Message):
    __slots__ = ["gameServerId"]
    GAMESERVERID_FIELD_NUMBER: _ClassVar[int]
    gameServerId: str
    def __init__(self, gameServerId: _Optional[str] = ...) -> None: ...

class GetGameServerPlayersResponse(_message.Message):
    __slots__ = ["players"]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[_player_message_pb2.Player]
    def __init__(self, players: _Optional[_Iterable[_Union[_player_message_pb2.Player, _Mapping]]] = ...) -> None: ...

class GetInvitesToLobbyRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInvitesToLobbyResponse(_message.Message):
    __slots__ = ["lobbyInvites"]
    LOBBYINVITES_FIELD_NUMBER: _ClassVar[int]
    lobbyInvites: _containers.RepeatedCompositeFieldContainer[LobbyInvite]
    def __init__(self, lobbyInvites: _Optional[_Iterable[_Union[LobbyInvite, _Mapping]]] = ...) -> None: ...

class GetLobbyGameServerRequest(_message.Message):
    __slots__ = ["lobbyId"]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    def __init__(self, lobbyId: _Optional[str] = ...) -> None: ...

class GetLobbyGameServerResponse(_message.Message):
    __slots__ = ["gameServerDetails"]
    GAMESERVERDETAILS_FIELD_NUMBER: _ClassVar[int]
    gameServerDetails: GameServerDetails
    def __init__(self, gameServerDetails: _Optional[_Union[GameServerDetails, _Mapping]] = ...) -> None: ...

class GetLobbyMembersRequest(_message.Message):
    __slots__ = ["lobbyId"]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    def __init__(self, lobbyId: _Optional[str] = ...) -> None: ...

class GetLobbyMembersResponse(_message.Message):
    __slots__ = ["players"]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[_player_message_pb2.Player]
    def __init__(self, players: _Optional[_Iterable[_Union[_player_message_pb2.Player, _Mapping]]] = ...) -> None: ...

class GetLobbyOwnerRequest(_message.Message):
    __slots__ = ["lobbyId"]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    def __init__(self, lobbyId: _Optional[str] = ...) -> None: ...

class GetLobbyOwnerResponse(_message.Message):
    __slots__ = ["owner"]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    owner: _player_message_pb2.Player
    def __init__(self, owner: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ...) -> None: ...

class GetLobbyPhotonGameRequest(_message.Message):
    __slots__ = ["lobbyId"]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    def __init__(self, lobbyId: _Optional[str] = ...) -> None: ...

class GetLobbyPhotonGameResponse(_message.Message):
    __slots__ = ["photonGame"]
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    photonGame: _common_message_pb2.PhotonGame
    def __init__(self, photonGame: _Optional[_Union[_common_message_pb2.PhotonGame, _Mapping]] = ...) -> None: ...

class GetLobbyRequest(_message.Message):
    __slots__ = ["lobbyId"]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    def __init__(self, lobbyId: _Optional[str] = ...) -> None: ...

class GetLobbyResponse(_message.Message):
    __slots__ = ["lobby"]
    LOBBY_FIELD_NUMBER: _ClassVar[int]
    lobby: Lobby
    def __init__(self, lobby: _Optional[_Union[Lobby, _Mapping]] = ...) -> None: ...

class InvitePlayerToLobbyAsRequest(_message.Message):
    __slots__ = ["invitedGpid", "playerType"]
    INVITEDGPID_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    invitedGpid: str
    playerType: LobbyPlayerType
    def __init__(self, invitedGpid: _Optional[str] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ...) -> None: ...

class InvitePlayerToLobbyAsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InvitePlayerToLobbyRequest(_message.Message):
    __slots__ = ["invitedGpid"]
    INVITEDGPID_FIELD_NUMBER: _ClassVar[int]
    invitedGpid: str
    def __init__(self, invitedGpid: _Optional[str] = ...) -> None: ...

class InvitePlayerToLobbyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class JoinLobbyAsRequest(_message.Message):
    __slots__ = ["lobbyId", "playerType", "token"]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    playerType: LobbyPlayerType
    token: str
    def __init__(self, lobbyId: _Optional[str] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ..., token: _Optional[str] = ...) -> None: ...

class JoinLobbyAsResponse(_message.Message):
    __slots__ = ["lobby"]
    LOBBY_FIELD_NUMBER: _ClassVar[int]
    lobby: Lobby
    def __init__(self, lobby: _Optional[_Union[Lobby, _Mapping]] = ...) -> None: ...

class JoinLobbyRequest(_message.Message):
    __slots__ = ["lobbyId"]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    def __init__(self, lobbyId: _Optional[str] = ...) -> None: ...

class JoinLobbyResponse(_message.Message):
    __slots__ = ["lobby"]
    LOBBY_FIELD_NUMBER: _ClassVar[int]
    lobby: Lobby
    def __init__(self, lobby: _Optional[_Union[Lobby, _Mapping]] = ...) -> None: ...

class KickPlayerFromLobbyRequest(_message.Message):
    __slots__ = ["kickedGpid"]
    KICKEDGPID_FIELD_NUMBER: _ClassVar[int]
    kickedGpid: str
    def __init__(self, kickedGpid: _Optional[str] = ...) -> None: ...

class KickPlayerFromLobbyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LeaveLobbyRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LeaveLobbyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Lobby(_message.Message):
    __slots__ = ["data", "gameServer", "id", "invites", "joinable", "lobbyType", "maxMembers", "maxSpectators", "members", "name", "numberOfMembers", "numberOfSpectators", "ownerGpid", "photonGame", "spectatorInvites", "spectators", "token"]
    class DataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    GAMESERVER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INVITES_FIELD_NUMBER: _ClassVar[int]
    JOINABLE_FIELD_NUMBER: _ClassVar[int]
    LOBBYTYPE_FIELD_NUMBER: _ClassVar[int]
    MAXMEMBERS_FIELD_NUMBER: _ClassVar[int]
    MAXSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFMEMBERS_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    OWNERGPID_FIELD_NUMBER: _ClassVar[int]
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    SPECTATORINVITES_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    data: _containers.ScalarMap[str, str]
    gameServer: _common_message_pb2.GameServer
    id: str
    invites: _containers.RepeatedCompositeFieldContainer[_friends_message_pb2.PlayerFriend]
    joinable: bool
    lobbyType: LobbyType
    maxMembers: int
    maxSpectators: int
    members: _containers.RepeatedCompositeFieldContainer[_friends_message_pb2.PlayerFriend]
    name: str
    numberOfMembers: int
    numberOfSpectators: int
    ownerGpid: str
    photonGame: _common_message_pb2.PhotonGame
    spectatorInvites: _containers.RepeatedCompositeFieldContainer[_friends_message_pb2.PlayerFriend]
    spectators: _containers.RepeatedCompositeFieldContainer[_friends_message_pb2.PlayerFriend]
    token: str
    def __init__(self, id: _Optional[str] = ..., ownerGpid: _Optional[str] = ..., name: _Optional[str] = ..., lobbyType: _Optional[_Union[LobbyType, str]] = ..., joinable: bool = ..., maxMembers: _Optional[int] = ..., data: _Optional[_Mapping[str, str]] = ..., members: _Optional[_Iterable[_Union[_friends_message_pb2.PlayerFriend, _Mapping]]] = ..., invites: _Optional[_Iterable[_Union[_friends_message_pb2.PlayerFriend, _Mapping]]] = ..., gameServer: _Optional[_Union[_common_message_pb2.GameServer, _Mapping]] = ..., photonGame: _Optional[_Union[_common_message_pb2.PhotonGame, _Mapping]] = ..., maxSpectators: _Optional[int] = ..., spectators: _Optional[_Iterable[_Union[_friends_message_pb2.PlayerFriend, _Mapping]]] = ..., spectatorInvites: _Optional[_Iterable[_Union[_friends_message_pb2.PlayerFriend, _Mapping]]] = ..., numberOfMembers: _Optional[int] = ..., numberOfSpectators: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class LobbyInvite(_message.Message):
    __slots__ = ["date", "inviteSender", "lobbyId", "lobbyName", "playerType"]
    DATE_FIELD_NUMBER: _ClassVar[int]
    INVITESENDER_FIELD_NUMBER: _ClassVar[int]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    LOBBYNAME_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    date: int
    inviteSender: _friends_message_pb2.PlayerFriend
    lobbyId: str
    lobbyName: str
    playerType: LobbyPlayerType
    def __init__(self, lobbyId: _Optional[str] = ..., inviteSender: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ..., date: _Optional[int] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ..., lobbyName: _Optional[str] = ...) -> None: ...

class OnLobbyChatMessageEvent(_message.Message):
    __slots__ = ["gpid", "message"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    message: str
    def __init__(self, gpid: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class OnLobbyDataChangedEvent(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _common_message_pb2.Dictionary
    def __init__(self, data: _Optional[_Union[_common_message_pb2.Dictionary, _Mapping]] = ...) -> None: ...

class OnLobbyGameServerChangedEvent(_message.Message):
    __slots__ = ["gameServer"]
    GAMESERVER_FIELD_NUMBER: _ClassVar[int]
    gameServer: _common_message_pb2.GameServer
    def __init__(self, gameServer: _Optional[_Union[_common_message_pb2.GameServer, _Mapping]] = ...) -> None: ...

class OnLobbyJoinableChangedEvent(_message.Message):
    __slots__ = ["joinable"]
    JOINABLE_FIELD_NUMBER: _ClassVar[int]
    joinable: bool
    def __init__(self, joinable: bool = ...) -> None: ...

class OnLobbyMaxMembersChangedEvent(_message.Message):
    __slots__ = ["maxMembers"]
    MAXMEMBERS_FIELD_NUMBER: _ClassVar[int]
    maxMembers: int
    def __init__(self, maxMembers: _Optional[int] = ...) -> None: ...

class OnLobbyMaxSpectatorsChangedEvent(_message.Message):
    __slots__ = ["maxSpectators"]
    MAXSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    maxSpectators: int
    def __init__(self, maxSpectators: _Optional[int] = ...) -> None: ...

class OnLobbyNameChangedEvent(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class OnLobbyOwnerChangedEvent(_message.Message):
    __slots__ = ["lobbyOwnerGpid"]
    LOBBYOWNERGPID_FIELD_NUMBER: _ClassVar[int]
    lobbyOwnerGpid: str
    def __init__(self, lobbyOwnerGpid: _Optional[str] = ...) -> None: ...

class OnLobbyPhotonGameChangedEvent(_message.Message):
    __slots__ = ["photonGame"]
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    photonGame: _common_message_pb2.PhotonGame
    def __init__(self, photonGame: _Optional[_Union[_common_message_pb2.PhotonGame, _Mapping]] = ...) -> None: ...

class OnLobbyPlayerTypeChangedEvent(_message.Message):
    __slots__ = ["gpid", "playerType"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    playerType: LobbyPlayerType
    def __init__(self, gpid: _Optional[str] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ...) -> None: ...

class OnLobbyTypeChangedEvent(_message.Message):
    __slots__ = ["lobbyType"]
    LOBBYTYPE_FIELD_NUMBER: _ClassVar[int]
    lobbyType: LobbyType
    def __init__(self, lobbyType: _Optional[_Union[LobbyType, str]] = ...) -> None: ...

class OnNewPlayerInvitedToLobbyEvent(_message.Message):
    __slots__ = ["inviteSenderGpid", "newPlayer"]
    INVITESENDERGPID_FIELD_NUMBER: _ClassVar[int]
    NEWPLAYER_FIELD_NUMBER: _ClassVar[int]
    inviteSenderGpid: str
    newPlayer: _friends_message_pb2.PlayerFriend
    def __init__(self, inviteSenderGpid: _Optional[str] = ..., newPlayer: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ...) -> None: ...

class OnNewPlayerJoinedLobbyEvent(_message.Message):
    __slots__ = ["newPlayer"]
    NEWPLAYER_FIELD_NUMBER: _ClassVar[int]
    newPlayer: _friends_message_pb2.PlayerFriend
    def __init__(self, newPlayer: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ...) -> None: ...

class OnNewSpectatorInvitedToLobbyEvent(_message.Message):
    __slots__ = ["inviteSenderGpid", "newSpectator"]
    INVITESENDERGPID_FIELD_NUMBER: _ClassVar[int]
    NEWSPECTATOR_FIELD_NUMBER: _ClassVar[int]
    inviteSenderGpid: str
    newSpectator: _friends_message_pb2.PlayerFriend
    def __init__(self, inviteSenderGpid: _Optional[str] = ..., newSpectator: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ...) -> None: ...

class OnNewSpectatorJoinedLobbyEvent(_message.Message):
    __slots__ = ["newSpectator"]
    NEWSPECTATOR_FIELD_NUMBER: _ClassVar[int]
    newSpectator: _friends_message_pb2.PlayerFriend
    def __init__(self, newSpectator: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ...) -> None: ...

class OnPlayerKickedFromLobbyEvent(_message.Message):
    __slots__ = ["kickInitiatorGpid", "kickedGpid"]
    KICKEDGPID_FIELD_NUMBER: _ClassVar[int]
    KICKINITIATORGPID_FIELD_NUMBER: _ClassVar[int]
    kickInitiatorGpid: str
    kickedGpid: str
    def __init__(self, kickInitiatorGpid: _Optional[str] = ..., kickedGpid: _Optional[str] = ...) -> None: ...

class OnPlayerLeftLobbyEvent(_message.Message):
    __slots__ = ["leftGpid"]
    LEFTGPID_FIELD_NUMBER: _ClassVar[int]
    leftGpid: str
    def __init__(self, leftGpid: _Optional[str] = ...) -> None: ...

class OnReceivedInviteToLobbyEvent(_message.Message):
    __slots__ = ["invite"]
    INVITE_FIELD_NUMBER: _ClassVar[int]
    invite: LobbyInvite
    def __init__(self, invite: _Optional[_Union[LobbyInvite, _Mapping]] = ...) -> None: ...

class OnReceivedSpectatorInviteToLobbyEvent(_message.Message):
    __slots__ = ["invite"]
    INVITE_FIELD_NUMBER: _ClassVar[int]
    invite: LobbyInvite
    def __init__(self, invite: _Optional[_Union[LobbyInvite, _Mapping]] = ...) -> None: ...

class OnRefuseInviteToLobbyEvent(_message.Message):
    __slots__ = ["inviteSenderGpid", "invitedGpid"]
    INVITEDGPID_FIELD_NUMBER: _ClassVar[int]
    INVITESENDERGPID_FIELD_NUMBER: _ClassVar[int]
    inviteSenderGpid: str
    invitedGpid: str
    def __init__(self, inviteSenderGpid: _Optional[str] = ..., invitedGpid: _Optional[str] = ...) -> None: ...

class OnRevokeInviteToLobbyEvent(_message.Message):
    __slots__ = ["inviteSenderGpid", "invitedGpid"]
    INVITEDGPID_FIELD_NUMBER: _ClassVar[int]
    INVITESENDERGPID_FIELD_NUMBER: _ClassVar[int]
    inviteSenderGpid: str
    invitedGpid: str
    def __init__(self, inviteSenderGpid: _Optional[str] = ..., invitedGpid: _Optional[str] = ...) -> None: ...

class RefuseInvitationToLobbyRequest(_message.Message):
    __slots__ = ["lobbyId"]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    def __init__(self, lobbyId: _Optional[str] = ...) -> None: ...

class RefuseInvitationToLobbyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RequestInternetServerListRequest(_message.Message):
    __slots__ = ["freePlayerSlots", "map", "maxPlayers", "withPassword"]
    FREEPLAYERSLOTS_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    MAXPLAYERS_FIELD_NUMBER: _ClassVar[int]
    WITHPASSWORD_FIELD_NUMBER: _ClassVar[int]
    freePlayerSlots: int
    map: str
    maxPlayers: int
    withPassword: bool
    def __init__(self, map: _Optional[str] = ..., freePlayerSlots: _Optional[int] = ..., maxPlayers: _Optional[int] = ..., withPassword: bool = ...) -> None: ...

class RequestInternetServerListResponse(_message.Message):
    __slots__ = ["gameServers"]
    GAMESERVERS_FIELD_NUMBER: _ClassVar[int]
    gameServers: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.GameServer]
    def __init__(self, gameServers: _Optional[_Iterable[_Union[_common_message_pb2.GameServer, _Mapping]]] = ...) -> None: ...

class RequestLobbyListRequest(_message.Message):
    __slots__ = ["distanceFilter", "filters"]
    DISTANCEFILTER_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    distanceFilter: LobbyDistanceFilter
    filters: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Filter]
    def __init__(self, distanceFilter: _Optional[_Union[LobbyDistanceFilter, str]] = ..., filters: _Optional[_Iterable[_Union[_common_message_pb2.Filter, _Mapping]]] = ...) -> None: ...

class RequestLobbyListResponse(_message.Message):
    __slots__ = ["lobbies"]
    LOBBIES_FIELD_NUMBER: _ClassVar[int]
    lobbies: _containers.RepeatedCompositeFieldContainer[Lobby]
    def __init__(self, lobbies: _Optional[_Iterable[_Union[Lobby, _Mapping]]] = ...) -> None: ...

class RevokePlayerInvitationToLobbyRequest(_message.Message):
    __slots__ = ["revokedGpid"]
    REVOKEDGPID_FIELD_NUMBER: _ClassVar[int]
    revokedGpid: str
    def __init__(self, revokedGpid: _Optional[str] = ...) -> None: ...

class RevokePlayerInvitationToLobbyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SearchLobbyRequest(_message.Message):
    __slots__ = ["amount", "filters", "version"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    amount: int
    filters: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Filter]
    version: int
    def __init__(self, amount: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[_common_message_pb2.Filter, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class SearchLobbyResponse(_message.Message):
    __slots__ = ["lobbies"]
    LOBBIES_FIELD_NUMBER: _ClassVar[int]
    lobbies: _containers.RepeatedCompositeFieldContainer[Lobby]
    def __init__(self, lobbies: _Optional[_Iterable[_Union[Lobby, _Mapping]]] = ...) -> None: ...

class SendLobbyChatMsgRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SendLobbyChatMsgResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetLobbyDataRequest(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _common_message_pb2.Dictionary
    def __init__(self, data: _Optional[_Union[_common_message_pb2.Dictionary, _Mapping]] = ...) -> None: ...

class SetLobbyDataResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetLobbyGameServerRequest(_message.Message):
    __slots__ = ["gameServerId"]
    GAMESERVERID_FIELD_NUMBER: _ClassVar[int]
    gameServerId: str
    def __init__(self, gameServerId: _Optional[str] = ...) -> None: ...

class SetLobbyGameServerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetLobbyJoinableRequest(_message.Message):
    __slots__ = ["joinable"]
    JOINABLE_FIELD_NUMBER: _ClassVar[int]
    joinable: bool
    def __init__(self, joinable: bool = ...) -> None: ...

class SetLobbyJoinableResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetLobbyMaxMembersRequest(_message.Message):
    __slots__ = ["maxMembers"]
    MAXMEMBERS_FIELD_NUMBER: _ClassVar[int]
    maxMembers: int
    def __init__(self, maxMembers: _Optional[int] = ...) -> None: ...

class SetLobbyMaxMembersResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetLobbyMaxSpectatorsRequest(_message.Message):
    __slots__ = ["maxSpectators"]
    MAXSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    maxSpectators: int
    def __init__(self, maxSpectators: _Optional[int] = ...) -> None: ...

class SetLobbyMaxSpectatorsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetLobbyNameRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SetLobbyNameResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetLobbyOwnerRequest(_message.Message):
    __slots__ = ["gpid"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class SetLobbyOwnerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetLobbyPhotonGameRequest(_message.Message):
    __slots__ = ["photonGame"]
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    photonGame: _common_message_pb2.PhotonGame
    def __init__(self, photonGame: _Optional[_Union[_common_message_pb2.PhotonGame, _Mapping]] = ...) -> None: ...

class SetLobbyPhotonGameResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetLobbyTypeRequest(_message.Message):
    __slots__ = ["lobbyType"]
    LOBBYTYPE_FIELD_NUMBER: _ClassVar[int]
    lobbyType: LobbyType
    def __init__(self, lobbyType: _Optional[_Union[LobbyType, str]] = ...) -> None: ...

class SetLobbyTypeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LobbyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class LobbyPlayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class LobbyDistanceFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
