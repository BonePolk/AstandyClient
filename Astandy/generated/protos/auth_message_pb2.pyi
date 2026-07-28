import common_message_pb2 as _common_message_pb2
import player_message_pb2 as _player_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppVerification(_message.Message):
    __slots__ = ["apkHash", "appSnapshot", "contentHash", "e", "environment", "isRooted", "jsonForbiddenApps", "n", "path", "token"]
    class AppSnapshotEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APKHASH_FIELD_NUMBER: _ClassVar[int]
    APPSNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    CONTENTHASH_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    E_FIELD_NUMBER: _ClassVar[int]
    ISROOTED_FIELD_NUMBER: _ClassVar[int]
    JSONFORBIDDENAPPS_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    apkHash: str
    appSnapshot: _containers.ScalarMap[str, str]
    contentHash: str
    e: bytes
    environment: _common_message_pb2.EnvironmentInfo
    isRooted: bool
    jsonForbiddenApps: _containers.RepeatedScalarFieldContainer[str]
    n: bytes
    path: str
    token: str
    def __init__(self, isRooted: bool = ..., apkHash: _Optional[str] = ..., jsonForbiddenApps: _Optional[_Iterable[str]] = ..., path: _Optional[str] = ..., contentHash: _Optional[str] = ..., appSnapshot: _Optional[_Mapping[str, str]] = ..., n: _Optional[bytes] = ..., e: _Optional[bytes] = ..., environment: _Optional[_Union[_common_message_pb2.EnvironmentInfo, _Mapping]] = ..., token: _Optional[str] = ...) -> None: ...

class AppleIdAuthRequest(_message.Message):
    __slots__ = ["appVerification", "authAppleId", "deviceInfo"]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    AUTHAPPLEID_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    appVerification: AppVerification
    authAppleId: AuthAppleId
    deviceInfo: DeviceInfo
    def __init__(self, authAppleId: _Optional[_Union[AuthAppleId, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class AppleIdAuthResponse(_message.Message):
    __slots__ = ["playerTicket", "ticket", "ticketBinary"]
    PLAYERTICKET_FIELD_NUMBER: _ClassVar[int]
    TICKETBINARY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    playerTicket: str
    ticket: str
    ticketBinary: bytes
    def __init__(self, ticket: _Optional[str] = ..., ticketBinary: _Optional[bytes] = ..., playerTicket: _Optional[str] = ...) -> None: ...

class AppleIdLinkAuthRequest(_message.Message):
    __slots__ = ["authAppleId"]
    AUTHAPPLEID_FIELD_NUMBER: _ClassVar[int]
    authAppleId: AuthAppleId
    def __init__(self, authAppleId: _Optional[_Union[AuthAppleId, _Mapping]] = ...) -> None: ...

class AppleIdLinkAuthResponse(_message.Message):
    __slots__ = ["guestLinking"]
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class AppleIdUnLinkAuthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AppleIdUnLinkAuthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AuthAppleId(_message.Message):
    __slots__ = ["defaultName", "gameId", "gameVersion", "identityToken", "locale", "platform", "store"]
    DEFAULTNAME_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    IDENTITYTOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    defaultName: str
    gameId: str
    gameVersion: str
    identityToken: str
    locale: str
    platform: _common_message_pb2.Platform
    store: _common_message_pb2.Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., identityToken: _Optional[str] = ..., defaultName: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ...) -> None: ...

class AuthBoltId(_message.Message):
    __slots__ = ["gameId", "gameVersion", "locale", "platform", "store", "token"]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    locale: str
    platform: _common_message_pb2.Platform
    store: _common_message_pb2.Store
    token: str
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., token: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ...) -> None: ...

class AuthFacebook(_message.Message):
    __slots__ = ["gameId", "gameVersion", "locale", "platform", "store", "token"]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    locale: str
    platform: _common_message_pb2.Platform
    store: _common_message_pb2.Store
    token: str
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., token: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ...) -> None: ...

