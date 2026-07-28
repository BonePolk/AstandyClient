from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameSeason(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetGameSeasonsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetGameSeasonsResponse(_message.Message):
    __slots__ = ["seasons"]
    SEASONS_FIELD_NUMBER: _ClassVar[int]
    seasons: _containers.RepeatedCompositeFieldContainer[GameSeason]
    def __init__(self, seasons: _Optional[_Iterable[_Union[GameSeason, _Mapping]]] = ...) -> None: ...
