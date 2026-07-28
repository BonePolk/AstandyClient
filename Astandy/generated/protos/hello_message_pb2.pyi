from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ["e", "iv", "n", "sdkVersion"]
    E_FIELD_NUMBER: _ClassVar[int]
    IV_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    SDKVERSION_FIELD_NUMBER: _ClassVar[int]
    e: bytes
    iv: bytes
    n: bytes
    sdkVersion: str
    def __init__(self, n: _Optional[bytes] = ..., e: _Optional[bytes] = ..., iv: _Optional[bytes] = ..., sdkVersion: _Optional[str] = ...) -> None: ...

class HelloRequestV2(_message.Message):
    __slots__ = ["sdkVersion"]
    SDKVERSION_FIELD_NUMBER: _ClassVar[int]
    sdkVersion: str
    def __init__(self, sdkVersion: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ["key", "uniqueValue"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    UNIQUEVALUE_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    uniqueValue: str
    def __init__(self, key: _Optional[bytes] = ..., uniqueValue: _Optional[str] = ...) -> None: ...

class HelloResponseV2(_message.Message):
    __slots__ = ["uniqueValue"]
    UNIQUEVALUE_FIELD_NUMBER: _ClassVar[int]
    uniqueValue: str
    def __init__(self, uniqueValue: _Optional[str] = ...) -> None: ...
