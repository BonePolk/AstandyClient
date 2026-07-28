from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

Amazon: Store
Android: Platform
AppGallery: Store
AppStore: Store
BOOLEAN: PropertyType
Bool: SettingType
DATE: PropertyType
DESCRIPTOR: _descriptor.FileDescriptor
Dev: Store
EQUAL: Comparison
EQUAL_TO_OR_GREATER_THAN: Comparison
EQUAL_TO_OR_LESS_THAN: Comparison
FLOAT: PropertyType
Float: SettingType
GREATER_THAN: Comparison
GetApps: Store
GooglePlay: Store
IN: Comparison
INT: PropertyType
IN_OR_NULL: Comparison
IOS: Platform
ITEM_ID: PropertyType
Integer: SettingType
JSON: PropertyType
LESS_THAN: Comparison
LONG: PropertyType
Long: SettingType
NOT_EQUAL: Comparison
Oct: Store
RANDOM_UNIFORM: PropertyType
RESOURCE_URL: PropertyType
START_WITH: Comparison
STRING: PropertyType
String: SettingType
Unknown: Platform
Yoo: Store

class AvatarBinary(_message.Message):
    __slots__ = ["avatar", "id"]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    avatar: bytes
    id: str
    def __init__(self, id: _Optional[str] = ..., avatar: _Optional[bytes] = ...) -> None: ...

