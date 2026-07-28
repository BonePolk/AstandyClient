import stats_message_pb2 as _stats_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClanMemberStat(_message.Message):
    __slots__ = ["floatValue", "intValue", "longValue", "statId", "type"]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    STATID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    floatValue: float
    intValue: int
    longValue: int
    statId: str
    type: _stats_message_pb2.StatDefType
    def __init__(self, statId: _Optional[str] = ..., type: _Optional[_Union[_stats_message_pb2.StatDefType, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., longValue: _Optional[int] = ...) -> None: ...

class ClanMemberStats(_message.Message):
    __slots__ = ["gpid", "stats", "version"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    stats: _containers.RepeatedCompositeFieldContainer[ClanMemberStat]
    version: int
    def __init__(self, gpid: _Optional[str] = ..., stats: _Optional[_Iterable[_Union[ClanMemberStat, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class ClanStat(_message.Message):
    __slots__ = ["floatValue", "intValue", "longValue", "statId", "type"]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    STATID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    floatValue: float
    intValue: int
    longValue: int
    statId: str
    type: _stats_message_pb2.StatDefType
    def __init__(self, type: _Optional[_Union[_stats_message_pb2.StatDefType, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., longValue: _Optional[int] = ..., statId: _Optional[str] = ...) -> None: ...

class ClanStats(_message.Message):
    __slots__ = ["clanId", "seasonId", "stats"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    seasonId: str
    stats: _containers.RepeatedCompositeFieldContainer[ClanStat]
    def __init__(self, clanId: _Optional[str] = ..., stats: _Optional[_Iterable[_Union[ClanStat, _Mapping]]] = ..., seasonId: _Optional[str] = ...) -> None: ...

class ClanStatsMap(_message.Message):
    __slots__ = ["stats"]
    class StatsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClanStat
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClanStat, _Mapping]] = ...) -> None: ...
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.MessageMap[str, ClanStat]
    def __init__(self, stats: _Optional[_Mapping[str, ClanStat]] = ...) -> None: ...

class GetClanStatsRequest(_message.Message):
    __slots__ = ["addLeaderboardStats", "clanId"]
    ADDLEADERBOARDSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    addLeaderboardStats: bool
    clanId: str
    def __init__(self, clanId: _Optional[str] = ..., addLeaderboardStats: bool = ...) -> None: ...

class GetClanStatsResponse(_message.Message):
    __slots__ = ["clanId", "clanMemberStats", "clanStats", "stats"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[ClanMemberStats]
    clanStats: ClanStats
    stats: ClanStatsMap
    def __init__(self, clanId: _Optional[str] = ..., stats: _Optional[_Union[ClanStatsMap, _Mapping]] = ..., clanStats: _Optional[_Union[ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[ClanMemberStats, _Mapping]]] = ...) -> None: ...

class GetCurrentClanStatsRequest(_message.Message):
    __slots__ = ["addLeaderboardStats"]
    ADDLEADERBOARDSTATS_FIELD_NUMBER: _ClassVar[int]
    addLeaderboardStats: bool
    def __init__(self, addLeaderboardStats: bool = ...) -> None: ...

class GetCurrentClanStatsResponse(_message.Message):
    __slots__ = ["clanId", "clanMemberStats", "clanStats", "stats"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[ClanMemberStats]
    clanStats: ClanStats
    stats: ClanStatsMap
    def __init__(self, clanId: _Optional[str] = ..., stats: _Optional[_Union[ClanStatsMap, _Mapping]] = ..., clanStats: _Optional[_Union[ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[ClanMemberStats, _Mapping]]] = ...) -> None: ...

class OnClanStatsUpdatedEvent(_message.Message):
    __slots__ = ["clanMemberStats", "clanStats"]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[ClanMemberStats]
    clanStats: ClanStats
    def __init__(self, clanStats: _Optional[_Union[ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[ClanMemberStats, _Mapping]]] = ...) -> None: ...
