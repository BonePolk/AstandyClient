import common_message_pb2 as _common_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Dlc(_message.Message):
    __slots__ = ["files", "key", "name", "properties"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[DlcFile]
    key: str
    name: str
    properties: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    def __init__(self, key: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ..., files: _Optional[_Iterable[_Union[DlcFile, _Mapping]]] = ...) -> None: ...

class DlcFile(_message.Message):
    __slots__ = ["fileName", "fileSizeInBytes", "properties", "resourceUrls", "signature"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILESIZEINBYTES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    RESOURCEURLS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    fileName: str
    fileSizeInBytes: int
    properties: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    resourceUrls: _containers.RepeatedScalarFieldContainer[str]
    signature: str
    def __init__(self, resourceUrls: _Optional[_Iterable[str]] = ..., fileSizeInBytes: _Optional[int] = ..., signature: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ..., fileName: _Optional[str] = ...) -> None: ...

class DlcResponse(_message.Message):
    __slots__ = ["cdnUrls", "dlcExist", "dlcs"]
    CDNURLS_FIELD_NUMBER: _ClassVar[int]
    DLCEXIST_FIELD_NUMBER: _ClassVar[int]
    DLCS_FIELD_NUMBER: _ClassVar[int]
    cdnUrls: _containers.RepeatedScalarFieldContainer[str]
    dlcExist: bool
    dlcs: _containers.RepeatedCompositeFieldContainer[Dlc]
    def __init__(self, dlcs: _Optional[_Iterable[_Union[Dlc, _Mapping]]] = ..., cdnUrls: _Optional[_Iterable[str]] = ..., dlcExist: bool = ...) -> None: ...

class PreviewDlcRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReleasedDlcRequest(_message.Message):
    __slots__ = ["checksum", "gameUid", "platform", "version"]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    GAMEUID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    checksum: bytes
    gameUid: str
    platform: _common_message_pb2.Platform
    version: str
    def __init__(self, version: _Optional[str] = ..., gameUid: _Optional[str] = ..., platform: _Optional[_Union[_common_message_pb2.Platform, str]] = ..., checksum: _Optional[bytes] = ...) -> None: ...
