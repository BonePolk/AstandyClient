from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
blue: Side
canceled: State
finished: State
preparing: State
ready: State
red: Side
started: State

class AnnounceTournamentRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AnnounceTournamentResponse(_message.Message):
    __slots__ = ["tournament"]
    TOURNAMENT_FIELD_NUMBER: _ClassVar[int]
    tournament: Tournament
    def __init__(self, tournament: _Optional[_Union[Tournament, _Mapping]] = ...) -> None: ...

class FinishTournamentRequest(_message.Message):
    __slots__ = ["gameId", "tournamentId", "winner"]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENTID_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    tournamentId: str
    winner: Side
    def __init__(self, tournamentId: _Optional[str] = ..., gameId: _Optional[str] = ..., winner: _Optional[_Union[Side, str]] = ...) -> None: ...

class FinishTournamentResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetTournamentRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetTournamentResponse(_message.Message):
    __slots__ = ["tournament"]
    TOURNAMENT_FIELD_NUMBER: _ClassVar[int]
    tournament: Tournament
    def __init__(self, tournament: _Optional[_Union[Tournament, _Mapping]] = ...) -> None: ...

class JoinTournamentRequest(_message.Message):
    __slots__ = ["team", "tournamentId"]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    TOURNAMENTID_FIELD_NUMBER: _ClassVar[int]
    team: Team
    tournamentId: str
    def __init__(self, tournamentId: _Optional[str] = ..., team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class JoinTournamentResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LeaveTournamentRequest(_message.Message):
    __slots__ = ["tournamentId"]
    TOURNAMENTID_FIELD_NUMBER: _ClassVar[int]
    tournamentId: str
    def __init__(self, tournamentId: _Optional[str] = ...) -> None: ...

class LeaveTournamentResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PlayTournamentGameRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PlayTournamentGameResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartTournamentRequest(_message.Message):
    __slots__ = ["tournamentId"]
    TOURNAMENTID_FIELD_NUMBER: _ClassVar[int]
    tournamentId: str
    def __init__(self, tournamentId: _Optional[str] = ...) -> None: ...

class StartTournamentResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Team(_message.Message):
    __slots__ = ["gpid", "gpids", "name"]
    GPIDS_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    gpids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    def __init__(self, name: _Optional[str] = ..., gpid: _Optional[str] = ..., gpids: _Optional[_Iterable[str]] = ...) -> None: ...

class Tournament(_message.Message):
    __slots__ = ["date", "downloadUrl", "minGameVersion", "name", "version"]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURL_FIELD_NUMBER: _ClassVar[int]
    MINGAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    date: int
    downloadUrl: str
    minGameVersion: str
    name: str
    version: int
    def __init__(self, name: _Optional[str] = ..., version: _Optional[int] = ..., minGameVersion: _Optional[str] = ..., downloadUrl: _Optional[str] = ..., date: _Optional[int] = ...) -> None: ...

class TournamentsRequest(_message.Message):
    __slots__ = ["state"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: State
    def __init__(self, state: _Optional[_Union[State, str]] = ...) -> None: ...

class TournamentsResponse(_message.Message):
    __slots__ = ["tournaments"]
    TOURNAMENTS_FIELD_NUMBER: _ClassVar[int]
    tournaments: _containers.RepeatedCompositeFieldContainer[Tournament]
    def __init__(self, tournaments: _Optional[_Iterable[_Union[Tournament, _Mapping]]] = ...) -> None: ...

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Side(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
