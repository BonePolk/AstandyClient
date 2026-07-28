import currency_message_pb2 as _currency_message_pb2
import player_message_pb2 as _player_message_pb2
import common_message_pb2 as _common_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

AWAITS_PAYMENT: ReferralCashbackPaymentStatus
COMMANDER: ReferralState
DESCRIPTOR: _descriptor.FileDescriptor
PAID: ReferralCashbackPaymentStatus
PAYMENT_CANCELLED: ReferralCashbackPaymentStatus
RECRUIT: ReferralState

class FindReferralStateRequest(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class FindReferralStateResponse(_message.Message):
    __slots__ = ["player", "state"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    player: _player_message_pb2.Player
    state: ReferralState
    def __init__(self, player: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., state: _Optional[_Union[ReferralState, str]] = ...) -> None: ...

class GetRecruitByIdRequest(_message.Message):
    __slots__ = ["recruitGpid", "withCashbackPayments"]
    RECRUITGPID_FIELD_NUMBER: _ClassVar[int]
    WITHCASHBACKPAYMENTS_FIELD_NUMBER: _ClassVar[int]
    recruitGpid: str
    withCashbackPayments: bool
    def __init__(self, recruitGpid: _Optional[str] = ..., withCashbackPayments: bool = ...) -> None: ...

class GetRecruitByIdResponse(_message.Message):
    __slots__ = ["recruit"]
    RECRUIT_FIELD_NUMBER: _ClassVar[int]
    recruit: ReferralRecruit
    def __init__(self, recruit: _Optional[_Union[ReferralRecruit, _Mapping]] = ...) -> None: ...

class GetRecruitsByOffsetRequest(_message.Message):
    __slots__ = ["continuationToken", "withCashbackPayments"]
    CONTINUATIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    WITHCASHBACKPAYMENTS_FIELD_NUMBER: _ClassVar[int]
    continuationToken: _common_message_pb2.ContinuationToken
    withCashbackPayments: bool
    def __init__(self, continuationToken: _Optional[_Union[_common_message_pb2.ContinuationToken, _Mapping]] = ..., withCashbackPayments: bool = ...) -> None: ...

class GetRecruitsByOffsetResponse(_message.Message):
    __slots__ = ["continuationToken", "recruits"]
    CONTINUATIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    RECRUITS_FIELD_NUMBER: _ClassVar[int]
    continuationToken: str
    recruits: _containers.RepeatedCompositeFieldContainer[ReferralRecruit]
    def __init__(self, recruits: _Optional[_Iterable[_Union[ReferralRecruit, _Mapping]]] = ..., continuationToken: _Optional[str] = ...) -> None: ...

class GetReferralPlayerStateRequest(_message.Message):
    __slots__ = ["withFullInfo"]
    WITHFULLINFO_FIELD_NUMBER: _ClassVar[int]
    withFullInfo: bool
    def __init__(self, withFullInfo: bool = ...) -> None: ...

class GetReferralPlayerStateResponse(_message.Message):
    __slots__ = ["referralPlayerState", "referralPlayerStateLite"]
    REFERRALPLAYERSTATELITE_FIELD_NUMBER: _ClassVar[int]
    REFERRALPLAYERSTATE_FIELD_NUMBER: _ClassVar[int]
    referralPlayerState: ReferralPlayerState
    referralPlayerStateLite: ReferralPlayerStateLite
    def __init__(self, referralPlayerState: _Optional[_Union[ReferralPlayerState, _Mapping]] = ..., referralPlayerStateLite: _Optional[_Union[ReferralPlayerStateLite, _Mapping]] = ...) -> None: ...

class GetReferralSystemSettingsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetReferralSystemSettingsResponse(_message.Message):
    __slots__ = ["cashbackSettings", "settings"]
    CASHBACKSETTINGS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    cashbackSettings: ReferralCashbackSettings
    settings: ReferralSystemSettings
    def __init__(self, settings: _Optional[_Union[ReferralSystemSettings, _Mapping]] = ..., cashbackSettings: _Optional[_Union[ReferralCashbackSettings, _Mapping]] = ...) -> None: ...

class OnPlayerStateChangedEvent(_message.Message):
    __slots__ = ["referralPlayerState"]
    REFERRALPLAYERSTATE_FIELD_NUMBER: _ClassVar[int]
    referralPlayerState: ReferralPlayerState
    def __init__(self, referralPlayerState: _Optional[_Union[ReferralPlayerState, _Mapping]] = ...) -> None: ...

class ReferralCashbackPayment(_message.Message):
    __slots__ = ["currencyAmounts", "lastStatusUpdated", "paymentStatus"]
    CURRENCYAMOUNTS_FIELD_NUMBER: _ClassVar[int]
    LASTSTATUSUPDATED_FIELD_NUMBER: _ClassVar[int]
    PAYMENTSTATUS_FIELD_NUMBER: _ClassVar[int]
    currencyAmounts: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    lastStatusUpdated: int
    paymentStatus: ReferralCashbackPaymentStatus
    def __init__(self, paymentStatus: _Optional[_Union[ReferralCashbackPaymentStatus, str]] = ..., currencyAmounts: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., lastStatusUpdated: _Optional[int] = ...) -> None: ...

class ReferralCashbackSettings(_message.Message):
    __slots__ = ["currencies", "initialPaymentsSettings", "nextPaymentsSettings", "paymentAfterDays", "thresholdPoints"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    INITIALPAYMENTSSETTINGS_FIELD_NUMBER: _ClassVar[int]
    NEXTPAYMENTSSETTINGS_FIELD_NUMBER: _ClassVar[int]
    PAYMENTAFTERDAYS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLDPOINTS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedScalarFieldContainer[int]
    initialPaymentsSettings: ReferralPaymentsSettings
    nextPaymentsSettings: ReferralPaymentsSettings
    paymentAfterDays: int
    thresholdPoints: int
    def __init__(self, initialPaymentsSettings: _Optional[_Union[ReferralPaymentsSettings, _Mapping]] = ..., nextPaymentsSettings: _Optional[_Union[ReferralPaymentsSettings, _Mapping]] = ..., paymentAfterDays: _Optional[int] = ..., currencies: _Optional[_Iterable[int]] = ..., thresholdPoints: _Optional[int] = ...) -> None: ...

class ReferralCommanderInfo(_message.Message):
    __slots__ = ["activeRecruits", "startedAsCommander", "statistics"]
    ACTIVERECRUITS_FIELD_NUMBER: _ClassVar[int]
    STARTEDASCOMMANDER_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    activeRecruits: int
    startedAsCommander: int
    statistics: ReferralCommanderStatistics
    def __init__(self, startedAsCommander: _Optional[int] = ..., activeRecruits: _Optional[int] = ..., statistics: _Optional[_Union[ReferralCommanderStatistics, _Mapping]] = ...) -> None: ...

class ReferralCommanderStatistics(_message.Message):
    __slots__ = ["currencyEarned", "recruitsCompleted", "recruitsMadePayment", "totalRecruits"]
    CURRENCYEARNED_FIELD_NUMBER: _ClassVar[int]
    RECRUITSCOMPLETED_FIELD_NUMBER: _ClassVar[int]
    RECRUITSMADEPAYMENT_FIELD_NUMBER: _ClassVar[int]
    TOTALRECRUITS_FIELD_NUMBER: _ClassVar[int]
    currencyEarned: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    recruitsCompleted: int
    recruitsMadePayment: int
    totalRecruits: int
    def __init__(self, totalRecruits: _Optional[int] = ..., recruitsCompleted: _Optional[int] = ..., recruitsMadePayment: _Optional[int] = ..., currencyEarned: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...

class ReferralPaymentsSettings(_message.Message):
    __slots__ = ["amount", "paymentsAmount", "percent"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAYMENTSAMOUNT_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    amount: float
    paymentsAmount: int
    percent: float
    def __init__(self, paymentsAmount: _Optional[int] = ..., percent: _Optional[float] = ..., amount: _Optional[float] = ...) -> None: ...

class ReferralPlayerState(_message.Message):
    __slots__ = ["commanderInfo", "recruitInfo", "state"]
    COMMANDERINFO_FIELD_NUMBER: _ClassVar[int]
    RECRUITINFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    commanderInfo: ReferralCommanderInfo
    recruitInfo: ReferralRecruitInfo
    state: ReferralState
    def __init__(self, state: _Optional[_Union[ReferralState, str]] = ..., recruitInfo: _Optional[_Union[ReferralRecruitInfo, _Mapping]] = ..., commanderInfo: _Optional[_Union[ReferralCommanderInfo, _Mapping]] = ...) -> None: ...

class ReferralPlayerStateLite(_message.Message):
    __slots__ = ["recruitInfo", "state"]
    RECRUITINFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    recruitInfo: ReferralRecruitInfoLite
    state: ReferralState
    def __init__(self, state: _Optional[_Union[ReferralState, str]] = ..., recruitInfo: _Optional[_Union[ReferralRecruitInfoLite, _Mapping]] = ...) -> None: ...

class ReferralRecruit(_message.Message):
    __slots__ = ["achievedThreshold", "cashbackPayments", "player", "statistics", "subscribedToCommander"]
    ACHIEVEDTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    CASHBACKPAYMENTS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBEDTOCOMMANDER_FIELD_NUMBER: _ClassVar[int]
    achievedThreshold: bool
    cashbackPayments: _containers.RepeatedCompositeFieldContainer[ReferralCashbackPayment]
    player: _player_message_pb2.Player
    statistics: ReferralRecruitStatistics
    subscribedToCommander: int
    def __init__(self, player: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., achievedThreshold: bool = ..., subscribedToCommander: _Optional[int] = ..., statistics: _Optional[_Union[ReferralRecruitStatistics, _Mapping]] = ..., cashbackPayments: _Optional[_Iterable[_Union[ReferralCashbackPayment, _Mapping]]] = ...) -> None: ...

class ReferralRecruitInfo(_message.Message):
    __slots__ = ["commanderGpid", "startedReferralProgram", "statistics", "subscribedToCommander"]
    COMMANDERGPID_FIELD_NUMBER: _ClassVar[int]
    STARTEDREFERRALPROGRAM_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBEDTOCOMMANDER_FIELD_NUMBER: _ClassVar[int]
    commanderGpid: str
    startedReferralProgram: int
    statistics: ReferralRecruitStatistics
    subscribedToCommander: int
    def __init__(self, commanderGpid: _Optional[str] = ..., subscribedToCommander: _Optional[int] = ..., statistics: _Optional[_Union[ReferralRecruitStatistics, _Mapping]] = ..., startedReferralProgram: _Optional[int] = ...) -> None: ...

class ReferralRecruitInfoLite(_message.Message):
    __slots__ = ["commanderGpid", "startedReferralProgram"]
    COMMANDERGPID_FIELD_NUMBER: _ClassVar[int]
    STARTEDREFERRALPROGRAM_FIELD_NUMBER: _ClassVar[int]
    commanderGpid: str
    startedReferralProgram: int
    def __init__(self, commanderGpid: _Optional[str] = ..., startedReferralProgram: _Optional[int] = ...) -> None: ...

class ReferralRecruitStatistics(_message.Message):
    __slots__ = ["completedOnTime", "gameEventProgressPoints"]
    COMPLETEDONTIME_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTPROGRESSPOINTS_FIELD_NUMBER: _ClassVar[int]
    completedOnTime: bool
    gameEventProgressPoints: int
    def __init__(self, gameEventProgressPoints: _Optional[int] = ..., completedOnTime: bool = ...) -> None: ...

class ReferralSystemSettings(_message.Message):
    __slots__ = ["commanderGameEventId", "commanderSubscriptionTimeoutMs", "durationDays", "enabled", "recruitGameEventId"]
    COMMANDERGAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    COMMANDERSUBSCRIPTIONTIMEOUTMS_FIELD_NUMBER: _ClassVar[int]
    DURATIONDAYS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RECRUITGAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    commanderGameEventId: str
    commanderSubscriptionTimeoutMs: int
    durationDays: int
    enabled: bool
    recruitGameEventId: str
    def __init__(self, recruitGameEventId: _Optional[str] = ..., commanderGameEventId: _Optional[str] = ..., durationDays: _Optional[int] = ..., commanderSubscriptionTimeoutMs: _Optional[int] = ..., enabled: bool = ...) -> None: ...

class SubscribeToCommanderRequest(_message.Message):
    __slots__ = ["commanderUid"]
    COMMANDERUID_FIELD_NUMBER: _ClassVar[int]
    commanderUid: str
    def __init__(self, commanderUid: _Optional[str] = ...) -> None: ...

class SubscribeToCommanderResponse(_message.Message):
    __slots__ = ["player"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    player: _player_message_pb2.Player
    def __init__(self, player: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ...) -> None: ...

class ReferralCashbackPaymentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ReferralState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
