import common_message_pb2 as _common_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccusationByServerRequest(_message.Message):
    __slots__ = ["environment", "gpid", "matchId", "reporters"]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    REPORTERS_FIELD_NUMBER: _ClassVar[int]
    environment: _common_message_pb2.EnvironmentInfo
    gpid: str
    matchId: str
    reporters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gpid: _Optional[str] = ..., reporters: _Optional[_Iterable[str]] = ..., matchId: _Optional[str] = ..., environment: _Optional[_Union[_common_message_pb2.EnvironmentInfo, _Mapping]] = ...) -> None: ...

class AccusationByServerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
