import common_message_pb2 as _common_message_pb2
import inventory_message_pb2 as _inventory_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AchievementDefinition(_message.Message):
    __slots__ = ["id", "imageLocked", "imageUnlocked", "key", "title"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGELOCKED_FIELD_NUMBER: _ClassVar[int]
    IMAGEUNLOCKED_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    imageLocked: str
    imageUnlocked: str
    key: str
    title: _common_message_pb2.LocalizedTitle
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., title: _Optional[_Union[_common_message_pb2.LocalizedTitle, _Mapping]] = ..., imageLocked: _Optional[str] = ..., imageUnlocked: _Optional[str] = ...) -> None: ...

class AchievementUpdate(_message.Message):
    __slots__ = ["achievementId", "givenReward", "progress", "unlockDate"]
    ACHIEVEMENTID_FIELD_NUMBER: _ClassVar[int]
    GIVENREWARD_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    UNLOCKDATE_FIELD_NUMBER: _ClassVar[int]
    achievementId: str
    givenReward: _inventory_message_pb2.GivenReward
    progress: int
    unlockDate: int
    def __init__(self, achievementId: _Optional[str] = ..., progress: _Optional[int] = ..., unlockDate: _Optional[int] = ..., givenReward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ...) -> None: ...

class GetAchievementDefinitionRequest(_message.Message):
    __slots__ = ["achievementId"]
    ACHIEVEMENTID_FIELD_NUMBER: _ClassVar[int]
    achievementId: str
    def __init__(self, achievementId: _Optional[str] = ...) -> None: ...

class GetAchievementDefinitionResponse(_message.Message):
    __slots__ = ["achievement"]
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    achievement: AchievementDefinition
    def __init__(self, achievement: _Optional[_Union[AchievementDefinition, _Mapping]] = ...) -> None: ...

class GetAchievementDefinitionsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAchievementDefinitionsResponse(_message.Message):
    __slots__ = ["achievements"]
    ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    achievements: _containers.RepeatedCompositeFieldContainer[AchievementDefinition]
    def __init__(self, achievements: _Optional[_Iterable[_Union[AchievementDefinition, _Mapping]]] = ...) -> None: ...

class GetCurrentPlayerAchievementsRequest(_message.Message):
    __slots__ = ["showLocked"]
    SHOWLOCKED_FIELD_NUMBER: _ClassVar[int]
    showLocked: bool
    def __init__(self, showLocked: bool = ...) -> None: ...

class GetCurrentPlayerAchievementsResponse(_message.Message):
    __slots__ = ["achievements"]
    ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    achievements: _containers.RepeatedCompositeFieldContainer[PlayerAchievement]
    def __init__(self, achievements: _Optional[_Iterable[_Union[PlayerAchievement, _Mapping]]] = ...) -> None: ...

class GetPlayerAchievementsRequest(_message.Message):
    __slots__ = ["gpid", "showLocked"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    SHOWLOCKED_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    showLocked: bool
    def __init__(self, gpid: _Optional[str] = ..., showLocked: bool = ...) -> None: ...

class GetPlayerAchievementsResponse(_message.Message):
    __slots__ = ["playerAchievement"]
    PLAYERACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    playerAchievement: _containers.RepeatedCompositeFieldContainer[PlayerAchievement]
    def __init__(self, playerAchievement: _Optional[_Iterable[_Union[PlayerAchievement, _Mapping]]] = ...) -> None: ...

class GetPlayersAchievementsRequest(_message.Message):
    __slots__ = ["gpids", "showLocked"]
    GPIDS_FIELD_NUMBER: _ClassVar[int]
    SHOWLOCKED_FIELD_NUMBER: _ClassVar[int]
    gpids: _containers.RepeatedScalarFieldContainer[str]
    showLocked: bool
    def __init__(self, gpids: _Optional[_Iterable[str]] = ..., showLocked: bool = ...) -> None: ...

class GetPlayersAchievementsResponse(_message.Message):
    __slots__ = ["playerAchievements"]
    PLAYERACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    playerAchievements: _containers.RepeatedCompositeFieldContainer[PlayerAchievements]
    def __init__(self, playerAchievements: _Optional[_Iterable[_Union[PlayerAchievements, _Mapping]]] = ...) -> None: ...

class GiveAchievements(_message.Message):
    __slots__ = ["achievementsIds", "gpid"]
    ACHIEVEMENTSIDS_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    achievementsIds: _containers.RepeatedScalarFieldContainer[str]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ..., achievementsIds: _Optional[_Iterable[str]] = ...) -> None: ...

class GiveAchievementsRequest(_message.Message):
    __slots__ = ["giveAchievements"]
    GIVEACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    giveAchievements: _containers.RepeatedCompositeFieldContainer[GiveAchievements]
    def __init__(self, giveAchievements: _Optional[_Iterable[_Union[GiveAchievements, _Mapping]]] = ...) -> None: ...

class GiveAchievementsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OnAchievementsUpdatedEvent(_message.Message):
    __slots__ = ["achievementUpdates"]
    ACHIEVEMENTUPDATES_FIELD_NUMBER: _ClassVar[int]
    achievementUpdates: _containers.RepeatedCompositeFieldContainer[AchievementUpdate]
    def __init__(self, achievementUpdates: _Optional[_Iterable[_Union[AchievementUpdate, _Mapping]]] = ...) -> None: ...

class PlayerAchievement(_message.Message):
    __slots__ = ["id", "imageLocked", "imageUnlocked", "key", "progressCurrent", "progressTarget", "title", "unlockDate"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGELOCKED_FIELD_NUMBER: _ClassVar[int]
    IMAGEUNLOCKED_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PROGRESSCURRENT_FIELD_NUMBER: _ClassVar[int]
    PROGRESSTARGET_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNLOCKDATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    imageLocked: str
    imageUnlocked: str
    key: str
    progressCurrent: int
    progressTarget: int
    title: _common_message_pb2.LocalizedTitle
    unlockDate: int
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., title: _Optional[_Union[_common_message_pb2.LocalizedTitle, _Mapping]] = ..., imageLocked: _Optional[str] = ..., imageUnlocked: _Optional[str] = ..., progressCurrent: _Optional[int] = ..., progressTarget: _Optional[int] = ..., unlockDate: _Optional[int] = ...) -> None: ...

class PlayerAchievements(_message.Message):
    __slots__ = ["gpid", "playerAchievement"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    PLAYERACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    playerAchievement: _containers.RepeatedCompositeFieldContainer[PlayerAchievement]
    def __init__(self, gpid: _Optional[str] = ..., playerAchievement: _Optional[_Iterable[_Union[PlayerAchievement, _Mapping]]] = ...) -> None: ...
