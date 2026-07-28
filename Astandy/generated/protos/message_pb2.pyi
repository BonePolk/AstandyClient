from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GroupMemberDisconnected: MatchmakingFailCause
GroupMemberIsNotOneClan: MatchmakingFailCause
GroupMemberNotConfirmed: MatchmakingFailCause
GroupMembersMmrDifferenceTooBig: MatchmakingFailCause
GroupWaitTimeout: MatchmakingFailCause
Unknown: MatchmakingFailCause

class Filter(_message.Message):
    __slots__ = ["conditions"]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    conditions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, conditions: _Optional[_Iterable[str]] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ["players"]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[Player]
    def __init__(self, players: _Optional[_Iterable[_Union[Player, _Mapping]]] = ...) -> None: ...

class HandshakeMessage(_message.Message):
    __slots__ = ["ticket"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: str
    def __init__(self, ticket: _Optional[str] = ...) -> None: ...

class HandshakeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MatchGroup(_message.Message):
    __slots__ = ["filterCondition", "region", "teams"]
    FILTERCONDITION_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    filterCondition: str
    region: str
    teams: _containers.RepeatedCompositeFieldContainer[TeamGroup]
    def __init__(self, teams: _Optional[_Iterable[_Union[TeamGroup, _Mapping]]] = ..., filterCondition: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class MatchmakingRequest(_message.Message):
    __slots__ = ["filter", "gameMode", "groupId", "groupSize", "region"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GAMEMODE_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    GROUPSIZE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    filter: Filter
    gameMode: str
    groupId: str
    groupSize: int
    region: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gameMode: _Optional[str] = ..., region: _Optional[_Iterable[str]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ..., groupId: _Optional[str] = ..., groupSize: _Optional[int] = ...) -> None: ...

class OnMatchmakingDoneEvent(_message.Message):
    __slots__ = ["id", "matchGroup"]
    ID_FIELD_NUMBER: _ClassVar[int]
    MATCHGROUP_FIELD_NUMBER: _ClassVar[int]
    id: str
    matchGroup: MatchGroup
    def __init__(self, id: _Optional[str] = ..., matchGroup: _Optional[_Union[MatchGroup, _Mapping]] = ...) -> None: ...

class OnMatchmakingFailEvent(_message.Message):
    __slots__ = ["cause", "group", "message"]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    cause: MatchmakingFailCause
    group: Group
    message: str
    def __init__(self, cause: _Optional[_Union[MatchmakingFailCause, str]] = ..., message: _Optional[str] = ..., group: _Optional[_Union[Group, _Mapping]] = ...) -> None: ...

class OnMatchmakingProgressEvent(_message.Message):
    __slots__ = ["matchGroup", "taskId"]
    MATCHGROUP_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    matchGroup: MatchGroup
    taskId: int
    def __init__(self, taskId: _Optional[int] = ..., matchGroup: _Optional[_Union[MatchGroup, _Mapping]] = ...) -> None: ...

class OnPlayersConfirmedEvent(_message.Message):
    __slots__ = ["matchGroup", "newConfirmedPlayers"]
    MATCHGROUP_FIELD_NUMBER: _ClassVar[int]
    NEWCONFIRMEDPLAYERS_FIELD_NUMBER: _ClassVar[int]
    matchGroup: MatchGroup
    newConfirmedPlayers: _containers.RepeatedCompositeFieldContainer[Player]
    def __init__(self, matchGroup: _Optional[_Union[MatchGroup, _Mapping]] = ..., newConfirmedPlayers: _Optional[_Iterable[_Union[Player, _Mapping]]] = ...) -> None: ...

class Player(_message.Message):
    __slots__ = ["clanId", "confirmed", "id", "name", "online"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    confirmed: bool
    id: str
    name: str
    online: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., online: bool = ..., confirmed: bool = ..., clanId: _Optional[str] = ...) -> None: ...

class TeamGroup(_message.Message):
    __slots__ = ["groups"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    def __init__(self, groups: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...) -> None: ...

class MatchmakingFailCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
