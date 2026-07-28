import common_message_pb2 as _common_message_pb2
import inventory_message_pb2 as _inventory_message_pb2
import challenges_message_pb2 as _challenges_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
EventPointsBought: ProgressGameEventType
GamePassAndEventPointsBought: ProgressGameEventType
GamePassBought: ProgressGameEventType
ReferralPointsReceived: ProgressGameEventType
Unspecified: ProgressGameEventType

class ClaimAllRewardsOfSpecificPasses(_message.Message):
    __slots__ = ["gameEventId", "passId"]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    PASSID_FIELD_NUMBER: _ClassVar[int]
    gameEventId: str
    passId: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gameEventId: _Optional[str] = ..., passId: _Optional[_Iterable[str]] = ...) -> None: ...

class ClaimRewardsResponse(_message.Message):
    __slots__ = ["reward"]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: _inventory_message_pb2.GivenReward
    def __init__(self, reward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ...) -> None: ...

class ClaimSpecificLevelRewardRequest(_message.Message):
    __slots__ = ["gameEventId", "level", "passId"]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PASSID_FIELD_NUMBER: _ClassVar[int]
    gameEventId: str
    level: int
    passId: str
    def __init__(self, gameEventId: _Optional[str] = ..., passId: _Optional[str] = ..., level: _Optional[int] = ...) -> None: ...

class CurrentGameEvent(_message.Message):
    __slots__ = ["action", "code", "currentDay", "dateSince", "dateUntil", "durationDays", "gamePasses", "id", "isProgressShared", "points", "settings", "title"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CURRENTDAY_FIELD_NUMBER: _ClassVar[int]
    DATESINCE_FIELD_NUMBER: _ClassVar[int]
    DATEUNTIL_FIELD_NUMBER: _ClassVar[int]
    DURATIONDAYS_FIELD_NUMBER: _ClassVar[int]
    GAMEPASSES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISPROGRESSSHARED_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    action: str
    code: str
    currentDay: int
    dateSince: int
    dateUntil: int
    durationDays: int
    gamePasses: _containers.RepeatedCompositeFieldContainer[GamePass]
    id: str
    isProgressShared: bool
    points: int
    settings: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    title: _common_message_pb2.LocalizedTitle
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., dateSince: _Optional[int] = ..., dateUntil: _Optional[int] = ..., durationDays: _Optional[int] = ..., gamePasses: _Optional[_Iterable[_Union[GamePass, _Mapping]]] = ..., points: _Optional[int] = ..., currentDay: _Optional[int] = ..., settings: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ..., title: _Optional[_Union[_common_message_pb2.LocalizedTitle, _Mapping]] = ..., action: _Optional[str] = ..., isProgressShared: bool = ...) -> None: ...

class GameEventDefinition(_message.Message):
    __slots__ = ["action", "challenges", "code", "dateSince", "dateUntil", "durationDays", "gamePasses", "id", "isProgressShared", "settings", "title"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CHALLENGES_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATESINCE_FIELD_NUMBER: _ClassVar[int]
    DATEUNTIL_FIELD_NUMBER: _ClassVar[int]
    DURATIONDAYS_FIELD_NUMBER: _ClassVar[int]
    GAMEPASSES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISPROGRESSSHARED_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    action: str
    challenges: _containers.RepeatedCompositeFieldContainer[_challenges_message_pb2.ChallengeDefinition]
    code: str
    dateSince: int
    dateUntil: int
    durationDays: int
    gamePasses: _containers.RepeatedCompositeFieldContainer[GamePassDefinition]
    id: str
    isProgressShared: bool
    settings: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    title: _common_message_pb2.LocalizedTitle
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., dateSince: _Optional[int] = ..., dateUntil: _Optional[int] = ..., durationDays: _Optional[int] = ..., gamePasses: _Optional[_Iterable[_Union[GamePassDefinition, _Mapping]]] = ..., challenges: _Optional[_Iterable[_Union[_challenges_message_pb2.ChallengeDefinition, _Mapping]]] = ..., settings: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ..., title: _Optional[_Union[_common_message_pb2.LocalizedTitle, _Mapping]] = ..., action: _Optional[str] = ..., isProgressShared: bool = ...) -> None: ...

