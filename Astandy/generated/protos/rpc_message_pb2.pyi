from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BinaryValue(_message.Message):
    __slots__ = ["array", "isNull", "one"]
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    ISNULL_FIELD_NUMBER: _ClassVar[int]
    ONE_FIELD_NUMBER: _ClassVar[int]
    array: _containers.RepeatedScalarFieldContainer[bytes]
    isNull: bool
    one: bytes
    def __init__(self, isNull: bool = ..., array: _Optional[_Iterable[bytes]] = ..., one: _Optional[bytes] = ...) -> None: ...

class Boolean(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class BooleanArray(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, value: _Optional[_Iterable[bool]] = ...) -> None: ...

class Byte(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class ByteArray(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class CompressedInstance(_message.Message):
    __slots__ = ["payload", "uncompressedLength"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    UNCOMPRESSEDLENGTH_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    uncompressedLength: int
    def __init__(self, uncompressedLength: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class Double(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class DoubleArray(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, value: _Optional[_Iterable[float]] = ...) -> None: ...

class Enum(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class EventResponse(_message.Message):
    __slots__ = ["eventId", "eventName", "listenerName", "params"]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    EVENTNAME_FIELD_NUMBER: _ClassVar[int]
    LISTENERNAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    eventId: int
    eventName: str
    listenerName: str
    params: _containers.RepeatedCompositeFieldContainer[BinaryValue]
    def __init__(self, listenerName: _Optional[str] = ..., eventName: _Optional[str] = ..., params: _Optional[_Iterable[_Union[BinaryValue, _Mapping]]] = ..., eventId: _Optional[int] = ...) -> None: ...

class Exception(_message.Message):
    __slots__ = ["code", "id", "params"]
    class ParamsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    code: int
    id: int
    params: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[int] = ..., code: _Optional[int] = ..., params: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Float(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class FloatArray(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, value: _Optional[_Iterable[float]] = ...) -> None: ...

class Integer(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class IntegerArray(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, value: _Optional[_Iterable[int]] = ...) -> None: ...

class Long(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class LongArray(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, value: _Optional[_Iterable[int]] = ...) -> None: ...

class QueuedMessage(_message.Message):
    __slots__ = ["boltId", "gameId", "important", "message", "timestamp", "topic", "userId"]
    BOLTID_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    IMPORTANT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    boltId: str
    gameId: str
    important: bool
    message: ResponseMessage
    timestamp: int
    topic: str
    userId: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, message: _Optional[_Union[ResponseMessage, _Mapping]] = ..., boltId: _Optional[str] = ..., timestamp: _Optional[int] = ..., userId: _Optional[_Iterable[str]] = ..., topic: _Optional[str] = ..., important: bool = ..., gameId: _Optional[str] = ...) -> None: ...

class ResponseMessage(_message.Message):
    __slots__ = ["compressedInstance", "eventResponse", "rpcResponse"]
    COMPRESSEDINSTANCE_FIELD_NUMBER: _ClassVar[int]
    EVENTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    RPCRESPONSE_FIELD_NUMBER: _ClassVar[int]
    compressedInstance: CompressedInstance
    eventResponse: EventResponse
    rpcResponse: RpcResponse
    def __init__(self, rpcResponse: _Optional[_Union[RpcResponse, _Mapping]] = ..., eventResponse: _Optional[_Union[EventResponse, _Mapping]] = ..., compressedInstance: _Optional[_Union[CompressedInstance, _Mapping]] = ...) -> None: ...

class RpcRequest(_message.Message):
    __slots__ = ["compressedInstance", "id", "methodId", "methodName", "params", "serviceName"]
    COMPRESSEDINSTANCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    METHODID_FIELD_NUMBER: _ClassVar[int]
    METHODNAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    SERVICENAME_FIELD_NUMBER: _ClassVar[int]
    compressedInstance: CompressedInstance
    id: str
    methodId: int
    methodName: str
    params: _containers.RepeatedCompositeFieldContainer[BinaryValue]
    serviceName: str
    def __init__(self, id: _Optional[str] = ..., serviceName: _Optional[str] = ..., methodName: _Optional[str] = ..., params: _Optional[_Iterable[_Union[BinaryValue, _Mapping]]] = ..., methodId: _Optional[int] = ..., compressedInstance: _Optional[_Union[CompressedInstance, _Mapping]] = ...) -> None: ...

class RpcResponse(_message.Message):
    __slots__ = ["exception", "id"]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELD_NUMBER: _ClassVar[int]
    exception: Exception
    id: str
    def __init__(self, id: _Optional[str] = ..., exception: _Optional[_Union[Exception, _Mapping]] = ..., **kwargs) -> None: ...

class String(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class StringArray(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value: _Optional[_Iterable[str]] = ...) -> None: ...
