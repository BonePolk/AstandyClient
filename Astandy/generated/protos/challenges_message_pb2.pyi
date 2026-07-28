import common_message_pb2 as _common_message_pb2
import inventory_message_pb2 as _inventory_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChallengeDefinition(_message.Message):
    __slots__ = ["action", "code", "dayRange", "eventPoints", "gameEventChallengeId", "gameEventId", "keyItemDefinitionId", "localizedTitle", "reward", "targetPoints", "type"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DAYRANGE_FIELD_NUMBER: _ClassVar[int]
    EVENTPOINTS_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTCHALLENGEID_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    KEYITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZEDTITLE_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    TARGETPOINTS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    action: str
    code: str
    dayRange: _common_message_pb2.DayRange
    eventPoints: int
    gameEventChallengeId: str
    gameEventId: str
    keyItemDefinitionId: int
    localizedTitle: _common_message_pb2.LocalizedTitle
    reward: _inventory_message_pb2.RewardInfo
    targetPoints: int
    type: str
    def __init__(self, gameEventChallengeId: _Optional[str] = ..., gameEventId: _Optional[str] = ..., code: _Optional[str] = ..., keyItemDefinitionId: _Optional[int] = ..., localizedTitle: _Optional[_Union[_common_message_pb2.LocalizedTitle, _Mapping]] = ..., action: _Optional[str] = ..., dayRange: _Optional[_Union[_common_message_pb2.DayRange, _Mapping]] = ..., type: _Optional[str] = ..., eventPoints: _Optional[int] = ..., targetPoints: _Optional[int] = ..., reward: _Optional[_Union[_inventory_message_pb2.RewardInfo, _Mapping]] = ...) -> None: ...

class ChallengeProgress(_message.Message):
    __slots__ = ["completed", "gameEventChallengeProgressId", "id", "points", "rewardsObtained"]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTCHALLENGEPROGRESSID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    REWARDSOBTAINED_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    gameEventChallengeProgressId: str
    id: str
    points: int
    rewardsObtained: bool
    def __init__(self, id: _Optional[str] = ..., points: _Optional[int] = ..., completed: bool = ..., rewardsObtained: bool = ..., gameEventChallengeProgressId: _Optional[str] = ...) -> None: ...

class CurrentChallenge(_message.Message):
    __slots__ = ["action", "code", "completed", "currentPoints", "dayRange", "eventPoints", "gameEventChallengeId", "gameEventChallengeProgressId", "gameEventId", "keyItemDefinitionId", "localizedTitle", "reward", "rewardsObtained", "targetPoints", "type"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    CURRENTPOINTS_FIELD_NUMBER: _ClassVar[int]
    DAYRANGE_FIELD_NUMBER: _ClassVar[int]
    EVENTPOINTS_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTCHALLENGEID_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTCHALLENGEPROGRESSID_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    KEYITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZEDTITLE_FIELD_NUMBER: _ClassVar[int]
    REWARDSOBTAINED_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    TARGETPOINTS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    action: str
    code: str
    completed: bool
    currentPoints: int
    dayRange: _common_message_pb2.DayRange
    eventPoints: int
    gameEventChallengeId: str
    gameEventChallengeProgressId: str
    gameEventId: str
    keyItemDefinitionId: int
    localizedTitle: _common_message_pb2.LocalizedTitle
    reward: _inventory_message_pb2.RewardInfo
    rewardsObtained: bool
    targetPoints: int
    type: str
    def __init__(self, gameEventChallengeId: _Optional[str] = ..., code: _Optional[str] = ..., keyItemDefinitionId: _Optional[int] = ..., localizedTitle: _Optional[_Union[_common_message_pb2.LocalizedTitle, _Mapping]] = ..., action: _Optional[str] = ..., dayRange: _Optional[_Union[_common_message_pb2.DayRange, _Mapping]] = ..., type: _Optional[str] = ..., eventPoints: _Optional[int] = ..., targetPoints: _Optional[int] = ..., currentPoints: _Optional[int] = ..., reward: _Optional[_Union[_inventory_message_pb2.RewardInfo, _Mapping]] = ..., completed: bool = ..., gameEventId: _Optional[str] = ..., rewardsObtained: bool = ..., gameEventChallengeProgressId: _Optional[str] = ...) -> None: ...

class GetAllChallengesRequest(_message.Message):
    __slots__ = ["gameEventId"]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    gameEventId: str
    def __init__(self, gameEventId: _Optional[str] = ...) -> None: ...

class GetAllChallengesResponse(_message.Message):
    __slots__ = ["challenges"]
    CHALLENGES_FIELD_NUMBER: _ClassVar[int]
    challenges: _containers.RepeatedCompositeFieldContainer[CurrentChallenge]
    def __init__(self, challenges: _Optional[_Iterable[_Union[CurrentChallenge, _Mapping]]] = ...) -> None: ...

class GetCurrentChallengesRequest(_message.Message):
    __slots__ = ["completed", "gameEventId"]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    gameEventId: str
    def __init__(self, gameEventId: _Optional[str] = ..., completed: bool = ...) -> None: ...

class GetCurrentChallengesResponse(_message.Message):
    __slots__ = ["challenges"]
    CHALLENGES_FIELD_NUMBER: _ClassVar[int]
    challenges: _containers.RepeatedCompositeFieldContainer[CurrentChallenge]
    def __init__(self, challenges: _Optional[_Iterable[_Union[CurrentChallenge, _Mapping]]] = ...) -> None: ...

class ListOfLevelsToClaimReward(_message.Message):
    __slots__ = ["levels"]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, levels: _Optional[_Iterable[int]] = ...) -> None: ...

class OnProgressChallengeEvent(_message.Message):
    __slots__ = ["challengeCompleted", "challengePoints", "challengeReward", "challengeRewardsObtained", "eventLevels", "eventPoints", "eventReward", "gameEventChallengeId", "gameEventChallengeProgressId", "gameEventId", "levelsToClaimReward"]
    class EventLevelsEntry(_message.Message):
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
        value: ListOfLevelsToClaimReward
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ListOfLevelsToClaimReward, _Mapping]] = ...) -> None: ...
    CHALLENGECOMPLETED_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEPOINTS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEREWARDSOBTAINED_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEREWARD_FIELD_NUMBER: _ClassVar[int]
    EVENTLEVELS_FIELD_NUMBER: _ClassVar[int]
    EVENTPOINTS_FIELD_NUMBER: _ClassVar[int]
    EVENTREWARD_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTCHALLENGEID_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTCHALLENGEPROGRESSID_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    challengeCompleted: bool
    challengePoints: int
    challengeReward: _inventory_message_pb2.GivenReward
    challengeRewardsObtained: bool
    eventLevels: _containers.ScalarMap[str, int]
    eventPoints: int
    eventReward: _inventory_message_pb2.GivenReward
    gameEventChallengeId: str
    gameEventChallengeProgressId: str
    gameEventId: str
    levelsToClaimReward: _containers.MessageMap[str, ListOfLevelsToClaimReward]
    def __init__(self, gameEventChallengeId: _Optional[str] = ..., challengeCompleted: bool = ..., challengePoints: _Optional[int] = ..., challengeReward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ..., gameEventId: _Optional[str] = ..., eventPoints: _Optional[int] = ..., eventLevels: _Optional[_Mapping[str, int]] = ..., eventReward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ..., levelsToClaimReward: _Optional[_Mapping[str, ListOfLevelsToClaimReward]] = ..., challengeRewardsObtained: bool = ..., gameEventChallengeProgressId: _Optional[str] = ...) -> None: ...