class BanGamePlayerCustomRequest(_message.Message):
    __slots__ = ["code", "description", "gpid", "message", "tag", "until"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    code: int
    description: str
    gpid: str
    message: str
    tag: str
    until: int
    def __init__(self, gpid: _Optional[str] = ..., code: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ..., tag: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class BanGamePlayerRequest(_message.Message):
    __slots__ = ["code", "description", "gpid", "tag"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    code: int
    description: str
    gpid: str
    tag: str
    def __init__(self, gpid: _Optional[str] = ..., code: _Optional[int] = ..., tag: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class BanGamePlayerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Banned(_message.Message):
    __slots__ = ["banned", "untilDate"]
    BANNED_FIELD_NUMBER: _ClassVar[int]
    UNTILDATE_FIELD_NUMBER: _ClassVar[int]
    banned: bool
    untilDate: int
    def __init__(self, banned: bool = ..., untilDate: _Optional[int] = ...) -> None: ...

class BoltSetting(_message.Message):
    __slots__ = ["booleanValue", "floatValue", "intValue", "key", "longValue", "stringValue", "type"]
    BOOLEANVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    booleanValue: bool
    floatValue: float
    intValue: int
    key: str
    longValue: int
    stringValue: str
    type: SettingType
    def __init__(self, key: _Optional[str] = ..., type: _Optional[_Union[SettingType, str]] = ..., stringValue: _Optional[str] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., booleanValue: bool = ..., longValue: _Optional[int] = ...) -> None: ...

class CheckBanGamePlayerRequest(_message.Message):
    __slots__ = ["gpid"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gpid: _Optional[_Iterable[str]] = ...) -> None: ...

class CheckBanGamePlayerResponse(_message.Message):
    __slots__ = ["ban"]
    BAN_FIELD_NUMBER: _ClassVar[int]
    ban: _containers.RepeatedCompositeFieldContainer[CheckBanResult]
    def __init__(self, ban: _Optional[_Iterable[_Union[CheckBanResult, _Mapping]]] = ...) -> None: ...

class CheckBanResult(_message.Message):
    __slots__ = ["code", "gpid", "scope"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    code: int
    gpid: str
    scope: int
    def __init__(self, gpid: _Optional[str] = ..., code: _Optional[int] = ..., scope: _Optional[int] = ...) -> None: ...

class ContinuationToken(_message.Message):
    __slots__ = ["length", "token"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    length: int
    token: str
    def __init__(self, length: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class DateRange(_message.Message):
    __slots__ = ["to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: int
    def __init__(self, to: _Optional[int] = ..., **kwargs) -> None: ...

class DayRange(_message.Message):
    __slots__ = ["to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: int
    def __init__(self, to: _Optional[int] = ..., **kwargs) -> None: ...

class Dictionary(_message.Message):
    __slots__ = ["content"]
    class ContentEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: _containers.ScalarMap[str, str]
    def __init__(self, content: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EnvironmentInfo(_message.Message):
    __slots__ = ["environment", "version"]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    environment: bytes
    version: int
    def __init__(self, version: _Optional[int] = ..., environment: _Optional[bytes] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ["comparison", "floatValue", "intValue", "name", "stringValue", "strings"]
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    comparison: Comparison
    floatValue: float
    intValue: int
    name: str
    stringValue: str
    strings: Strings
    def __init__(self, name: _Optional[str] = ..., comparison: _Optional[_Union[Comparison, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., stringValue: _Optional[str] = ..., strings: _Optional[_Union[Strings, _Mapping]] = ...) -> None: ...

class GameServer(_message.Message):
    __slots__ = ["id", "ip", "port"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ip: str
    port: int
    def __init__(self, id: _Optional[str] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class GetAvatarsRequest(_message.Message):
    __slots__ = ["avatarIds"]
    AVATARIDS_FIELD_NUMBER: _ClassVar[int]
    avatarIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, avatarIds: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAvatarsResponse(_message.Message):
    __slots__ = ["avatarBinaries"]
    AVATARBINARIES_FIELD_NUMBER: _ClassVar[int]
    avatarBinaries: _containers.RepeatedCompositeFieldContainer[AvatarBinary]
    def __init__(self, avatarBinaries: _Optional[_Iterable[_Union[AvatarBinary, _Mapping]]] = ...) -> None: ...

class LocalizedTitle(_message.Message):
    __slots__ = ["description", "name", "resourceUrl"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCEURL_FIELD_NUMBER: _ClassVar[int]
    description: str
    name: str
    resourceUrl: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., resourceUrl: _Optional[str] = ...) -> None: ...

class Offset(_message.Message):
    __slots__ = ["length", "offset"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    length: int
    offset: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class Page(_message.Message):
    __slots__ = ["page", "size"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    size: int
    def __init__(self, page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class PhotonGame(_message.Message):
    __slots__ = ["appVersion", "customProperties", "region", "roomId"]
    class CustomPropertiesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPVERSION_FIELD_NUMBER: _ClassVar[int]
    CUSTOMPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    appVersion: str
    customProperties: _containers.ScalarMap[str, str]
    region: str
    roomId: str
    def __init__(self, region: _Optional[str] = ..., roomId: _Optional[str] = ..., appVersion: _Optional[str] = ..., customProperties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Property(_message.Message):
    __slots__ = ["booleanValue", "floatValue", "intValue", "longValue", "name", "stringValue", "type"]
    BOOLEANVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    booleanValue: bool
    floatValue: float
    intValue: int
    longValue: int
    name: str
    stringValue: str
    type: PropertyType
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[PropertyType, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., longValue: _Optional[int] = ..., stringValue: _Optional[str] = ..., booleanValue: bool = ...) -> None: ...

class Range(_message.Message):
    __slots__ = ["to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: int
    def __init__(self, to: _Optional[int] = ..., **kwargs) -> None: ...

class SetPhotonGameRequest(_message.Message):
    __slots__ = ["gpid", "photonGame"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    photonGame: PhotonGame
    def __init__(self, gpid: _Optional[str] = ..., photonGame: _Optional[_Union[PhotonGame, _Mapping]] = ...) -> None: ...

class SetPhotonGameResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Strings(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value: _Optional[_Iterable[str]] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ["topic"]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str
    def __init__(self, topic: _Optional[str] = ...) -> None: ...

class SubscribeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UnsubscribeRequest(_message.Message):
    __slots__ = ["topic"]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str
    def __init__(self, topic: _Optional[str] = ...) -> None: ...

class UnsubscribeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserConfigBinary(_message.Message):
    __slots__ = ["config"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: bytes
    def __init__(self, config: _Optional[bytes] = ...) -> None: ...

class Comparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Store(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SettingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
