from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

BY_TOKEN_ACCESS_MODE: FileAccessMode
DESCRIPTOR: _descriptor.FileDescriptor
PRIVATE_ACCESS_MODE: FileAccessMode
PUBLIC_ACCESS_MODE: FileAccessMode

class ChangeFileAccessModeRequest(_message.Message):
    __slots__ = ["accessMode", "filename"]
    ACCESSMODE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    accessMode: FileAccessMode
    filename: str
    def __init__(self, filename: _Optional[str] = ..., accessMode: _Optional[_Union[FileAccessMode, str]] = ...) -> None: ...

class ChangeFileAccessModeResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class DeleteFileRequest(_message.Message):
    __slots__ = ["filename"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class DeleteFileResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetFilenamesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetFilenamesResponse(_message.Message):
    __slots__ = ["filenames"]
    FILENAMES_FIELD_NUMBER: _ClassVar[int]
    filenames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, filenames: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSharedFileRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class GetSharedFileResponse(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: Storage
    def __init__(self, file: _Optional[_Union[Storage, _Mapping]] = ...) -> None: ...

class ReadAllFilesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadAllFilesResponse(_message.Message):
    __slots__ = ["files"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[Storage]
    def __init__(self, files: _Optional[_Iterable[_Union[Storage, _Mapping]]] = ...) -> None: ...

class ReadFile3Request(_message.Message):
    __slots__ = ["filename"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class ReadFile3Response(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: Storage
    def __init__(self, file: _Optional[_Union[Storage, _Mapping]] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ["filename"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: bytes
    def __init__(self, file: _Optional[bytes] = ...) -> None: ...

class ReadFilesRequest(_message.Message):
    __slots__ = ["filenames"]
    FILENAMES_FIELD_NUMBER: _ClassVar[int]
    filenames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, filenames: _Optional[_Iterable[str]] = ...) -> None: ...

class ReadFilesResponse(_message.Message):
    __slots__ = ["files"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[Storage]
    def __init__(self, files: _Optional[_Iterable[_Union[Storage, _Mapping]]] = ...) -> None: ...

class ReadPlayerPublicFilesRequest(_message.Message):
    __slots__ = ["filenames", "gpid"]
    FILENAMES_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    filenames: _containers.RepeatedScalarFieldContainer[str]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ..., filenames: _Optional[_Iterable[str]] = ...) -> None: ...

class ReadPlayerPublicFilesResponse(_message.Message):
    __slots__ = ["files"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[Storage]
    def __init__(self, files: _Optional[_Iterable[_Union[Storage, _Mapping]]] = ...) -> None: ...

class ReadPublicFileRequest(_message.Message):
    __slots__ = ["filename", "gpid"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    filename: str
    gpid: str
    def __init__(self, gpid: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class ReadPublicFileResponse(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: Storage
    def __init__(self, file: _Optional[_Union[Storage, _Mapping]] = ...) -> None: ...

class ShareFileRequest(_message.Message):
    __slots__ = ["filename"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class ShareFileResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class Storage(_message.Message):
    __slots__ = ["accessMode", "file", "filename", "gpid", "token"]
    ACCESSMODE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    accessMode: FileAccessMode
    file: bytes
    filename: str
    gpid: str
    token: str
    def __init__(self, filename: _Optional[str] = ..., file: _Optional[bytes] = ..., gpid: _Optional[str] = ..., token: _Optional[str] = ..., accessMode: _Optional[_Union[FileAccessMode, str]] = ...) -> None: ...

class UnshareFileRequest(_message.Message):
    __slots__ = ["filename"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class UnshareFileResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ["file", "filename", "type"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    file: bytes
    filename: str
    type: str
    def __init__(self, filename: _Optional[str] = ..., file: _Optional[bytes] = ..., type: _Optional[str] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ["accessMode", "filename", "gpid", "token"]
    ACCESSMODE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    accessMode: FileAccessMode
    filename: str
    gpid: str
    token: str
    def __init__(self, filename: _Optional[str] = ..., gpid: _Optional[str] = ..., token: _Optional[str] = ..., accessMode: _Optional[_Union[FileAccessMode, str]] = ...) -> None: ...

class FileAccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
