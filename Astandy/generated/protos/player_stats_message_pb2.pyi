import stats_message_pb2 as _stats_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCurrentStatsRequest(_message.Message):
    __slots__ = ["addLeaderboardStats"]
    ADDLEADERBOARDSTATS_FIELD_NUMBER: _ClassVar[int]
    addLeaderboardStats: bool
    def __init__(self, addLeaderboardStats: bool = ...) -> None: ...

class GetCurrentStatsResponse(_message.Message):
    __slots__ = ["stats"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: Stats
    def __init__(self, stats: _Optional[_Union[Stats, _Mapping]] = ...) -> None: ...

class GetGlobalStatsRequest(_message.Message):
    __slots__ = ["historicDays"]
    HISTORICDAYS_FIELD_NUMBER: _ClassVar[int]
    historicDays: int
    def __init__(self, historicDays: _Optional[int] = ...) -> None: ...

class GetGlobalStatsResponse(_message.Message):
    __slots__ = ["playerStats"]
    PLAYERSTATS_FIELD_NUMBER: _ClassVar[int]
    playerStats: _containers.RepeatedCompositeFieldContainer[PlayerStat]
    def __init__(self, playerStats: _Optional[_Iterable[_Union[PlayerStat, _Mapping]]] = ...) -> None: ...

class GetPlayerStatsRequest(_message.Message):
    __slots__ = ["addLeaderboardStats", "apiNames", "gpid"]
    ADDLEADERBOARDSTATS_FIELD_NUMBER: _ClassVar[int]
    APINAMES_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    addLeaderboardStats: bool
    apiNames: _containers.RepeatedScalarFieldContainer[str]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ..., apiNames: _Optional[_Iterable[str]] = ..., addLeaderboardStats: bool = ...) -> None: ...

class GetPlayerStatsResponse(_message.Message):
    __slots__ = ["playerStats"]
    PLAYERSTATS_FIELD_NUMBER: _ClassVar[int]
    playerStats: PlayerStats
    def __init__(self, playerStats: _Optional[_Union[PlayerStats, _Mapping]] = ...) -> None: ...

class GetPlayersStatsRequest(_message.Message):
    __slots__ = ["addLeaderboardStats", "apiNames", "gpids"]
    ADDLEADERBOARDSTATS_FIELD_NUMBER: _ClassVar[int]
    APINAMES_FIELD_NUMBER: _ClassVar[int]
    GPIDS_FIELD_NUMBER: _ClassVar[int]
    addLeaderboardStats: bool
    apiNames: _containers.RepeatedScalarFieldContainer[str]
    gpids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gpids: _Optional[_Iterable[str]] = ..., apiNames: _Optional[_Iterable[str]] = ..., addLeaderboardStats: bool = ...) -> None: ...

class GetPlayersStatsResponse(_message.Message):
    __slots__ = ["playersStats"]
    PLAYERSSTATS_FIELD_NUMBER: _ClassVar[int]
    playersStats: _containers.RepeatedCompositeFieldContainer[PlayerStats]
    def __init__(self, playersStats: _Optional[_Iterable[_Union[PlayerStats, _Mapping]]] = ...) -> None: ...

class GetStatsRequest(_message.Message):
    __slots__ = ["apiNames", "gpid"]
    APINAMES_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    apiNames: _containers.RepeatedScalarFieldContainer[str]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ..., apiNames: _Optional[_Iterable[str]] = ...) -> None: ...