class GameEventProgress(_message.Message):
    __slots__ = ["challengeProgresses", "currentDay", "gamePassProgresses", "id", "points"]
    CHALLENGEPROGRESSES_FIELD_NUMBER: _ClassVar[int]
    CURRENTDAY_FIELD_NUMBER: _ClassVar[int]
    GAMEPASSPROGRESSES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    challengeProgresses: _containers.RepeatedCompositeFieldContainer[_challenges_message_pb2.ChallengeProgress]
    currentDay: int
    gamePassProgresses: _containers.RepeatedCompositeFieldContainer[GamePassProgress]
    id: str
    points: int
    def __init__(self, id: _Optional[str] = ..., points: _Optional[int] = ..., gamePassProgresses: _Optional[_Iterable[_Union[GamePassProgress, _Mapping]]] = ..., challengeProgresses: _Optional[_Iterable[_Union[_challenges_message_pb2.ChallengeProgress, _Mapping]]] = ..., currentDay: _Optional[int] = ...) -> None: ...

class GamePass(_message.Message):
    __slots__ = ["code", "currentLevel", "id", "keyItemDefinitionId", "levels", "levelsToClaimReward"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CURRENTLEVEL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEYITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    code: str
    currentLevel: int
    id: str
    keyItemDefinitionId: int
    levels: _containers.RepeatedCompositeFieldContainer[GamePassLevel]
    levelsToClaimReward: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., keyItemDefinitionId: _Optional[int] = ..., levels: _Optional[_Iterable[_Union[GamePassLevel, _Mapping]]] = ..., currentLevel: _Optional[int] = ..., levelsToClaimReward: _Optional[_Iterable[int]] = ...) -> None: ...

class GamePassDefinition(_message.Message):
    __slots__ = ["code", "id", "keyItemDefinitionId", "levels"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEYITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    code: str
    id: str
    keyItemDefinitionId: int
    levels: _containers.RepeatedCompositeFieldContainer[GamePassLevel]
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., keyItemDefinitionId: _Optional[int] = ..., levels: _Optional[_Iterable[_Union[GamePassLevel, _Mapping]]] = ...) -> None: ...

class GamePassLevel(_message.Message):
    __slots__ = ["level", "minPoints", "reoccurringPoints", "reward"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MINPOINTS_FIELD_NUMBER: _ClassVar[int]
    REOCCURRINGPOINTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    level: int
    minPoints: int
    reoccurringPoints: int
    reward: _inventory_message_pb2.RewardInfo
    def __init__(self, level: _Optional[int] = ..., minPoints: _Optional[int] = ..., reward: _Optional[_Union[_inventory_message_pb2.RewardInfo, _Mapping]] = ..., reoccurringPoints: _Optional[int] = ...) -> None: ...

class GamePassProgress(_message.Message):
    __slots__ = ["currentLevel", "id", "levelsToClaimReward"]
    CURRENTLEVEL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    currentLevel: int
    id: str
    levelsToClaimReward: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[str] = ..., currentLevel: _Optional[int] = ..., levelsToClaimReward: _Optional[_Iterable[int]] = ...) -> None: ...

class GetAllChallengesByServerRequest(_message.Message):
    __slots__ = ["gameEventIds"]
    GAMEEVENTIDS_FIELD_NUMBER: _ClassVar[int]
    gameEventIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gameEventIds: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAllChallengesByServerResponse(_message.Message):
    __slots__ = ["challenges"]
    CHALLENGES_FIELD_NUMBER: _ClassVar[int]
    challenges: _containers.RepeatedCompositeFieldContainer[_challenges_message_pb2.CurrentChallenge]
    def __init__(self, challenges: _Optional[_Iterable[_Union[_challenges_message_pb2.CurrentChallenge, _Mapping]]] = ...) -> None: ...

class GetCachedPlayerGameEventsRequest(_message.Message):
    __slots__ = ["lastUpdated"]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    lastUpdated: str
    def __init__(self, lastUpdated: _Optional[str] = ...) -> None: ...

class GetCachedPlayerGameEventsResponse(_message.Message):
    __slots__ = ["gameEvents", "lastUpdated", "msUntilRefresh"]
    GAMEEVENTS_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    MSUNTILREFRESH_FIELD_NUMBER: _ClassVar[int]
    gameEvents: _containers.RepeatedCompositeFieldContainer[GameEventDefinition]
    lastUpdated: str
    msUntilRefresh: int
    def __init__(self, gameEvents: _Optional[_Iterable[_Union[GameEventDefinition, _Mapping]]] = ..., lastUpdated: _Optional[str] = ..., msUntilRefresh: _Optional[int] = ...) -> None: ...

