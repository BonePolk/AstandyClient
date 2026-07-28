from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HackDetection(_message.Message):
    __slots__ = ["apkHash", "isRooted", "json", "modDate"]
    APKHASH_FIELD_NUMBER: _ClassVar[int]
    ISROOTED_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    MODDATE_FIELD_NUMBER: _ClassVar[int]
    apkHash: str
    isRooted: bool
    json: _containers.RepeatedScalarFieldContainer[str]
    modDate: int
    def __init__(self, apkHash: _Optional[str] = ..., isRooted: bool = ..., json: _Optional[_Iterable[str]] = ..., modDate: _Optional[int] = ...) -> None: ...