class GetStatsResponse(_message.Message):
    __slots__ = ["stats"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: Stats
    def __init__(self, stats: _Optional[_Union[Stats, _Mapping]] = ...) -> None: ...

class OnStatsUpdatedEvent(_message.Message):
    __slots__ = ["updatedDate", "updatedStats"]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDSTATS_FIELD_NUMBER: _ClassVar[int]
    updatedDate: int
    updatedStats: _containers.RepeatedCompositeFieldContainer[PlayerStat]
    def __init__(self, updatedStats: _Optional[_Iterable[_Union[PlayerStat, _Mapping]]] = ..., updatedDate: _Optional[int] = ...) -> None: ...

class PlayerStat(_message.Message):
    __slots__ = ["floatValue", "intValue", "longValue", "name", "type", "window"]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    floatValue: float
    intValue: int
    longValue: int
    name: str
    type: _stats_message_pb2.StatDefType
    window: float
    def __init__(self, name: _Optional[str] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., window: _Optional[float] = ..., type: _Optional[_Union[_stats_message_pb2.StatDefType, str]] = ..., longValue: _Optional[int] = ...) -> None: ...

class PlayerStats(_message.Message):
    __slots__ = ["gpid", "stats"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    stats: Stats
    def __init__(self, gpid: _Optional[str] = ..., stats: _Optional[_Union[Stats, _Mapping]] = ...) -> None: ...

class ResetStatsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResetStatsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Stats(_message.Message):
    __slots__ = ["seasonId", "stat", "updatedDate"]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    STAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    seasonId: str
    stat: _containers.RepeatedCompositeFieldContainer[PlayerStat]
    updatedDate: int
    def __init__(self, stat: _Optional[_Iterable[_Union[PlayerStat, _Mapping]]] = ..., seasonId: _Optional[str] = ..., updatedDate: _Optional[int] = ...) -> None: ...

class StorePlayerStat(_message.Message):
    __slots__ = ["name", "storeFloat", "storeInt", "storeLong"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STOREFLOAT_FIELD_NUMBER: _ClassVar[int]
    STOREINT_FIELD_NUMBER: _ClassVar[int]
    STORELONG_FIELD_NUMBER: _ClassVar[int]
    name: str
    storeFloat: float
    storeInt: int
    storeLong: int
    def __init__(self, name: _Optional[str] = ..., storeInt: _Optional[int] = ..., storeFloat: _Optional[float] = ..., storeLong: _Optional[int] = ...) -> None: ...

class StorePlayerStats(_message.Message):
    __slots__ = ["gpid", "seasonId", "stats"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    seasonId: str
    stats: _containers.RepeatedCompositeFieldContainer[StorePlayerStat]
    def __init__(self, gpid: _Optional[str] = ..., stats: _Optional[_Iterable[_Union[StorePlayerStat, _Mapping]]] = ..., seasonId: _Optional[str] = ...) -> None: ...

class StorePlayerStatsRequest(_message.Message):
    __slots__ = ["storePlayerStats"]
    STOREPLAYERSTATS_FIELD_NUMBER: _ClassVar[int]
    storePlayerStats: StorePlayerStats
    def __init__(self, storePlayerStats: _Optional[_Union[StorePlayerStats, _Mapping]] = ...) -> None: ...

class StorePlayerStatsResponse(_message.Message):
    __slots__ = ["gpid", "updatedDate"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    updatedDate: int
    def __init__(self, gpid: _Optional[str] = ..., updatedDate: _Optional[int] = ...) -> None: ...

class StorePlayersStatsRequest(_message.Message):
    __slots__ = ["storePlayersStats"]
    STOREPLAYERSSTATS_FIELD_NUMBER: _ClassVar[int]
    storePlayersStats: _containers.RepeatedCompositeFieldContainer[StorePlayerStats]
    def __init__(self, storePlayersStats: _Optional[_Iterable[_Union[StorePlayerStats, _Mapping]]] = ...) -> None: ...

class StorePlayersStatsResponse(_message.Message):
    __slots__ = ["storePlayerStatsResponse"]
    STOREPLAYERSTATSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    storePlayerStatsResponse: _containers.RepeatedCompositeFieldContainer[StorePlayerStatsResponse]
    def __init__(self, storePlayerStatsResponse: _Optional[_Iterable[_Union[StorePlayerStatsResponse, _Mapping]]] = ...) -> None: ...

class StoreStatsRequest(_message.Message):
    __slots__ = ["stats"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[StorePlayerStats]
    def __init__(self, stats: _Optional[_Iterable[_Union[StorePlayerStats, _Mapping]]] = ...) -> None: ...

class StoreStatsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