class ProgressChallengeByServerRequest(_message.Message):
    __slots__ = ["gameEventChallengeId", "gameEventChallengeProgressId", "gpid", "points"]
    GAMEEVENTCHALLENGEID_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTCHALLENGEPROGRESSID_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    gameEventChallengeId: str
    gameEventChallengeProgressId: str
    gpid: str
    points: int
    def __init__(self, gameEventChallengeId: _Optional[str] = ..., points: _Optional[int] = ..., gpid: _Optional[str] = ..., gameEventChallengeProgressId: _Optional[str] = ...) -> None: ...

class ProgressChallengeByServerResponse(_message.Message):
    __slots__ = ["challengePoints", "challengeReward", "completed", "eventGamePassLevels", "eventPoints", "eventReward"]
    class EventGamePassLevelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    CHALLENGEPOINTS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEREWARD_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    EVENTGAMEPASSLEVELS_FIELD_NUMBER: _ClassVar[int]
    EVENTPOINTS_FIELD_NUMBER: _ClassVar[int]
    EVENTREWARD_FIELD_NUMBER: _ClassVar[int]
    challengePoints: int
    challengeReward: _inventory_message_pb2.GivenReward
    completed: bool
    eventGamePassLevels: _containers.ScalarMap[str, int]
    eventPoints: int
    eventReward: _inventory_message_pb2.GivenReward
    def __init__(self, completed: bool = ..., challengePoints: _Optional[int] = ..., challengeReward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ..., eventPoints: _Optional[int] = ..., eventGamePassLevels: _Optional[_Mapping[str, int]] = ..., eventReward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ...) -> None: ...

