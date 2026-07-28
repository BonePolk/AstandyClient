import common_message_pb2 as _common_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

APPLE_ID: AuthType
BOLT_ID: AuthType
CHAT: BanScope
CLAN_CHAT: BanScope
Cyberathlete: Role
DESCRIPTOR: _descriptor.FileDescriptor
FACEBOOK: AuthType
GAME_CENTER: AuthType
GLOBAL: BanScope
GOOGLE_PLAY: AuthType
GUEST: AuthType
HUAWEI: AuthType
LOBBY_CHAT: BanScope
MARKETPLACE: BanScope
MARKETPLACE_SPECIAL: BanScope
MATCH_CHAT: BanScope
StateAway: OnlineStatus
StateBusy: OnlineStatus
StateLookingToPlay: OnlineStatus
StateLookingToTrade: OnlineStatus
StateOffline: OnlineStatus
StateOnline: OnlineStatus
StateSnooze: OnlineStatus
TEST: AuthType
TWITCH: AuthType
Tester: Role
VK: AuthType
Youtuber: Role

class Attribute(_message.Message):
    __slots__ = ["boolean", "float", "int", "string", "type"]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    boolean: bool
    float: float
    int: int
    string: str
    type: _common_message_pb2.PropertyType
    def __init__(self, type: _Optional[_Union[_common_message_pb2.PropertyType, str]] = ..., int: _Optional[int] = ..., float: _Optional[float] = ..., string: _Optional[str] = ..., boolean: bool = ...) -> None: ...

class Attributes(_message.Message):
    __slots__ = ["map"]
    class MapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Attribute
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Attribute, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, Attribute]
    def __init__(self, map: _Optional[_Mapping[str, Attribute]] = ...) -> None: ...

