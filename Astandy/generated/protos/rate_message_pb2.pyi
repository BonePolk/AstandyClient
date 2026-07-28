import inventory_message_pb2 as _inventory_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AskLaterRequest(_message.Message):
    __slots__ = ["context", "internalData", "timestampAskLater"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPASKLATER_FIELD_NUMBER: _ClassVar[int]
    context: str
    internalData: str
    timestampAskLater: int
    def __init__(self, timestampAskLater: _Optional[int] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...

class AskLaterResponse(_message.Message):
    __slots__ = ["context", "internalData", "timestamp", "timestampAskLater"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPASKLATER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    context: str
    internalData: str
    timestamp: int
    timestampAskLater: int
    def __init__(self, timestampAskLater: _Optional[int] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class DontAskLaterRequest(_message.Message):
    __slots__ = ["context", "internalData"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    context: str
    internalData: str
    def __init__(self, internalData: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...

class DontAskLaterResponse(_message.Message):
    __slots__ = ["context", "dontAskLater", "internalData", "timestamp"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DONTASKLATER_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    context: str
    dontAskLater: bool
    internalData: str
    timestamp: int
    def __init__(self, dontAskLater: bool = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class GetLastRateGameRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetLastRateGameResponse(_message.Message):
    __slots__ = ["context", "dontAskLater", "internalData", "message", "rate", "rateContexts", "reward", "timestamp", "timestampAskLater"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DONTASKLATER_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RATECONTEXTS_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPASKLATER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    context: str
    dontAskLater: bool
    internalData: str
    message: str
    rate: int
    rateContexts: _containers.RepeatedCompositeFieldContainer[RateContext]
    reward: _inventory_message_pb2.RewardInfo
    timestamp: int
    timestampAskLater: int
    def __init__(self, rate: _Optional[int] = ..., message: _Optional[str] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ..., timestampAskLater: _Optional[int] = ..., dontAskLater: bool = ..., timestamp: _Optional[int] = ..., rateContexts: _Optional[_Iterable[_Union[RateContext, _Mapping]]] = ..., reward: _Optional[_Union[_inventory_message_pb2.RewardInfo, _Mapping]] = ...) -> None: ...

class RateContext(_message.Message):
    __slots__ = ["data", "id"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    data: str
    id: str
    def __init__(self, id: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class RateGameRequest(_message.Message):
    __slots__ = ["context", "internalData", "message", "rate"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    context: str
    internalData: str
    message: str
    rate: int
    def __init__(self, rate: _Optional[int] = ..., message: _Optional[str] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...

class RateGameResponse(_message.Message):
    __slots__ = ["context", "internalData", "message", "rate", "reward", "timestamp"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    context: str
    internalData: str
    message: str
    rate: int
    reward: _inventory_message_pb2.GivenReward
    timestamp: int
    def __init__(self, rate: _Optional[int] = ..., message: _Optional[str] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ..., timestamp: _Optional[int] = ..., reward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ...) -> None: ...