class AuthGameCenter(_message.Message):
    __slots__ = ["bundleId", "defaultName", "gameId", "gameVersion", "gpid", "locale", "platform", "publicKeyUrl", "salt", "signature", "store", "timestamp"]
    BUNDLEID_FIELD_NUMBER: _ClassVar[int]
    DEFAULTNAME_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEYURL_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    bundleId: str
    defaultName: str
    gameId: str
    gameVersion: str
    gpid: str
    locale: str
    platform: _common_message_pb2.Platform
    publicKeyUrl: str
    salt: bytes
    signature: bytes
    store: _common_message_pb2.Store
    timestamp: int
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., gpid: _Optional[str] = ..., bundleId: _Optional[str] = ..., publicKeyUrl: _Optional[str] = ..., signature: _Optional[bytes] = ..., salt: _Optional[bytes] = ..., timestamp: _Optional[int] = ..., defaultName: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ...) -> None: ...

class AuthGoogle(_message.Message):
    __slots__ = ["authCode", "gameId", "gameVersion", "locale", "platform", "store"]
    AUTHCODE_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    authCode: str
    gameId: str
    gameVersion: str
    locale: str
    platform: _common_message_pb2.Platform
    store: _common_message_pb2.Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., authCode: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ...) -> None: ...

class AuthGuest(_message.Message):
    __slots__ = ["gameId", "gameVersion", "locale", "platform", "store", "token"]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    locale: str
    platform: _common_message_pb2.Platform
    store: _common_message_pb2.Store
    token: str
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ..., token: _Optional[str] = ...) -> None: ...

class AuthHuawei(_message.Message):
    __slots__ = ["gameId", "gameVersion", "idToken", "locale", "platform", "store"]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    IDTOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    idToken: str
    locale: str
    platform: _common_message_pb2.Platform
    store: _common_message_pb2.Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., idToken: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ...) -> None: ...

class AuthTest(_message.Message):
    __slots__ = ["gameId", "gameVersion", "locale", "platform", "store", "token"]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    locale: str
    platform: _common_message_pb2.Platform
    store: _common_message_pb2.Store
    token: str
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., token: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ...) -> None: ...

class AuthTwitch(_message.Message):
    __slots__ = ["authCode", "gameId", "gameVersion", "locale", "platform", "store"]
    AUTHCODE_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    authCode: str
    gameId: str
    gameVersion: str
    locale: str
    platform: _common_message_pb2.Platform
    store: _common_message_pb2.Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., authCode: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ...) -> None: ...

class AuthVk(_message.Message):
    __slots__ = ["authCode", "authVkId", "gameId", "gameVersion", "locale", "platform", "store"]
    AUTHCODE_FIELD_NUMBER: _ClassVar[int]
    AUTHVKID_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    authCode: str
    authVkId: AuthVkId
    gameId: str
    gameVersion: str
    locale: str
    platform: _common_message_pb2.Platform
    store: _common_message_pb2.Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., authCode: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ..., authVkId: _Optional[_Union[AuthVkId, _Mapping]] = ...) -> None: ...

class AuthVkId(_message.Message):
    __slots__ = ["authorizationCode", "codeVerifier", "vkDeviceId"]
    AUTHORIZATIONCODE_FIELD_NUMBER: _ClassVar[int]
    CODEVERIFIER_FIELD_NUMBER: _ClassVar[int]
    VKDEVICEID_FIELD_NUMBER: _ClassVar[int]
    authorizationCode: str
    codeVerifier: str
    vkDeviceId: str
    def __init__(self, authorizationCode: _Optional[str] = ..., vkDeviceId: _Optional[str] = ..., codeVerifier: _Optional[str] = ...) -> None: ...