class BanMeRequest(_message.Message):
    __slots__ = ["code", "description"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    code: int
    description: str
    def __init__(self, code: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class BanMeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteAccountByPermissionRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteAccountByPermissionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetOnlineStatusRequest(_message.Message):
    __slots__ = ["gpid"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class GetOnlineStatusResponse(_message.Message):
    __slots__ = ["onlineStatus"]
    ONLINESTATUS_FIELD_NUMBER: _ClassVar[int]
    onlineStatus: OnlineStatus
    def __init__(self, onlineStatus: _Optional[_Union[OnlineStatus, str]] = ...) -> None: ...

class GetPlayerBanResponse(_message.Message):
    __slots__ = ["bans", "gpid"]
    BANS_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    bans: _containers.RepeatedCompositeFieldContainer[PlayerBan]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ..., bans: _Optional[_Iterable[_Union[PlayerBan, _Mapping]]] = ...) -> None: ...

class GetPlayerByIdRequest(_message.Message):
    __slots__ = ["gpid"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class GetPlayerByIdResponse(_message.Message):
    __slots__ = ["player"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    player: Player
    def __init__(self, player: _Optional[_Union[Player, _Mapping]] = ...) -> None: ...

class GetPlayerByUidRequest(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class GetPlayerByUidResponse(_message.Message):
    __slots__ = ["player"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    player: Player
    def __init__(self, player: _Optional[_Union[Player, _Mapping]] = ...) -> None: ...

class GetPlayerRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerResponse(_message.Message):
    __slots__ = ["email", "intercomHMAC", "permissions", "player", "uuid"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    INTERCOMHMAC_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    email: str
    intercomHMAC: str
    permissions: _containers.RepeatedScalarFieldContainer[int]
    player: Player
    uuid: str
    def __init__(self, player: _Optional[_Union[Player, _Mapping]] = ..., permissions: _Optional[_Iterable[int]] = ..., uuid: _Optional[str] = ..., intercomHMAC: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class GetPlayerSettingsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerSettingsResponse(_message.Message):
    __slots__ = ["settings"]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: PlayerSettings
    def __init__(self, settings: _Optional[_Union[PlayerSettings, _Mapping]] = ...) -> None: ...

class GetPlayersBansRequest(_message.Message):
    __slots__ = ["gpid"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gpid: _Optional[_Iterable[str]] = ...) -> None: ...

class GetPlayersBansResponse(_message.Message):
    __slots__ = ["playerResponses"]
    PLAYERRESPONSES_FIELD_NUMBER: _ClassVar[int]
    playerResponses: _containers.RepeatedCompositeFieldContainer[GetPlayerBanResponse]
    def __init__(self, playerResponses: _Optional[_Iterable[_Union[GetPlayerBanResponse, _Mapping]]] = ...) -> None: ...

class OnDeviceBanned(_message.Message):
    __slots__ = ["deviceId"]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    deviceId: str
    def __init__(self, deviceId: _Optional[str] = ...) -> None: ...

class OnGameDeactivated(_message.Message):
    __slots__ = ["gameId"]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    gameId: int
    def __init__(self, gameId: _Optional[int] = ...) -> None: ...

class OnPlayerAttributesChanged(_message.Message):
    __slots__ = ["attributes", "deleted", "gpid"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    attributes: Attributes
    deleted: _containers.RepeatedScalarFieldContainer[str]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ..., attributes: _Optional[_Union[Attributes, _Mapping]] = ..., deleted: _Optional[_Iterable[str]] = ...) -> None: ...

class OnPlayerBanned(_message.Message):
    __slots__ = ["banCode", "banScope", "message", "until"]
    BANCODE_FIELD_NUMBER: _ClassVar[int]
    BANSCOPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    banCode: int
    banScope: BanScope
    message: str
    until: int
    def __init__(self, banCode: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ..., banScope: _Optional[_Union[BanScope, str]] = ...) -> None: ...

class OnPlayerKicked(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class PlayInGame(_message.Message):
    __slots__ = ["gameCode", "gameVersion", "lobbyId", "lobbyName", "photonGame"]
    GAMECODE_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    LOBBYNAME_FIELD_NUMBER: _ClassVar[int]
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    gameCode: str
    gameVersion: str
    lobbyId: str
    lobbyName: str
    photonGame: _common_message_pb2.PhotonGame
    def __init__(self, gameCode: _Optional[str] = ..., gameVersion: _Optional[str] = ..., lobbyId: _Optional[str] = ..., photonGame: _Optional[_Union[_common_message_pb2.PhotonGame, _Mapping]] = ..., lobbyName: _Optional[str] = ...) -> None: ...

class Player(_message.Message):
    __slots__ = ["attributes", "avatarId", "bans", "deleted", "gpid", "guest", "logoutDate", "name", "playerStatus", "registrationDate", "tags", "testerRole", "timeInGame", "uid"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    BANS_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    GUEST_FIELD_NUMBER: _ClassVar[int]
    LOGOUTDATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYERSTATUS_FIELD_NUMBER: _ClassVar[int]
    REGISTRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TESTERROLE_FIELD_NUMBER: _ClassVar[int]
    TIMEINGAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    attributes: Attributes
    avatarId: str
    bans: _containers.RepeatedCompositeFieldContainer[PlayerBan]
    deleted: bool
    gpid: str
    guest: bool
    logoutDate: int
    name: str
    playerStatus: PlayerStatus
    registrationDate: int
    tags: _containers.RepeatedScalarFieldContainer[int]
    testerRole: str
    timeInGame: int
    uid: str
    def __init__(self, gpid: _Optional[str] = ..., uid: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., timeInGame: _Optional[int] = ..., playerStatus: _Optional[_Union[PlayerStatus, _Mapping]] = ..., logoutDate: _Optional[int] = ..., registrationDate: _Optional[int] = ..., attributes: _Optional[_Union[Attributes, _Mapping]] = ..., testerRole: _Optional[str] = ..., bans: _Optional[_Iterable[_Union[PlayerBan, _Mapping]]] = ..., deleted: bool = ..., tags: _Optional[_Iterable[int]] = ..., guest: bool = ...) -> None: ...

class PlayerBan(_message.Message):
    __slots__ = ["banCode", "banScope", "message", "until"]
    BANCODE_FIELD_NUMBER: _ClassVar[int]
    BANSCOPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    banCode: int
    banScope: BanScope
    message: str
    until: int
    def __init__(self, banCode: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ..., banScope: _Optional[_Union[BanScope, str]] = ...) -> None: ...

class PlayerSettings(_message.Message):
    __slots__ = ["settings"]
    class SettingsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.ScalarMap[str, str]
    def __init__(self, settings: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PlayerStatus(_message.Message):
    __slots__ = ["gpid", "onlineStatus", "playInGame"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    ONLINESTATUS_FIELD_NUMBER: _ClassVar[int]
    PLAYINGAME_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    onlineStatus: OnlineStatus
    playInGame: PlayInGame
    def __init__(self, gpid: _Optional[str] = ..., playInGame: _Optional[_Union[PlayInGame, _Mapping]] = ..., onlineStatus: _Optional[_Union[OnlineStatus, str]] = ...) -> None: ...

class SetAndGetPlayerNameRequest(_message.Message):
    __slots__ = ["newName"]
    NEWNAME_FIELD_NUMBER: _ClassVar[int]
    newName: str
    def __init__(self, newName: _Optional[str] = ...) -> None: ...

class SetAndGetPlayerNameResponse(_message.Message):
    __slots__ = ["newName"]
    NEWNAME_FIELD_NUMBER: _ClassVar[int]
    newName: str
    def __init__(self, newName: _Optional[str] = ...) -> None: ...

class SetAwayStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetAwayStatusResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetDefaultAvatarRequest(_message.Message):
    __slots__ = ["avatarId"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    def __init__(self, avatarId: _Optional[str] = ...) -> None: ...

class SetDefaultAvatarResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetOnlineStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetOnlineStatusResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetPlayerAttributesRequest(_message.Message):
    __slots__ = ["attributes"]
    class AttributeSetter(_message.Message):
        __slots__ = ["boolean", "float", "int", "string"]
        BOOLEAN_FIELD_NUMBER: _ClassVar[int]
        FLOAT_FIELD_NUMBER: _ClassVar[int]
        INT_FIELD_NUMBER: _ClassVar[int]
        STRING_FIELD_NUMBER: _ClassVar[int]
        boolean: bool
        float: float
        int: int
        string: str
        def __init__(self, int: _Optional[int] = ..., float: _Optional[float] = ..., string: _Optional[str] = ..., boolean: bool = ...) -> None: ...
    class AttributeSetters(_message.Message):
        __slots__ = ["setters"]
        class SettersEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: SetPlayerAttributesRequest.AttributeSetter
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SetPlayerAttributesRequest.AttributeSetter, _Mapping]] = ...) -> None: ...
        SETTERS_FIELD_NUMBER: _ClassVar[int]
        setters: _containers.MessageMap[str, SetPlayerAttributesRequest.AttributeSetter]
        def __init__(self, setters: _Optional[_Mapping[str, SetPlayerAttributesRequest.AttributeSetter]] = ...) -> None: ...
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SetPlayerAttributesRequest.AttributeSetters
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SetPlayerAttributesRequest.AttributeSetters, _Mapping]] = ...) -> None: ...
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.MessageMap[str, SetPlayerAttributesRequest.AttributeSetters]
    def __init__(self, attributes: _Optional[_Mapping[str, SetPlayerAttributesRequest.AttributeSetters]] = ...) -> None: ...

class SetPlayerAttributesResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetPlayerAvatarRequest(_message.Message):
    __slots__ = ["avatar"]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    avatar: bytes
    def __init__(self, avatar: _Optional[bytes] = ...) -> None: ...

class SetPlayerAvatarResponse(_message.Message):
    __slots__ = ["avatarId"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    def __init__(self, avatarId: _Optional[str] = ...) -> None: ...

class SetPlayerFirebaseTokenRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class SetPlayerFirebaseTokenResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetPlayerNameRequest(_message.Message):
    __slots__ = ["newName"]
    NEWNAME_FIELD_NUMBER: _ClassVar[int]
    newName: str
    def __init__(self, newName: _Optional[str] = ...) -> None: ...

class SetPlayerNameResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetPlayerSettingsRequest(_message.Message):
    __slots__ = ["settings"]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: PlayerSettings
    def __init__(self, settings: _Optional[_Union[PlayerSettings, _Mapping]] = ...) -> None: ...

class SetPlayerSettingsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class OnlineStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class BanScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
