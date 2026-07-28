import clan_stats_message_pb2 as _clan_stats_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CurrentClanMemberStats(_message.Message):
    __slots__ = ["stats"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[_clan_stats_message_pb2.ClanMemberStat]
    def __init__(self, stats: _Optional[_Iterable[_Union[_clan_stats_message_pb2.ClanMemberStat, _Mapping]]] = ...) -> None: ...

class GetClanMembersStatsRequest(_message.Message):
    __slots__ = ["clanId"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    def __init__(self, clanId: _Optional[str] = ...) -> None: ...

class GetClanMembersStatsResponse(_message.Message):
    __slots__ = ["clanId", "clanMembersStats"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSSTATS_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    clanMembersStats: _containers.RepeatedCompositeFieldContainer[_clan_stats_message_pb2.ClanMemberStats]
    def __init__(self, clanId: _Optional[str] = ..., clanMembersStats: _Optional[_Iterable[_Union[_clan_stats_message_pb2.ClanMemberStats, _Mapping]]] = ...) -> None: ...

class GetCurrentClanMemberStatsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCurrentClanMemberStatsResponse(_message.Message):
    __slots__ = ["clanId", "clanMemberStats"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    clanMemberStats: CurrentClanMemberStats
    def __init__(self, clanId: _Optional[str] = ..., clanMemberStats: _Optional[_Union[CurrentClanMemberStats, _Mapping]] = ...) -> None: ...

class SaveCurrentClanMemberStatsRequest(_message.Message):
    __slots__ = ["clanMemberStats"]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    clanMemberStats: CurrentClanMemberStats
    def __init__(self, clanMemberStats: _Optional[_Union[CurrentClanMemberStats, _Mapping]] = ...) -> None: ...

class SaveCurrentClanMemberStatsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