class GetCurrentGameEventsByServerRequest(_message.Message):
    __slots__ = ["gameVersion"]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    gameVersion: str
    def __init__(self, gameVersion: _Optional[str] = ...) -> None: ...

class GetCurrentGameEventsByServerResponse(_message.Message):
    __slots__ = ["gameEvents"]
    GAMEEVENTS_FIELD_NUMBER: _ClassVar[int]
    gameEvents: _containers.RepeatedCompositeFieldContainer[CurrentGameEvent]
    def __init__(self, gameEvents: _Optional[_Iterable[_Union[CurrentGameEvent, _Mapping]]] = ...) -> None: ...

class GetCurrentGameEventsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCurrentGameEventsResponse(_message.Message):
    __slots__ = ["gameEvents"]
    GAMEEVENTS_FIELD_NUMBER: _ClassVar[int]
    gameEvents: _containers.RepeatedCompositeFieldContainer[CurrentGameEvent]
    def __init__(self, gameEvents: _Optional[_Iterable[_Union[CurrentGameEvent, _Mapping]]] = ...) -> None: ...

class GetPlayerCurrentGameEventsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerCurrentGameEventsResponse(_message.Message):
    __slots__ = ["gameEvents", "msUntilRefresh"]
    GAMEEVENTS_FIELD_NUMBER: _ClassVar[int]
    MSUNTILREFRESH_FIELD_NUMBER: _ClassVar[int]
    gameEvents: _containers.RepeatedCompositeFieldContainer[CurrentGameEvent]
    msUntilRefresh: int
    def __init__(self, gameEvents: _Optional[_Iterable[_Union[CurrentGameEvent, _Mapping]]] = ..., msUntilRefresh: _Optional[int] = ...) -> None: ...

class GetPlayerGameEventProgressRequest(_message.Message):
    __slots__ = ["gameEventId"]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    gameEventId: str
    def __init__(self, gameEventId: _Optional[str] = ...) -> None: ...

class GetPlayerGameEventProgressResponse(_message.Message):
    __slots__ = ["gameEventsProgress"]
    GAMEEVENTSPROGRESS_FIELD_NUMBER: _ClassVar[int]
    gameEventsProgress: GameEventProgress
    def __init__(self, gameEventsProgress: _Optional[_Union[GameEventProgress, _Mapping]] = ...) -> None: ...

class GetPlayerGameEventsProgressesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerGameEventsProgressesResponse(_message.Message):
    __slots__ = ["gameEventsProgresses"]
    GAMEEVENTSPROGRESSES_FIELD_NUMBER: _ClassVar[int]
    gameEventsProgresses: _containers.RepeatedCompositeFieldContainer[GameEventProgress]
    def __init__(self, gameEventsProgresses: _Optional[_Iterable[_Union[GameEventProgress, _Mapping]]] = ...) -> None: ...

class OnGamePassChangedEvent(_message.Message):
    __slots__ = ["eventId", "levels", "levelsToClaimReward", "points", "reward"]
    class LevelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LevelsToClaimRewardEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _challenges_message_pb2.ListOfLevelsToClaimReward
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_challenges_message_pb2.ListOfLevelsToClaimReward, _Mapping]] = ...) -> None: ...
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    eventId: str
    levels: _containers.ScalarMap[str, int]
    levelsToClaimReward: _containers.MessageMap[str, _challenges_message_pb2.ListOfLevelsToClaimReward]
    points: int
    reward: _inventory_message_pb2.GivenReward
    def __init__(self, eventId: _Optional[str] = ..., points: _Optional[int] = ..., levels: _Optional[_Mapping[str, int]] = ..., reward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ..., levelsToClaimReward: _Optional[_Mapping[str, _challenges_message_pb2.ListOfLevelsToClaimReward]] = ...) -> None: ...

