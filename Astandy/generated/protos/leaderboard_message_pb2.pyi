import common_message_pb2 as _common_message_pb2
import player_message_pb2 as _player_message_pb2
import clan_message_pb2 as _clan_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClanLeaderboardEntry(_message.Message):
    __slots__ = ["clan", "diff", "isNew", "percent", "rank", "score"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    ISNEW_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    clan: _clan_message_pb2.Clan
    diff: int
    isNew: bool
    percent: int
    rank: int
    score: int
    def __init__(self, rank: _Optional[int] = ..., percent: _Optional[int] = ..., score: _Optional[int] = ..., diff: _Optional[int] = ..., isNew: bool = ..., clan: _Optional[_Union[_clan_message_pb2.Clan, _Mapping]] = ...) -> None: ...

class GetClanLeaderboardRequest(_message.Message):
    __slots__ = ["leaderboardCode", "offset"]
    LEADERBOARDCODE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    leaderboardCode: str
    offset: _common_message_pb2.Offset
    def __init__(self, leaderboardCode: _Optional[str] = ..., offset: _Optional[_Union[_common_message_pb2.Offset, _Mapping]] = ...) -> None: ...

class GetClanLeaderboardResponse(_message.Message):
    __slots__ = ["clans"]
    CLANS_FIELD_NUMBER: _ClassVar[int]
    clans: _containers.RepeatedCompositeFieldContainer[ClanLeaderboardEntry]
    def __init__(self, clans: _Optional[_Iterable[_Union[ClanLeaderboardEntry, _Mapping]]] = ...) -> None: ...

class GetClanRankRequest(_message.Message):
    __slots__ = ["clanId", "leaderboardCode"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARDCODE_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    leaderboardCode: str
    def __init__(self, leaderboardCode: _Optional[str] = ..., clanId: _Optional[str] = ...) -> None: ...

class GetClanRankResponse(_message.Message):
    __slots__ = ["clan"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: ClanLeaderboardEntry
    def __init__(self, clan: _Optional[_Union[ClanLeaderboardEntry, _Mapping]] = ...) -> None: ...

class GetPlayerLeaderboardRequest(_message.Message):
    __slots__ = ["leaderboardCode", "offset"]
    LEADERBOARDCODE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    leaderboardCode: str
    offset: _common_message_pb2.Offset
    def __init__(self, leaderboardCode: _Optional[str] = ..., offset: _Optional[_Union[_common_message_pb2.Offset, _Mapping]] = ...) -> None: ...

class GetPlayerLeaderboardResponse(_message.Message):
    __slots__ = ["players"]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[PlayerLeaderboardEntry]
    def __init__(self, players: _Optional[_Iterable[_Union[PlayerLeaderboardEntry, _Mapping]]] = ...) -> None: ...

class GetPlayerRankRequest(_message.Message):
    __slots__ = ["gpid", "leaderboardCode"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARDCODE_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    leaderboardCode: str
    def __init__(self, leaderboardCode: _Optional[str] = ..., gpid: _Optional[str] = ...) -> None: ...

class GetPlayerRankResponse(_message.Message):
    __slots__ = ["player"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    player: PlayerLeaderboardEntry
    def __init__(self, player: _Optional[_Union[PlayerLeaderboardEntry, _Mapping]] = ...) -> None: ...

class PlayerLeaderboardEntry(_message.Message):
    __slots__ = ["diff", "isNew", "percent", "player", "rank", "score"]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    ISNEW_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    diff: int
    isNew: bool
    percent: int
    player: _player_message_pb2.Player
    rank: int
    score: int
    def __init__(self, rank: _Optional[int] = ..., percent: _Optional[int] = ..., score: _Optional[int] = ..., diff: _Optional[int] = ..., isNew: bool = ..., player: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ...) -> None: ...
