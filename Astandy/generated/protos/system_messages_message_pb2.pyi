import common_message_pb2 as _common_message_pb2
import player_stats_message_pb2 as _player_stats_message_pb2
import clan_stats_message_pb2 as _clan_stats_message_pb2
import matches_message_pb2 as _matches_message_pb2
import player_message_pb2 as _player_message_pb2
import inventory_message_pb2 as _inventory_message_pb2
import currency_message_pb2 as _currency_message_pb2
import marketplace_message_pb2 as _marketplace_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACHIEVEMENT_UNLOCKED: SystemMessageType
AVATAR_REJECTED: SystemMessageType
BANS_RECEIVED: SystemMessageType
CHAT_BAN_RECEIVED: SystemMessageType
CLAN_MEMBERSHIP_ACCEPTED: SystemMessageType
CLAN_MEMBERSHIP_ENDED: SystemMessageType
COMMANDER_CASHBACK_RECEIVED: SystemMessageType
DESCRIPTOR: _descriptor.FileDescriptor
DEVELOPER_MESSAGE: SystemMessageType
FRIENDSHIP_REQUEST_ACCEPTED: SystemMessageType
GIFT_RECEIVED: SystemMessageType
GLOBAL_BAN_RECEIVED: SystemMessageType
INAPP_SUCCEED: SystemMessageType
MARKETPLACE_BAN_RECEIVED: SystemMessageType
MARKETPLACE_TRANSACTION_REVERTED: SystemMessageType
MATCHES_CANCELED: SystemMessageType
MATCHES_RESTORED: SystemMessageType
NEW_DEVICE_LOGINED: SystemMessageType
RECRUIT_SUBSCRIBED: SystemMessageType
REPORTED_PLAYERS_BANNED: SystemMessageType
REWARD_PROCESSED: SystemMessageType
SEASON_FINISHED: SystemMessageType
SOURCE_TWITCH: RewardSource
SOURCE_UNSPECIFIED: RewardSource
STORE_GIFT_RECEIVED: SystemMessageType

class BanReceived(_message.Message):
    __slots__ = ["banScope", "code", "message", "until"]
    BANSCOPE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    banScope: _player_message_pb2.BanScope
    code: int
    message: str
    until: int
    def __init__(self, code: _Optional[int] = ..., banScope: _Optional[_Union[_player_message_pb2.BanScope, str]] = ..., message: _Optional[str] = ..., until: _Optional[int] = ...) -> None: ...

