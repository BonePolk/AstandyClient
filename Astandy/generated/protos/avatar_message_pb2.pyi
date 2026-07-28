from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DefaultAvatar(_message.Message):
    __slots__ = ["avatarId"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    def __init__(self, avatarId: _Optional[str] = ...) -> None: ...

class GetDefaultAvatarsRequest(_message.Message):
    __slots__ = ["lastUpdated"]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    lastUpdated: str
    def __init__(self, lastUpdated: _Optional[str] = ...) -> None: ...

class GetDefaultAvatarsResponse(_message.Message):
    __slots__ = ["avatars", "lastUpdated"]
    AVATARS_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    avatars: _containers.RepeatedCompositeFieldContainer[DefaultAvatar]
    lastUpdated: str
    def __init__(self, avatars: _Optional[_Iterable[_Union[DefaultAvatar, _Mapping]]] = ..., lastUpdated: _Optional[str] = ...) -> None: ...
