import player_stats_message_pb2 as _player_stats_message_pb2
import clan_stats_message_pb2 as _clan_stats_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetClanStatsForSeasonRequest(_message.Message):
    __slots__ = ["clanId", "seasonId"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    seasonId: str
    def __init__(self, seasonId: _Optional[str] = ..., clanId: _Optional[str] = ...) -> None: ...

class GetClanStatsForSeasonResponse(_message.Message):
    __slots__ = ["clanMemberStats", "clanStats"]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[_clan_stats_message_pb2.ClanMemberStats]
    clanStats: _clan_stats_message_pb2.ClanStats
    def __init__(self, clanStats: _Optional[_Union[_clan_stats_message_pb2.ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[_clan_stats_message_pb2.ClanMemberStats, _Mapping]]] = ...) -> None: ...

class GetCurrentClanStatsForSeasonRequest(_message.Message):
    __slots__ = ["seasonId"]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    seasonId: str
    def __init__(self, seasonId: _Optional[str] = ...) -> None: ...

class GetCurrentClanStatsForSeasonResponse(_message.Message):
    __slots__ = ["clanMemberStats", "clanStats"]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[_clan_stats_message_pb2.ClanMemberStats]
    clanStats: _clan_stats_message_pb2.ClanStats
    def __init__(self, clanStats: _Optional[_Union[_clan_stats_message_pb2.ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[_clan_stats_message_pb2.ClanMemberStats, _Mapping]]] = ...) -> None: ...

class GetPlayerStatsForSeasonRequest(_message.Message):
    __slots__ = ["gpid", "seasonId"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    seasonId: str
    def __init__(self, seasonId: _Optional[str] = ..., gpid: _Optional[str] = ...) -> None: ...

class GetPlayerStatsForSeasonResponse(_message.Message):
    __slots__ = ["stat"]
    STAT_FIELD_NUMBER: _ClassVar[int]
    stat: _containers.RepeatedCompositeFieldContainer[_player_stats_message_pb2.PlayerStat]
    def __init__(self, stat: _Optional[_Iterable[_Union[_player_stats_message_pb2.PlayerStat, _Mapping]]] = ...) -> None: ...

class GetStatsForSeasonRequest(_message.Message):
    __slots__ = ["seasonId"]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    seasonId: str
    def __init__(self, seasonId: _Optional[str] = ...) -> None: ...

class GetStatsForSeasonResponse(_message.Message):
    __slots__ = ["stat"]
    STAT_FIELD_NUMBER: _ClassVar[int]
    stat: _containers.RepeatedCompositeFieldContainer[_player_stats_message_pb2.PlayerStat]
    def __init__(self, stat: _Optional[_Iterable[_Union[_player_stats_message_pb2.PlayerStat, _Mapping]]] = ...) -> None: ...