class ConsumedItemsHistory(_message.Message):
    __slots__ = ["currencies", "items"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    items: _containers.RepeatedCompositeFieldContainer[_inventory_message_pb2.PlayerInventoryItemHistory]
    def __init__(self, items: _Optional[_Iterable[_Union[_inventory_message_pb2.PlayerInventoryItemHistory, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...

class CountUnreadSystemMessagesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CountUnreadSystemMessagesResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class DeleteSystemMessagesRequest(_message.Message):
    __slots__ = ["deleteAll", "messageIds"]
    DELETEALL_FIELD_NUMBER: _ClassVar[int]
    MESSAGEIDS_FIELD_NUMBER: _ClassVar[int]
    deleteAll: bool
    messageIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, messageIds: _Optional[_Iterable[str]] = ..., deleteAll: bool = ...) -> None: ...

class DeleteSystemMessagesResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSystemMessageDetailsRequest(_message.Message):
    __slots__ = ["messageId"]
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    messageId: str
    def __init__(self, messageId: _Optional[str] = ...) -> None: ...

class GetSystemMessageDetailsResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: SystemMessageDetails
    def __init__(self, message: _Optional[_Union[SystemMessageDetails, _Mapping]] = ...) -> None: ...

class GetSystemMessagesRequest(_message.Message):
    __slots__ = ["continuationToken", "unreadOnly"]
    CONTINUATIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREADONLY_FIELD_NUMBER: _ClassVar[int]
    continuationToken: _common_message_pb2.ContinuationToken
    unreadOnly: bool
    def __init__(self, continuationToken: _Optional[_Union[_common_message_pb2.ContinuationToken, _Mapping]] = ..., unreadOnly: bool = ...) -> None: ...

class GetSystemMessagesResponse(_message.Message):
    __slots__ = ["continuationToken", "messages"]
    CONTINUATIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    continuationToken: str
    messages: _containers.RepeatedCompositeFieldContainer[SystemMessagePreview]
    def __init__(self, messages: _Optional[_Iterable[_Union[SystemMessagePreview, _Mapping]]] = ..., continuationToken: _Optional[str] = ...) -> None: ...

class GivenItemsHistory(_message.Message):
    __slots__ = ["currencies", "items", "stats"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    items: _containers.RepeatedCompositeFieldContainer[_inventory_message_pb2.PlayerInventoryItemHistory]
    stats: _containers.RepeatedCompositeFieldContainer[_inventory_message_pb2.StatAmount]
    def __init__(self, items: _Optional[_Iterable[_Union[_inventory_message_pb2.PlayerInventoryItemHistory, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., stats: _Optional[_Iterable[_Union[_inventory_message_pb2.StatAmount, _Mapping]]] = ...) -> None: ...

class OnSystemMessageReceivedEvent(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: SystemMessageDetails
    def __init__(self, message: _Optional[_Union[SystemMessageDetails, _Mapping]] = ...) -> None: ...

class ReadSystemMessagesRequest(_message.Message):
    __slots__ = ["messageIds", "readAll"]
    MESSAGEIDS_FIELD_NUMBER: _ClassVar[int]
    READALL_FIELD_NUMBER: _ClassVar[int]
    messageIds: _containers.RepeatedScalarFieldContainer[str]
    readAll: bool
    def __init__(self, messageIds: _Optional[_Iterable[str]] = ..., readAll: bool = ...) -> None: ...

class ReadSystemMessagesResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SMAchievementUnlocked(_message.Message):
    __slots__ = ["imageUnlocked", "key", "title"]
    IMAGEUNLOCKED_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    imageUnlocked: str
    key: str
    title: _common_message_pb2.LocalizedTitle
    def __init__(self, key: _Optional[str] = ..., imageUnlocked: _Optional[str] = ..., title: _Optional[_Union[_common_message_pb2.LocalizedTitle, _Mapping]] = ...) -> None: ...

class SMAvatarRejected(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SMBansReceived(_message.Message):
    __slots__ = ["bans"]
    BANS_FIELD_NUMBER: _ClassVar[int]
    bans: _containers.RepeatedCompositeFieldContainer[BanReceived]
    def __init__(self, bans: _Optional[_Iterable[_Union[BanReceived, _Mapping]]] = ...) -> None: ...

class SMChatBanReceived(_message.Message):
    __slots__ = ["code", "message", "until"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    until: int
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ...) -> None: ...

class SMClanMembershipAccepted(_message.Message):
    __slots__ = ["avatarId", "clanAlreadyDeleted", "name", "tag"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    CLANALREADYDELETED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    clanAlreadyDeleted: bool
    name: str
    tag: str
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., clanAlreadyDeleted: bool = ...) -> None: ...

class SMClanMembershipEnded(_message.Message):
    __slots__ = ["avatarId", "clanAlreadyDeleted", "name", "tag"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    CLANALREADYDELETED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    clanAlreadyDeleted: bool
    name: str
    tag: str
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., clanAlreadyDeleted: bool = ...) -> None: ...

class SMCommanderCashbackReceived(_message.Message):
    __slots__ = ["recruitCashbackPlayers"]
    class RecruitCashbackPlayer(_message.Message):
        __slots__ = ["currencyAmounts", "recruitGpid", "recruitName", "recruitPlayerAlreadyDeleted", "recruitUid"]
        CURRENCYAMOUNTS_FIELD_NUMBER: _ClassVar[int]
        RECRUITGPID_FIELD_NUMBER: _ClassVar[int]
        RECRUITNAME_FIELD_NUMBER: _ClassVar[int]
        RECRUITPLAYERALREADYDELETED_FIELD_NUMBER: _ClassVar[int]
        RECRUITUID_FIELD_NUMBER: _ClassVar[int]
        currencyAmounts: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
        recruitGpid: str
        recruitName: str
        recruitPlayerAlreadyDeleted: bool
        recruitUid: str
        def __init__(self, recruitGpid: _Optional[str] = ..., recruitUid: _Optional[str] = ..., recruitName: _Optional[str] = ..., recruitPlayerAlreadyDeleted: bool = ..., currencyAmounts: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...
    RECRUITCASHBACKPLAYERS_FIELD_NUMBER: _ClassVar[int]
    recruitCashbackPlayers: _containers.RepeatedCompositeFieldContainer[SMCommanderCashbackReceived.RecruitCashbackPlayer]
    def __init__(self, recruitCashbackPlayers: _Optional[_Iterable[_Union[SMCommanderCashbackReceived.RecruitCashbackPlayer, _Mapping]]] = ...) -> None: ...

class SMDevelopersMessageReceived(_message.Message):
    __slots__ = ["message", "properties"]
    class PropertiesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    message: str
    properties: _containers.ScalarMap[str, str]
    def __init__(self, message: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SMFriendshipRequestAccepted(_message.Message):
    __slots__ = ["avatarId", "name", "playerAlreadyDeleted", "playerId", "uid"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYERALREADYDELETED_FIELD_NUMBER: _ClassVar[int]
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    name: str
    playerAlreadyDeleted: bool
    playerId: str
    uid: str
    def __init__(self, playerId: _Optional[str] = ..., uid: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., playerAlreadyDeleted: bool = ...) -> None: ...

class SMGiftReceived(_message.Message):
    __slots__ = ["currencyAmount", "playerInventoryItem"]
    CURRENCYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    PLAYERINVENTORYITEM_FIELD_NUMBER: _ClassVar[int]
    currencyAmount: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    playerInventoryItem: _containers.RepeatedCompositeFieldContainer[_inventory_message_pb2.PlayerInventoryItem]
    def __init__(self, playerInventoryItem: _Optional[_Iterable[_Union[_inventory_message_pb2.PlayerInventoryItem, _Mapping]]] = ..., currencyAmount: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...

class SMGlobalBanReceived(_message.Message):
    __slots__ = ["code", "message", "until"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    until: int
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ...) -> None: ...

class SMInAppSucceed(_message.Message):
    __slots__ = ["productId"]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    productId: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, productId: _Optional[_Iterable[str]] = ...) -> None: ...

class SMMarketplaceBanReceived(_message.Message):
    __slots__ = ["code", "message", "until"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    until: int
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ...) -> None: ...

class SMMarketplaceTransactionReverted(_message.Message):
    __slots__ = ["closeDate", "itemDefinitionId", "modifications", "price", "quantity", "requestType"]
    class ModificationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _inventory_message_pb2.ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_inventory_message_pb2.ItemModificationValue, _Mapping]] = ...) -> None: ...
    CLOSEDATE_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    REQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    closeDate: int
    itemDefinitionId: int
    modifications: _containers.MessageMap[str, _inventory_message_pb2.ItemModificationValue]
    price: float
    quantity: int
    requestType: _marketplace_message_pb2.MarketRequestType
    def __init__(self, requestType: _Optional[_Union[_marketplace_message_pb2.MarketRequestType, str]] = ..., itemDefinitionId: _Optional[int] = ..., modifications: _Optional[_Mapping[str, _inventory_message_pb2.ItemModificationValue]] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., closeDate: _Optional[int] = ...) -> None: ...

class SMMatchesCanceled(_message.Message):
    __slots__ = ["matches"]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[_matches_message_pb2.FinishedMatch]
    def __init__(self, matches: _Optional[_Iterable[_Union[_matches_message_pb2.FinishedMatch, _Mapping]]] = ...) -> None: ...

class SMMatchesRestored(_message.Message):
    __slots__ = ["matches"]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[_matches_message_pb2.FinishedMatch]
    def __init__(self, matches: _Optional[_Iterable[_Union[_matches_message_pb2.FinishedMatch, _Mapping]]] = ...) -> None: ...

class SMNewDeviceLogined(_message.Message):
    __slots__ = ["country", "deviceModel", "ip"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DEVICEMODEL_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    country: str
    deviceModel: str
    ip: str
    def __init__(self, deviceModel: _Optional[str] = ..., country: _Optional[str] = ..., ip: _Optional[str] = ...) -> None: ...

class SMRecruitsSubscribed(_message.Message):
    __slots__ = ["recruitPlayers"]
    class SubscribedRecruitPlayer(_message.Message):
        __slots__ = ["gpid", "name", "playerAlreadyDeleted", "uid"]
        GPID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PLAYERALREADYDELETED_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        gpid: str
        name: str
        playerAlreadyDeleted: bool
        uid: str
        def __init__(self, gpid: _Optional[str] = ..., uid: _Optional[str] = ..., name: _Optional[str] = ..., playerAlreadyDeleted: bool = ...) -> None: ...
    RECRUITPLAYERS_FIELD_NUMBER: _ClassVar[int]
    recruitPlayers: _containers.RepeatedCompositeFieldContainer[SMRecruitsSubscribed.SubscribedRecruitPlayer]
    def __init__(self, recruitPlayers: _Optional[_Iterable[_Union[SMRecruitsSubscribed.SubscribedRecruitPlayer, _Mapping]]] = ...) -> None: ...

class SMReportedPlayersBanned(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class SMRewardProcessed(_message.Message):
    __slots__ = ["consumed", "context", "given", "source"]
    class ContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONSUMED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    GIVEN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    consumed: ConsumedItemsHistory
    context: _containers.ScalarMap[str, str]
    given: GivenItemsHistory
    source: RewardSource
    def __init__(self, source: _Optional[_Union[RewardSource, str]] = ..., given: _Optional[_Union[GivenItemsHistory, _Mapping]] = ..., consumed: _Optional[_Union[ConsumedItemsHistory, _Mapping]] = ..., context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SMSeasonFinished(_message.Message):
    __slots__ = ["clanMemberStats", "clanStats", "currencies", "items", "playerStats", "seasonId"]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PLAYERSTATS_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[_clan_stats_message_pb2.ClanMemberStat]
    clanStats: _containers.RepeatedCompositeFieldContainer[_clan_stats_message_pb2.ClanStat]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    items: _containers.RepeatedCompositeFieldContainer[_inventory_message_pb2.PlayerInventoryItem]
    playerStats: _containers.RepeatedCompositeFieldContainer[_player_stats_message_pb2.PlayerStat]
    seasonId: str
    def __init__(self, seasonId: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_inventory_message_pb2.PlayerInventoryItem, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., playerStats: _Optional[_Iterable[_Union[_player_stats_message_pb2.PlayerStat, _Mapping]]] = ..., clanStats: _Optional[_Iterable[_Union[_clan_stats_message_pb2.ClanStat, _Mapping]]] = ..., clanMemberStats: _Optional[_Iterable[_Union[_clan_stats_message_pb2.ClanMemberStat, _Mapping]]] = ...) -> None: ...

class SMStoreGiftReceived(_message.Message):
    __slots__ = ["context", "giverGpid", "giverName", "giverUid", "productIds"]
    class ContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    GIVERGPID_FIELD_NUMBER: _ClassVar[int]
    GIVERNAME_FIELD_NUMBER: _ClassVar[int]
    GIVERUID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTIDS_FIELD_NUMBER: _ClassVar[int]
    context: _containers.ScalarMap[str, str]
    giverGpid: str
    giverName: str
    giverUid: str
    productIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, giverGpid: _Optional[str] = ..., giverUid: _Optional[str] = ..., giverName: _Optional[str] = ..., productIds: _Optional[_Iterable[str]] = ..., context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SystemMessageDetails(_message.Message):
    __slots__ = ["achievementUnlocked", "avatarRejected", "bansReceived", "chatBanReceived", "clanMembershipAccepted", "clanMembershipEnded", "commanderCashbackReceived", "created", "deleteAt", "developersMessageReceived", "friendshipRequestAccepted", "giftReceived", "globalBanReceived", "inAppSucceed", "marketplaceBanReceived", "marketplaceTransactionReverted", "matchesCanceled", "matchesRestored", "messageId", "newDeviceLogined", "recruitsSubscribed", "reportedPlayersBanned", "rewardProcessed", "seasonFinished", "storeGiftReceived", "type", "updated"]
    ACHIEVEMENTUNLOCKED_FIELD_NUMBER: _ClassVar[int]
    AVATARREJECTED_FIELD_NUMBER: _ClassVar[int]
    BANSRECEIVED_FIELD_NUMBER: _ClassVar[int]
    CHATBANRECEIVED_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSHIPACCEPTED_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSHIPENDED_FIELD_NUMBER: _ClassVar[int]
    COMMANDERCASHBACKRECEIVED_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETEAT_FIELD_NUMBER: _ClassVar[int]
    DEVELOPERSMESSAGERECEIVED_FIELD_NUMBER: _ClassVar[int]
    FRIENDSHIPREQUESTACCEPTED_FIELD_NUMBER: _ClassVar[int]
    GIFTRECEIVED_FIELD_NUMBER: _ClassVar[int]
    GLOBALBANRECEIVED_FIELD_NUMBER: _ClassVar[int]
    INAPPSUCCEED_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACEBANRECEIVED_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACETRANSACTIONREVERTED_FIELD_NUMBER: _ClassVar[int]
    MATCHESCANCELED_FIELD_NUMBER: _ClassVar[int]
    MATCHESRESTORED_FIELD_NUMBER: _ClassVar[int]
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    NEWDEVICELOGINED_FIELD_NUMBER: _ClassVar[int]
    RECRUITSSUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    REPORTEDPLAYERSBANNED_FIELD_NUMBER: _ClassVar[int]
    REWARDPROCESSED_FIELD_NUMBER: _ClassVar[int]
    SEASONFINISHED_FIELD_NUMBER: _ClassVar[int]
    STOREGIFTRECEIVED_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    achievementUnlocked: SMAchievementUnlocked
    avatarRejected: SMAvatarRejected
    bansReceived: SMBansReceived
    chatBanReceived: SMChatBanReceived
    clanMembershipAccepted: SMClanMembershipAccepted
    clanMembershipEnded: SMClanMembershipEnded
    commanderCashbackReceived: SMCommanderCashbackReceived
    created: int
    deleteAt: int
    developersMessageReceived: SMDevelopersMessageReceived
    friendshipRequestAccepted: SMFriendshipRequestAccepted
    giftReceived: SMGiftReceived
    globalBanReceived: SMGlobalBanReceived
    inAppSucceed: SMInAppSucceed
    marketplaceBanReceived: SMMarketplaceBanReceived
    marketplaceTransactionReverted: SMMarketplaceTransactionReverted
    matchesCanceled: SMMatchesCanceled
    matchesRestored: SMMatchesRestored
    messageId: str
    newDeviceLogined: SMNewDeviceLogined
    recruitsSubscribed: SMRecruitsSubscribed
    reportedPlayersBanned: SMReportedPlayersBanned
    rewardProcessed: SMRewardProcessed
    seasonFinished: SMSeasonFinished
    storeGiftReceived: SMStoreGiftReceived
    type: SystemMessageType
    updated: int
    def __init__(self, messageId: _Optional[str] = ..., type: _Optional[_Union[SystemMessageType, str]] = ..., created: _Optional[int] = ..., deleteAt: _Optional[int] = ..., updated: _Optional[int] = ..., achievementUnlocked: _Optional[_Union[SMAchievementUnlocked, _Mapping]] = ..., avatarRejected: _Optional[_Union[SMAvatarRejected, _Mapping]] = ..., clanMembershipAccepted: _Optional[_Union[SMClanMembershipAccepted, _Mapping]] = ..., clanMembershipEnded: _Optional[_Union[SMClanMembershipEnded, _Mapping]] = ..., developersMessageReceived: _Optional[_Union[SMDevelopersMessageReceived, _Mapping]] = ..., friendshipRequestAccepted: _Optional[_Union[SMFriendshipRequestAccepted, _Mapping]] = ..., giftReceived: _Optional[_Union[SMGiftReceived, _Mapping]] = ..., marketplaceTransactionReverted: _Optional[_Union[SMMarketplaceTransactionReverted, _Mapping]] = ..., matchesCanceled: _Optional[_Union[SMMatchesCanceled, _Mapping]] = ..., globalBanReceived: _Optional[_Union[SMGlobalBanReceived, _Mapping]] = ..., reportedPlayersBanned: _Optional[_Union[SMReportedPlayersBanned, _Mapping]] = ..., seasonFinished: _Optional[_Union[SMSeasonFinished, _Mapping]] = ..., marketplaceBanReceived: _Optional[_Union[SMMarketplaceBanReceived, _Mapping]] = ..., chatBanReceived: _Optional[_Union[SMChatBanReceived, _Mapping]] = ..., matchesRestored: _Optional[_Union[SMMatchesRestored, _Mapping]] = ..., inAppSucceed: _Optional[_Union[SMInAppSucceed, _Mapping]] = ..., newDeviceLogined: _Optional[_Union[SMNewDeviceLogined, _Mapping]] = ..., recruitsSubscribed: _Optional[_Union[SMRecruitsSubscribed, _Mapping]] = ..., commanderCashbackReceived: _Optional[_Union[SMCommanderCashbackReceived, _Mapping]] = ..., rewardProcessed: _Optional[_Union[SMRewardProcessed, _Mapping]] = ..., storeGiftReceived: _Optional[_Union[SMStoreGiftReceived, _Mapping]] = ..., bansReceived: _Optional[_Union[SMBansReceived, _Mapping]] = ...) -> None: ...

class SystemMessagePreview(_message.Message):
    __slots__ = ["created", "deleteAt", "isRead", "messageId", "type", "updated"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETEAT_FIELD_NUMBER: _ClassVar[int]
    ISREAD_FIELD_NUMBER: _ClassVar[int]
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    created: int
    deleteAt: int
    isRead: bool
    messageId: str
    type: SystemMessageType
    updated: int
    def __init__(self, messageId: _Optional[str] = ..., type: _Optional[_Union[SystemMessageType, str]] = ..., isRead: bool = ..., created: _Optional[int] = ..., deleteAt: _Optional[int] = ..., updated: _Optional[int] = ...) -> None: ...

class SystemMessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RewardSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
