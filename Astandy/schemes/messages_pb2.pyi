from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BinaryValue(_message.Message):
    __slots__ = ("isNull", "array", "one")
    ISNULL_FIELD_NUMBER: _ClassVar[int]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    ONE_FIELD_NUMBER: _ClassVar[int]
    isNull: bool
    array: _containers.RepeatedScalarFieldContainer[bytes]
    one: bytes
    def __init__(self, isNull: bool = ..., array: _Optional[_Iterable[bytes]] = ..., one: _Optional[bytes] = ...) -> None: ...

class ClientMsg(_message.Message):
    __slots__ = ("id", "cls", "func", "data", "code")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLS_FIELD_NUMBER: _ClassVar[int]
    FUNC_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    cls: str
    func: str
    data: _containers.RepeatedCompositeFieldContainer[BinaryValue]
    code: int
    def __init__(self, id: _Optional[str] = ..., cls: _Optional[str] = ..., func: _Optional[str] = ..., data: _Optional[_Iterable[_Union[BinaryValue, _Mapping]]] = ..., code: _Optional[int] = ...) -> None: ...

class Exception(_message.Message):
    __slots__ = ("at", "code", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    at: int
    code: int
    properties: _containers.ScalarMap[str, str]
    def __init__(self, at: _Optional[int] = ..., code: _Optional[int] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("id", "exception", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    exception: Exception
    data: _containers.RepeatedCompositeFieldContainer[BinaryValue]
    def __init__(self, id: _Optional[str] = ..., exception: _Optional[_Union[Exception, _Mapping]] = ..., data: _Optional[_Iterable[_Union[BinaryValue, _Mapping]]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("listener", "event", "params", "code")
    LISTENER_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    listener: str
    event: str
    params: BinaryValue
    code: int
    def __init__(self, listener: _Optional[str] = ..., event: _Optional[str] = ..., params: _Optional[_Union[BinaryValue, _Mapping]] = ..., code: _Optional[int] = ...) -> None: ...

class CompressedInstance(_message.Message):
    __slots__ = ("uncompressed_size", "compressed")
    UNCOMPRESSED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    uncompressed_size: int
    compressed: bytes
    def __init__(self, uncompressed_size: _Optional[int] = ..., compressed: _Optional[bytes] = ...) -> None: ...

class ServerMsg(_message.Message):
    __slots__ = ("responses", "events", "compressed_instances")
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[Response]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    compressed_instances: _containers.RepeatedCompositeFieldContainer[CompressedInstance]
    def __init__(self, responses: _Optional[_Iterable[_Union[Response, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ..., compressed_instances: _Optional[_Iterable[_Union[CompressedInstance, _Mapping]]] = ...) -> None: ...