class ProgressChallengeRequest(_message.Message):
    __slots__ = ["gameEventChallengeId", "gameEventChallengeProgressId", "points"]
    GAMEEVENTCHALLENGEID_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTCHALLENGEPROGRESSID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    gameEventChallengeId: str
    gameEventChallengeProgressId: str
    points: int
    def __init__(self, gameEventChallengeId: _Optional[str] = ..., points: _Optional[int] = ..., gameEventChallengeProgressId: _Optional[str] = ...) -> None: ...

class ProgressChallengeResponse(_message.Message):
    __slots__ = ["challengePoints", "challengeReward", "completed", "eventGamePassLevels", "eventPoints", "eventReward", "rewardsObtained"]
    class EventGamePassLevelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    CHALLENGEPOINTS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEREWARD_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    EVENTGAMEPASSLEVELS_FIELD_NUMBER: _ClassVar[int]
    EVENTPOINTS_FIELD_NUMBER: _ClassVar[int]
    EVENTREWARD_FIELD_NUMBER: _ClassVar[int]
    REWARDSOBTAINED_FIELD_NUMBER: _ClassVar[int]
    challengePoints: int
    challengeReward: _inventory_message_pb2.GivenReward
    completed: bool
    eventGamePassLevels: _containers.ScalarMap[str, int]
    eventPoints: int
    eventReward: _inventory_message_pb2.GivenReward
    rewardsObtained: bool
    def __init__(self, completed: bool = ..., challengePoints: _Optional[int] = ..., challengeReward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ..., eventPoints: _Optional[int] = ..., eventGamePassLevels: _Optional[_Mapping[str, int]] = ..., eventReward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ..., rewardsObtained: bool = ...) -> None: ...

class ProgressChallengesByServerIncRequest(_message.Message):
    __slots__ = ["requests"]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[ProgressChallengeByServerRequest]
    def __init__(self, requests: _Optional[_Iterable[_Union[ProgressChallengeByServerRequest, _Mapping]]] = ...) -> None: ...

class ProgressChallengesByServerIncResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ProgressChallengesByServerResult]
    def __init__(self, results: _Optional[_Iterable[_Union[ProgressChallengesByServerResult, _Mapping]]] = ...) -> None: ...

class ProgressChallengesByServerRequest(_message.Message):
    __slots__ = ["requests"]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[ProgressChallengeByServerRequest]
    def __init__(self, requests: _Optional[_Iterable[_Union[ProgressChallengeByServerRequest, _Mapping]]] = ...) -> None: ...

class ProgressChallengesByServerResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ProgressChallengesByServerResult]
    def __init__(self, results: _Optional[_Iterable[_Union[ProgressChallengesByServerResult, _Mapping]]] = ...) -> None: ...

class ProgressChallengesByServerResult(_message.Message):
    __slots__ = ["gameEventChallengeId", "gameEventChallengeProgressId", "gpid", "result", "success"]
    GAMEEVENTCHALLENGEID_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTCHALLENGEPROGRESSID_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    gameEventChallengeId: str
    gameEventChallengeProgressId: str
    gpid: str
    result: ProgressChallengeByServerResponse
    success: bool
    def __init__(self, gpid: _Optional[str] = ..., success: bool = ..., result: _Optional[_Union[ProgressChallengeByServerResponse, _Mapping]] = ..., gameEventChallengeId: _Optional[str] = ..., gameEventChallengeProgressId: _Optional[str] = ...) -> None: ...

class SaveChallengeDefinition2Request(_message.Message):
    __slots__ = ["action", "code", "targetPoints"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TARGETPOINTS_FIELD_NUMBER: _ClassVar[int]
    action: str
    code: str
    targetPoints: int
    def __init__(self, code: _Optional[str] = ..., action: _Optional[str] = ..., targetPoints: _Optional[int] = ...) -> None: ...

class SaveChallengeDefinition2Response(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
