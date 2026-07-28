import common_message_pb2 as _common_message_pb2
import player_stats_message_pb2 as _player_stats_message_pb2
import clan_stats_message_pb2 as _clan_stats_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ANNULLED: MatchState
CANCELED: MatchState
CLAN_BATTLE: MatchType
DESCRIPTOR: _descriptor.FileDescriptor
FINISHED: MatchState
REGULAR: MatchType

class FinishMatchRequest(_message.Message):
    __slots__ = ["match"]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    match: FinishedMatch
    def __init__(self, match: _Optional[_Union[FinishedMatch, _Mapping]] = ...) -> None: ...

class FinishMatchResponse(_message.Message):
    __slots__ = ["matchId"]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    matchId: str
    def __init__(self, matchId: _Optional[str] = ...) -> None: ...

class FinishedMatch(_message.Message):
    __slots__ = ["clans", "creatorGpid", "finishDate", "matchId", "matchType", "players", "properties", "region", "seasonId", "startDate", "state", "version"]
    CLANS_FIELD_NUMBER: _ClassVar[int]
    CREATORGPID_FIELD_NUMBER: _ClassVar[int]
    FINISHDATE_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    MATCHTYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    STARTDATE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    clans: _containers.RepeatedCompositeFieldContainer[MatchClan]
    creatorGpid: str
    finishDate: int
    matchId: str
    matchType: MatchType
    players: _containers.RepeatedCompositeFieldContainer[MatchPlayer]
    properties: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    region: str
    seasonId: str
    startDate: int
    state: MatchState
    version: str
    def __init__(self, matchId: _Optional[str] = ..., matchType: _Optional[_Union[MatchType, str]] = ..., creatorGpid: _Optional[str] = ..., region: _Optional[str] = ..., version: _Optional[str] = ..., startDate: _Optional[int] = ..., finishDate: _Optional[int] = ..., seasonId: _Optional[str] = ..., state: _Optional[_Union[MatchState, str]] = ..., properties: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ..., players: _Optional[_Iterable[_Union[MatchPlayer, _Mapping]]] = ..., clans: _Optional[_Iterable[_Union[MatchClan, _Mapping]]] = ...) -> None: ...

class GetClanMatchesRequest(_message.Message):
    __slots__ = ["clanId", "filterProperties", "offset"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    FILTERPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    filterProperties: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    offset: _common_message_pb2.Offset
    def __init__(self, clanId: _Optional[str] = ..., offset: _Optional[_Union[_common_message_pb2.Offset, _Mapping]] = ..., filterProperties: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ...) -> None: ...

class GetClanMatchesResponse(_message.Message):
    __slots__ = ["matches"]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[FinishedMatch]
    def __init__(self, matches: _Optional[_Iterable[_Union[FinishedMatch, _Mapping]]] = ...) -> None: ...

class GetCurrentPlayerLastMatchRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCurrentPlayerLastMatchResponse(_message.Message):
    __slots__ = ["clanMatch", "playerMatch"]
    CLANMATCH_FIELD_NUMBER: _ClassVar[int]
    PLAYERMATCH_FIELD_NUMBER: _ClassVar[int]
    clanMatch: FinishedMatch
    playerMatch: FinishedMatch
    def __init__(self, playerMatch: _Optional[_Union[FinishedMatch, _Mapping]] = ..., clanMatch: _Optional[_Union[FinishedMatch, _Mapping]] = ...) -> None: ...

class GetMatchRequest(_message.Message):
    __slots__ = ["matchId"]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    matchId: str
    def __init__(self, matchId: _Optional[str] = ...) -> None: ...

class GetMatchResponse(_message.Message):
    __slots__ = ["match"]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    match: FinishedMatch
    def __init__(self, match: _Optional[_Union[FinishedMatch, _Mapping]] = ...) -> None: ...

class GetPlayerLastMatchRequest(_message.Message):
    __slots__ = ["gpid"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class GetPlayerLastMatchResponse(_message.Message):
    __slots__ = ["match"]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    match: FinishedMatch
    def __init__(self, match: _Optional[_Union[FinishedMatch, _Mapping]] = ...) -> None: ...

class GetPlayerMatchesRequest(_message.Message):
    __slots__ = ["filterProperties", "gpid", "offset"]
    FILTERPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filterProperties: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    gpid: str
    offset: _common_message_pb2.Offset
    def __init__(self, gpid: _Optional[str] = ..., offset: _Optional[_Union[_common_message_pb2.Offset, _Mapping]] = ..., filterProperties: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ...) -> None: ...

class GetPlayerMatchesResponse(_message.Message):
    __slots__ = ["matches"]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[FinishedMatch]
    def __init__(self, matches: _Optional[_Iterable[_Union[FinishedMatch, _Mapping]]] = ...) -> None: ...

class MatchClan(_message.Message):
    __slots__ = ["avatarId", "clanId", "clanName", "clanTag", "players", "properties", "reward"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CLANNAME_FIELD_NUMBER: _ClassVar[int]
    CLANTAG_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    clanId: str
    clanName: str
    clanTag: str
    players: _containers.RepeatedCompositeFieldContainer[MatchPlayer]
    properties: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    reward: MatchClanReward
    def __init__(self, clanId: _Optional[str] = ..., clanName: _Optional[str] = ..., clanTag: _Optional[str] = ..., avatarId: _Optional[str] = ..., players: _Optional[_Iterable[_Union[MatchPlayer, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ..., reward: _Optional[_Union[MatchClanReward, _Mapping]] = ...) -> None: ...

class MatchClanReward(_message.Message):
    __slots__ = ["stats"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _clan_stats_message_pb2.ClanStats
    def __init__(self, stats: _Optional[_Union[_clan_stats_message_pb2.ClanStats, _Mapping]] = ...) -> None: ...

class MatchPlayer(_message.Message):
    __slots__ = ["avatarId", "deleted", "gpid", "name", "properties", "reward", "uid"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    deleted: bool
    gpid: str
    name: str
    properties: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    reward: MatchPlayerReward
    uid: str
    def __init__(self, gpid: _Optional[str] = ..., uid: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ..., reward: _Optional[_Union[MatchPlayerReward, _Mapping]] = ..., deleted: bool = ...) -> None: ...

class MatchPlayerReward(_message.Message):
    __slots__ = ["stats"]
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[_player_stats_message_pb2.PlayerStat]
    def __init__(self, stats: _Optional[_Iterable[_Union[_player_stats_message_pb2.PlayerStat, _Mapping]]] = ...) -> None: ...

class OnMatchFinishedEvent(_message.Message):
    __slots__ = ["match"]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    match: FinishedMatch
    def __init__(self, match: _Optional[_Union[FinishedMatch, _Mapping]] = ...) -> None: ...

class MatchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