class BoltIdAuthRequest(_message.Message):
    __slots__ = ["appVerification", "authBoltId", "deviceInfo"]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    AUTHBOLTID_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    appVerification: AppVerification
    authBoltId: AuthBoltId
    deviceInfo: DeviceInfo
    def __init__(self, authBoltId: _Optional[_Union[AuthBoltId, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class BoltIdAuthResponse(_message.Message):
    __slots__ = ["playerTicket", "ticket", "ticketBinary"]
    PLAYERTICKET_FIELD_NUMBER: _ClassVar[int]
    TICKETBINARY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    playerTicket: str
    ticket: str
    ticketBinary: bytes
    def __init__(self, ticket: _Optional[str] = ..., ticketBinary: _Optional[bytes] = ..., playerTicket: _Optional[str] = ...) -> None: ...

class BoltIdLinkAuthRequest(_message.Message):
    __slots__ = ["authBoltId"]
    AUTHBOLTID_FIELD_NUMBER: _ClassVar[int]
    authBoltId: AuthBoltId
    def __init__(self, authBoltId: _Optional[_Union[AuthBoltId, _Mapping]] = ...) -> None: ...

class BoltIdLinkAuthResponse(_message.Message):
    __slots__ = ["guestLinking"]
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class BoltIdUnLinkAuthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class BoltIdUnLinkAuthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ["adsId", "deviceId", "deviceModel", "vndrId"]
    ADSID_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DEVICEMODEL_FIELD_NUMBER: _ClassVar[int]
    VNDRID_FIELD_NUMBER: _ClassVar[int]
    adsId: str
    deviceId: str
    deviceModel: str
    vndrId: str
    def __init__(self, deviceId: _Optional[str] = ..., deviceModel: _Optional[str] = ..., adsId: _Optional[str] = ..., vndrId: _Optional[str] = ...) -> None: ...

class FacebookAuthRequest(_message.Message):
    __slots__ = ["appVerification", "authFacebook", "deviceInfo"]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    AUTHFACEBOOK_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    appVerification: AppVerification
    authFacebook: AuthFacebook
    deviceInfo: DeviceInfo
    def __init__(self, authFacebook: _Optional[_Union[AuthFacebook, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class FacebookAuthResponse(_message.Message):
    __slots__ = ["playerTicket", "ticket", "ticketBinary"]
    PLAYERTICKET_FIELD_NUMBER: _ClassVar[int]
    TICKETBINARY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    playerTicket: str
    ticket: str
    ticketBinary: bytes
    def __init__(self, ticket: _Optional[str] = ..., ticketBinary: _Optional[bytes] = ..., playerTicket: _Optional[str] = ...) -> None: ...

class FacebookLinkAuthRequest(_message.Message):
    __slots__ = ["authFacebook"]
    AUTHFACEBOOK_FIELD_NUMBER: _ClassVar[int]
    authFacebook: AuthFacebook
    def __init__(self, authFacebook: _Optional[_Union[AuthFacebook, _Mapping]] = ...) -> None: ...

class FacebookLinkAuthResponse(_message.Message):
    __slots__ = ["guestLinking"]
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class FacebookUnLinkAuthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FacebookUnLinkAuthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GameCenterAuthRequest(_message.Message):
    __slots__ = ["appVerification", "authGameCenter", "deviceInfo"]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    AUTHGAMECENTER_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    appVerification: AppVerification
    authGameCenter: AuthGameCenter
    deviceInfo: DeviceInfo
    def __init__(self, authGameCenter: _Optional[_Union[AuthGameCenter, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class GameCenterAuthResponse(_message.Message):
    __slots__ = ["playerTicket", "ticket", "ticketBinary"]
    PLAYERTICKET_FIELD_NUMBER: _ClassVar[int]
    TICKETBINARY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    playerTicket: str
    ticket: str
    ticketBinary: bytes
    def __init__(self, ticket: _Optional[str] = ..., ticketBinary: _Optional[bytes] = ..., playerTicket: _Optional[str] = ...) -> None: ...

class GameCenterLinkAuthRequest(_message.Message):
    __slots__ = ["authGameCenter"]
    AUTHGAMECENTER_FIELD_NUMBER: _ClassVar[int]
    authGameCenter: AuthGameCenter
    def __init__(self, authGameCenter: _Optional[_Union[AuthGameCenter, _Mapping]] = ...) -> None: ...

class GameCenterLinkAuthResponse(_message.Message):
    __slots__ = ["guestLinking"]
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class GameCenterUnLinkAuthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GameCenterUnLinkAuthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetLinkedAuthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetLinkedAuthResponse(_message.Message):
    __slots__ = ["authTypes"]
    AUTHTYPES_FIELD_NUMBER: _ClassVar[int]
    authTypes: _containers.RepeatedCompositeFieldContainer[LinkedAuth]
    def __init__(self, authTypes: _Optional[_Iterable[_Union[LinkedAuth, _Mapping]]] = ...) -> None: ...

class GoogleAuthRequest(_message.Message):
    __slots__ = ["appVerification", "authGoogle", "deviceInfo"]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    AUTHGOOGLE_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    appVerification: AppVerification
    authGoogle: AuthGoogle
    deviceInfo: DeviceInfo
    def __init__(self, authGoogle: _Optional[_Union[AuthGoogle, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class GoogleAuthResponse(_message.Message):
    __slots__ = ["playerTicket", "ticket", "ticketBinary"]
    PLAYERTICKET_FIELD_NUMBER: _ClassVar[int]
    TICKETBINARY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    playerTicket: str
    ticket: str
    ticketBinary: bytes
    def __init__(self, ticket: _Optional[str] = ..., ticketBinary: _Optional[bytes] = ..., playerTicket: _Optional[str] = ...) -> None: ...

class GoogleLinkAuthRequest(_message.Message):
    __slots__ = ["authGoogle"]
    AUTHGOOGLE_FIELD_NUMBER: _ClassVar[int]
    authGoogle: AuthGoogle
    def __init__(self, authGoogle: _Optional[_Union[AuthGoogle, _Mapping]] = ...) -> None: ...

class GoogleLinkAuthResponse(_message.Message):
    __slots__ = ["guestLinking"]
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class GoogleUnLinkAuthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GoogleUnLinkAuthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GuestAuthRequest(_message.Message):
    __slots__ = ["appVerification", "authGuest", "deviceInfo"]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    AUTHGUEST_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    appVerification: AppVerification
    authGuest: AuthGuest
    deviceInfo: DeviceInfo
    def __init__(self, authGuest: _Optional[_Union[AuthGuest, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class GuestAuthResponse(_message.Message):
    __slots__ = ["playerTicket", "ticket", "ticketBinary"]
    PLAYERTICKET_FIELD_NUMBER: _ClassVar[int]
    TICKETBINARY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    playerTicket: str
    ticket: str
    ticketBinary: bytes
    def __init__(self, ticket: _Optional[str] = ..., ticketBinary: _Optional[bytes] = ..., playerTicket: _Optional[str] = ...) -> None: ...

class Handshake(_message.Message):
    __slots__ = ["ticket"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: str
    def __init__(self, ticket: _Optional[str] = ...) -> None: ...

class HandshakeResponse(_message.Message):
    __slots__ = ["boltSettings", "city", "country", "timestamp"]
    BOLTSETTINGS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    boltSettings: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.BoltSetting]
    city: str
    country: str
    timestamp: int
    def __init__(self, country: _Optional[str] = ..., boltSettings: _Optional[_Iterable[_Union[_common_message_pb2.BoltSetting, _Mapping]]] = ..., timestamp: _Optional[int] = ..., city: _Optional[str] = ...) -> None: ...

class HuaweiAuthRequest(_message.Message):
    __slots__ = ["appVerification", "authHuawei", "deviceInfo"]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    AUTHHUAWEI_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    appVerification: AppVerification
    authHuawei: AuthHuawei
    deviceInfo: DeviceInfo
    def __init__(self, authHuawei: _Optional[_Union[AuthHuawei, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class HuaweiAuthResponse(_message.Message):
    __slots__ = ["playerTicket", "ticket", "ticketBinary"]
    PLAYERTICKET_FIELD_NUMBER: _ClassVar[int]
    TICKETBINARY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    playerTicket: str
    ticket: str
    ticketBinary: bytes
    def __init__(self, ticket: _Optional[str] = ..., ticketBinary: _Optional[bytes] = ..., playerTicket: _Optional[str] = ...) -> None: ...

class HuaweiLinkAuthRequest(_message.Message):
    __slots__ = ["authHuawei"]
    AUTHHUAWEI_FIELD_NUMBER: _ClassVar[int]
    authHuawei: AuthHuawei
    def __init__(self, authHuawei: _Optional[_Union[AuthHuawei, _Mapping]] = ...) -> None: ...

class HuaweiLinkAuthResponse(_message.Message):
    __slots__ = ["guestLinking"]
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class HuaweiUnLinkAuthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class HuaweiUnLinkAuthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LinkedAuth(_message.Message):
    __slots__ = ["authType", "primary"]
    AUTHTYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    authType: _player_message_pb2.AuthType
    primary: bool
    def __init__(self, authType: _Optional[_Union[_player_message_pb2.AuthType, str]] = ..., primary: bool = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TestAuthRequest(_message.Message):
    __slots__ = ["authTest", "deviceInfo", "verification"]
    AUTHTEST_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    authTest: AuthTest
    deviceInfo: DeviceInfo
    verification: AppVerification
    def __init__(self, authTest: _Optional[_Union[AuthTest, _Mapping]] = ..., verification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class TestAuthResponse(_message.Message):
    __slots__ = ["playerTicket", "ticket", "ticketBinary"]
    PLAYERTICKET_FIELD_NUMBER: _ClassVar[int]
    TICKETBINARY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    playerTicket: str
    ticket: str
    ticketBinary: bytes
    def __init__(self, ticket: _Optional[str] = ..., ticketBinary: _Optional[bytes] = ..., playerTicket: _Optional[str] = ...) -> None: ...

class TwitchLinkAuthRequest(_message.Message):
    __slots__ = ["authTwitch"]
    AUTHTWITCH_FIELD_NUMBER: _ClassVar[int]
    authTwitch: AuthTwitch
    def __init__(self, authTwitch: _Optional[_Union[AuthTwitch, _Mapping]] = ...) -> None: ...

class TwitchLinkAuthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TwitchUnLinkAuthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TwitchUnLinkAuthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VkAuthRequest(_message.Message):
    __slots__ = ["appVerification", "authVk", "deviceInfo"]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    AUTHVK_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    appVerification: AppVerification
    authVk: AuthVk
    deviceInfo: DeviceInfo
    def __init__(self, authVk: _Optional[_Union[AuthVk, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class VkAuthResponse(_message.Message):
    __slots__ = ["playerTicket", "ticket", "ticketBinary"]
    PLAYERTICKET_FIELD_NUMBER: _ClassVar[int]
    TICKETBINARY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    playerTicket: str
    ticket: str
    ticketBinary: bytes
    def __init__(self, ticket: _Optional[str] = ..., ticketBinary: _Optional[bytes] = ..., playerTicket: _Optional[str] = ...) -> None: ...

class VkLinkAuthRequest(_message.Message):
    __slots__ = ["authVk"]
    AUTHVK_FIELD_NUMBER: _ClassVar[int]
    authVk: AuthVk
    def __init__(self, authVk: _Optional[_Union[AuthVk, _Mapping]] = ...) -> None: ...

class VkLinkAuthResponse(_message.Message):
    __slots__ = ["guestLinking"]
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class VkUnLinkAuthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VkUnLinkAuthResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
