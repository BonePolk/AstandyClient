import clan_stats_message_pb2 as _clan_stats_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GSGetClanStatsRequest(_message.Message):
    __slots__ = ["clanId", "clanMemberIds", "clanMemberStatIds", "clanStatIds"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERIDS_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATIDS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATIDS_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    clanMemberIds: _containers.RepeatedScalarFieldContainer[str]
    clanMemberStatIds: _containers.RepeatedScalarFieldContainer[str]
    clanStatIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, clanId: _Optional[str] = ..., clanStatIds: _Optional[_Iterable[str]] = ..., clanMemberIds: _Optional[_Iterable[str]] = ..., clanMemberStatIds: _Optional[_Iterable[str]] = ...) -> None: ...

class GSGetClanStatsResponse(_message.Message):
    __slots__ = ["clanMemberStats", "clanStats", "version"]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[_clan_stats_message_pb2.ClanMemberStats]
    clanStats: _clan_stats_message_pb2.ClanStats
    version: int
    def __init__(self, clanStats: _Optional[_Union[_clan_stats_message_pb2.ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[_clan_stats_message_pb2.ClanMemberStats, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class GSSaveClanStatsRequest(_message.Message):
    __slots__ = ["clanMemberStats", "clanStats", "version"]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[_clan_stats_message_pb2.ClanMemberStats]
    clanStats: _clan_stats_message_pb2.ClanStats
    version: int
    def __init__(self, clanStats: _Optional[_Union[_clan_stats_message_pb2.ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[_clan_stats_message_pb2.ClanMemberStats, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class GSSaveClanStatsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
