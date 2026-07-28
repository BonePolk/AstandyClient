import common_message_pb2 as _common_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameSetting(_message.Message):
    __slots__ = ["boolValue", "floatValue", "intValue", "key", "longValue", "type", "value"]
    BOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    boolValue: bool
    floatValue: float
    intValue: int
    key: str
    longValue: int
    type: _common_message_pb2.SettingType
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., boolValue: bool = ..., type: _Optional[_Union[_common_message_pb2.SettingType, str]] = ..., longValue: _Optional[int] = ...) -> None: ...

class GetGameSettingsEncryptedRequest(_message.Message):
    __slots__ = ["checksum"]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    checksum: bytes
    def __init__(self, checksum: _Optional[bytes] = ...) -> None: ...

class GetGameSettingsEncryptedResponse(_message.Message):
    __slots__ = ["gameSettings", "settingsExist"]
    GAMESETTINGS_FIELD_NUMBER: _ClassVar[int]
    SETTINGSEXIST_FIELD_NUMBER: _ClassVar[int]
    gameSettings: _containers.RepeatedCompositeFieldContainer[GameSetting]
    settingsExist: bool
    def __init__(self, gameSettings: _Optional[_Iterable[_Union[GameSetting, _Mapping]]] = ..., settingsExist: bool = ...) -> None: ...

class GetGameSettingsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetGameSettingsResponse(_message.Message):
    __slots__ = ["gameSettings"]
    GAMESETTINGS_FIELD_NUMBER: _ClassVar[int]
    gameSettings: _containers.RepeatedCompositeFieldContainer[GameSetting]
    def __init__(self, gameSettings: _Optional[_Iterable[_Union[GameSetting, _Mapping]]] = ...) -> None: ...
