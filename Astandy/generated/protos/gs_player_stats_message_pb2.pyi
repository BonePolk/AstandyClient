import player_stats_message_pb2 as _player_stats_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GSGetPlayersStatsRequest(_message.Message):
    __slots__ = ["gpids", "statIds"]
    GPIDS_FIELD_NUMBER: _ClassVar[int]
    STATIDS_FIELD_NUMBER: _ClassVar[int]
    gpids: _containers.RepeatedScalarFieldContainer[str]
    statIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gpids: _Optional[_Iterable[str]] = ..., statIds: _Optional[_Iterable[str]] = ...) -> None: ...

class GSGetPlayersStatsResponse(_message.Message):
    __slots__ = ["playersStats"]
    PLAYERSSTATS_FIELD_NUMBER: _ClassVar[int]
    playersStats: _containers.RepeatedCompositeFieldContainer[_player_stats_message_pb2.PlayerStats]
    def __init__(self, playersStats: _Optional[_Iterable[_Union[_player_stats_message_pb2.PlayerStats, _Mapping]]] = ...) -> None: ...

class GSIncrementPlayersStatsRequest(_message.Message):
    __slots__ = ["stats"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[_player_stats_message_pb2.PlayerStats]
    def __init__(self, stats: _Optional[_Iterable[_Union[_player_stats_message_pb2.PlayerStats, _Mapping]]] = ...) -> None: ...

class GSIncrementPlayersStatsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