class OnProgressGameEvent(_message.Message):
    __slots__ = ["context", "eventId", "levels", "levelsToClaimReward", "points", "reward"]
    class LevelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LevelsToClaimRewardEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _challenges_message_pb2.ListOfLevelsToClaimReward
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_challenges_message_pb2.ListOfLevelsToClaimReward, _Mapping]] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    context: ProgressGameEventContext
    eventId: str
    levels: _containers.ScalarMap[str, int]
    levelsToClaimReward: _containers.MessageMap[str, _challenges_message_pb2.ListOfLevelsToClaimReward]
    points: int
    reward: _inventory_message_pb2.GivenReward
    def __init__(self, eventId: _Optional[str] = ..., points: _Optional[int] = ..., levels: _Optional[_Mapping[str, int]] = ..., reward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ..., context: _Optional[_Union[ProgressGameEventContext, _Mapping]] = ..., levelsToClaimReward: _Optional[_Mapping[str, _challenges_message_pb2.ListOfLevelsToClaimReward]] = ...) -> None: ...

class OnProgressSharedGameEvent(_message.Message):
    __slots__ = ["eventId", "points"]
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    eventId: str
    points: int
    def __init__(self, eventId: _Optional[str] = ..., points: _Optional[int] = ...) -> None: ...

class OnSharedGameEventLevelAchieved(_message.Message):
    __slots__ = ["eventId", "levels", "levelsToClaimReward", "points"]
    class LevelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LevelsToClaimRewardEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _challenges_message_pb2.ListOfLevelsToClaimReward
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_challenges_message_pb2.ListOfLevelsToClaimReward, _Mapping]] = ...) -> None: ...
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    eventId: str
    levels: _containers.ScalarMap[str, int]
    levelsToClaimReward: _containers.MessageMap[str, _challenges_message_pb2.ListOfLevelsToClaimReward]
    points: int
    def __init__(self, eventId: _Optional[str] = ..., points: _Optional[int] = ..., levels: _Optional[_Mapping[str, int]] = ..., levelsToClaimReward: _Optional[_Mapping[str, _challenges_message_pb2.ListOfLevelsToClaimReward]] = ...) -> None: ...

class ProgressGameEventByServerRequest(_message.Message):
    __slots__ = ["gameEventId", "gpid", "points"]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    gameEventId: str
    gpid: str
    points: int
    def __init__(self, gpid: _Optional[str] = ..., gameEventId: _Optional[str] = ..., points: _Optional[int] = ...) -> None: ...

class ProgressGameEventByServerResponse(_message.Message):
    __slots__ = ["levels", "points", "reward"]
    class LevelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.ScalarMap[str, int]
    points: int
    reward: _inventory_message_pb2.GivenReward
    def __init__(self, points: _Optional[int] = ..., levels: _Optional[_Mapping[str, int]] = ..., reward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ...) -> None: ...

class ProgressGameEventContext(_message.Message):
    __slots__ = ["type"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ProgressGameEventType
    def __init__(self, type: _Optional[_Union[ProgressGameEventType, str]] = ...) -> None: ...

class ProgressGameEventRequest(_message.Message):
    __slots__ = ["gameEventId", "points"]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    gameEventId: str
    points: int
    def __init__(self, gameEventId: _Optional[str] = ..., points: _Optional[int] = ...) -> None: ...

class ProgressGameEventResponse(_message.Message):
    __slots__ = ["levels", "points", "reward"]
    class LevelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.ScalarMap[str, int]
    points: int
    reward: _inventory_message_pb2.GivenReward
    def __init__(self, points: _Optional[int] = ..., levels: _Optional[_Mapping[str, int]] = ..., reward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ...) -> None: ...

class ProgressGameEventsByServerRequest(_message.Message):
    __slots__ = ["requests"]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[ProgressGameEventByServerRequest]
    def __init__(self, requests: _Optional[_Iterable[_Union[ProgressGameEventByServerRequest, _Mapping]]] = ...) -> None: ...

class ProgressGameEventsByServerResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ProgressGameEventsByServerResult]
    def __init__(self, results: _Optional[_Iterable[_Union[ProgressGameEventsByServerResult, _Mapping]]] = ...) -> None: ...

class ProgressGameEventsByServerResult(_message.Message):
    __slots__ = ["gpid", "result", "success"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    result: ProgressGameEventByServerResponse
    success: bool
    def __init__(self, gpid: _Optional[str] = ..., success: bool = ..., result: _Optional[_Union[ProgressGameEventByServerResponse, _Mapping]] = ...) -> None: ...

class ProgressGameEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
