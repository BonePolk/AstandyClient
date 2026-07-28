from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ProcessingState_Creating: _ClassVar[ProcessingState]
    ProcessingState_Cancelling: _ClassVar[ProcessingState]
    ProcessingState_Expiring: _ClassVar[ProcessingState]

class OperationValuePair_ValueOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OperationValuePair_ValueOneofCase_None: _ClassVar[OperationValuePair_ValueOneofCase]
    OperationValuePair_ValueOneofCase_IntValue: _ClassVar[OperationValuePair_ValueOneofCase]
    OperationValuePair_ValueOneofCase_BoolValue: _ClassVar[OperationValuePair_ValueOneofCase]

class LobbyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LobbyType_Default: _ClassVar[LobbyType]
    LobbyType_SqlLobby: _ClassVar[LobbyType]
    LobbyType_AsyncRandomLobby: _ClassVar[LobbyType]

class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RequestType_NoneTypeRequest: _ClassVar[RequestType]
    RequestType_OpenRequest: _ClassVar[RequestType]
    RequestType_ClosedRequest: _ClassVar[RequestType]

class PropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PropertyType_None: _ClassVar[PropertyType]
    PropertyType_Game: _ClassVar[PropertyType]
    PropertyType_Actor: _ClassVar[PropertyType]
    PropertyType_GameAndActor: _ClassVar[PropertyType]

class OperationValuePair_Types_Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OperationValuePair_Types_Operation_Default: _ClassVar[OperationValuePair_Types_Operation]
    OperationValuePair_Types_Operation_Exist: _ClassVar[OperationValuePair_Types_Operation]
    OperationValuePair_Types_Operation_Equals: _ClassVar[OperationValuePair_Types_Operation]

class OnlineStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OnlineStatus_StateOffline: _ClassVar[OnlineStatus]
    OnlineStatus_StateOnline: _ClassVar[OnlineStatus]
    OnlineStatus_StateBusy: _ClassVar[OnlineStatus]
    OnlineStatus_StateAway: _ClassVar[OnlineStatus]
    OnlineStatus_StateSnooze: _ClassVar[OnlineStatus]
    OnlineStatus_StateLookingToTrade: _ClassVar[OnlineStatus]
    OnlineStatus_StateLookingToPlay: _ClassVar[OnlineStatus]

class MarketRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MarketRequestType_MpNoneType: _ClassVar[MarketRequestType]
    MarketRequestType_SaleRequest: _ClassVar[MarketRequestType]
    MarketRequestType_PurchaseRequest: _ClassVar[MarketRequestType]

class ClanMemberRolePermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ClanMemberRolePermission_ChangeClanSettings: _ClassVar[ClanMemberRolePermission]
    ClanMemberRolePermission_AcceptMember: _ClassVar[ClanMemberRolePermission]
    ClanMemberRolePermission_InviteMember: _ClassVar[ClanMemberRolePermission]
    ClanMemberRolePermission_KickMemberLess: _ClassVar[ClanMemberRolePermission]
    ClanMemberRolePermission_KickMemberEqual: _ClassVar[ClanMemberRolePermission]
    ClanMemberRolePermission_AssignRoleLess: _ClassVar[ClanMemberRolePermission]
    ClanMemberRolePermission_AssignRoleEqual: _ClassVar[ClanMemberRolePermission]
    ClanMemberRolePermission_CreateClanBattle: _ClassVar[ClanMemberRolePermission]
    ClanMemberRolePermission_JoinClanBattle: _ClassVar[ClanMemberRolePermission]
    ClanMemberRolePermission_UpgradeClanMembersCount: _ClassVar[ClanMemberRolePermission]

class ClanType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ClanType_Closed: _ClassVar[ClanType]
    ClanType_ByRequest: _ClassVar[ClanType]
    ClanType_Opened: _ClassVar[ClanType]

class RetrievableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RetrievableType_Unremovable: _ClassVar[RetrievableType]
    RetrievableType_Removable: _ClassVar[RetrievableType]
    RetrievableType_Retrievable: _ClassVar[RetrievableType]

class GoogleAuthResponse_TicketsOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GoogleAuthResponse_TicketsOneofCase_None: _ClassVar[GoogleAuthResponse_TicketsOneofCase]
    GoogleAuthResponse_TicketsOneofCase_Ticket: _ClassVar[GoogleAuthResponse_TicketsOneofCase]
    GoogleAuthResponse_TicketsOneofCase_TicketBinary: _ClassVar[GoogleAuthResponse_TicketsOneofCase]

class JoinClanType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JoinClanType_ByAcceptInviteRequest: _ClassVar[JoinClanType]
    JoinClanType_ByAcceptJoinRequest: _ClassVar[JoinClanType]
    JoinClanType_JoinToOpenClan: _ClassVar[JoinClanType]
    JoinClanType_NoneJoinType: _ClassVar[JoinClanType]

class BanScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BanScope_Global: _ClassVar[BanScope]
    BanScope_Marketplace: _ClassVar[BanScope]
    BanScope_MarketplaceSpecial: _ClassVar[BanScope]
    BanScope_Chat: _ClassVar[BanScope]

class BoltIdAuthResponse_TicketsOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BoltIdAuthResponse_TicketsOneofCase_None: _ClassVar[BoltIdAuthResponse_TicketsOneofCase]
    BoltIdAuthResponse_TicketsOneofCase_Ticket: _ClassVar[BoltIdAuthResponse_TicketsOneofCase]
    BoltIdAuthResponse_TicketsOneofCase_TicketBinary: _ClassVar[BoltIdAuthResponse_TicketsOneofCase]

class OfferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OfferType_InappPurchase: _ClassVar[OfferType]
    OfferType_Store: _ClassVar[OfferType]

class LobbyPlayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LobbyPlayerType_Any: _ClassVar[LobbyPlayerType]
    LobbyPlayerType_Member: _ClassVar[LobbyPlayerType]
    LobbyPlayerType_Spectator: _ClassVar[LobbyPlayerType]

class StatDefType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    StatDefType_Int: _ClassVar[StatDefType]
    StatDefType_Float: _ClassVar[StatDefType]
    StatDefType_Long: _ClassVar[StatDefType]

class VkAuthResponse_TicketsOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VkAuthResponse_TicketsOneofCase_None: _ClassVar[VkAuthResponse_TicketsOneofCase]
    VkAuthResponse_TicketsOneofCase_Ticket: _ClassVar[VkAuthResponse_TicketsOneofCase]
    VkAuthResponse_TicketsOneofCase_TicketBinary: _ClassVar[VkAuthResponse_TicketsOneofCase]

class SettingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SettingType_String: _ClassVar[SettingType]
    SettingType_Integer: _ClassVar[SettingType]
    SettingType_Float: _ClassVar[SettingType]
    SettingType_Bool: _ClassVar[SettingType]
    SettingType_Long: _ClassVar[SettingType]

class ClosingReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ClosingReason_NoneReason: _ClassVar[ClosingReason]
    ClosingReason_SuccessTransaction: _ClassVar[ClosingReason]
    ClosingReason_NotEnoughFunds: _ClassVar[ClosingReason]
    ClosingReason_Cancelled: _ClassVar[ClosingReason]
    ClosingReason_SaleRequestNotFound: _ClassVar[ClosingReason]
    ClosingReason_Expired: _ClassVar[ClosingReason]
    ClosingReason_InventorySizeExceeded: _ClassVar[ClosingReason]

class ExternalPlatform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ExternalPlatform_Default: _ClassVar[ExternalPlatform]
    ExternalPlatform_Vk: _ClassVar[ExternalPlatform]
    ExternalPlatform_Facebook: _ClassVar[ExternalPlatform]
    ExternalPlatform_Youtube: _ClassVar[ExternalPlatform]
    ExternalPlatform_TikTok: _ClassVar[ExternalPlatform]
    ExternalPlatform_Instagram: _ClassVar[ExternalPlatform]
    ExternalPlatform_Twitter: _ClassVar[ExternalPlatform]
    ExternalPlatform_Discord: _ClassVar[ExternalPlatform]

class SystemMessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SystemMessageType_MatchesCanceled: _ClassVar[SystemMessageType]
    SystemMessageType_ReportedPlayersBanned: _ClassVar[SystemMessageType]
    SystemMessageType_FriendshipRequestAccepted: _ClassVar[SystemMessageType]
    SystemMessageType_ClanMembershipAccepted: _ClassVar[SystemMessageType]
    SystemMessageType_ClanMembershipEnded: _ClassVar[SystemMessageType]
    SystemMessageType_AchievementUnlocked: _ClassVar[SystemMessageType]
    SystemMessageType_GiftReceived: _ClassVar[SystemMessageType]
    SystemMessageType_SeasonFinished: _ClassVar[SystemMessageType]
    SystemMessageType_AvatarRejected: _ClassVar[SystemMessageType]
    SystemMessageType_GlobalBanReceived: _ClassVar[SystemMessageType]
    SystemMessageType_MarketplaceTransactionReverted: _ClassVar[SystemMessageType]
    SystemMessageType_DeveloperMessage: _ClassVar[SystemMessageType]
    SystemMessageType_MarketplaceBanReceived: _ClassVar[SystemMessageType]
    SystemMessageType_ChatBanReceived: _ClassVar[SystemMessageType]
    SystemMessageType_InappSucceed: _ClassVar[SystemMessageType]
    SystemMessageType_NewDeviceLogined: _ClassVar[SystemMessageType]
    SystemMessageType_MatchesRestored: _ClassVar[SystemMessageType]

class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Platform_Win32S: _ClassVar[Platform]
    Platform_Win32Windows: _ClassVar[Platform]
    Platform_Win32NT: _ClassVar[Platform]
    Platform_WinCE: _ClassVar[Platform]
    Platform_Unix: _ClassVar[Platform]
    Platform_Xbox: _ClassVar[Platform]
    Platform_MacOSX: _ClassVar[Platform]

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MessageType_ClansNoneType: _ClassVar[MessageType]
    MessageType_ChatMessage: _ClassVar[MessageType]
    MessageType_LogMessage: _ClassVar[MessageType]

class Store(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Store_GooglePlay: _ClassVar[Store]
    Store_AppStore: _ClassVar[Store]
    Store_AppGallery: _ClassVar[Store]
    Store_Amazon: _ClassVar[Store]
    Store_Dev: _ClassVar[Store]
    Store_Yoo: _ClassVar[Store]

class ProgressGameEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ProgressGameEventType_Unspecified: _ClassVar[ProgressGameEventType]
    ProgressGameEventType_GamePassBought: _ClassVar[ProgressGameEventType]
    ProgressGameEventType_EventPointsBought: _ClassVar[ProgressGameEventType]
    ProgressGameEventType_GamePassAndEventPointsBought: _ClassVar[ProgressGameEventType]

class BHBHHDGDFCHFACH(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BHBHHDGDFCHFACH_Unknown: _ClassVar[BHBHHDGDFCHFACH]
    BHBHHDGDFCHFACH_GroupWaitTimeout: _ClassVar[BHBHHDGDFCHFACH]
    BHBHHDGDFCHFACH_GroupMemberDisconnected: _ClassVar[BHBHHDGDFCHFACH]
    BHBHHDGDFCHFACH_GroupMemberNotConfirmed: _ClassVar[BHBHHDGDFCHFACH]
    BHBHHDGDFCHFACH_GroupMemberIsNotOneClan: _ClassVar[BHBHHDGDFCHFACH]

class MatchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MatchState_Finished: _ClassVar[MatchState]
    MatchState_Canceled: _ClassVar[MatchState]
    MatchState_Annulled: _ClassVar[MatchState]

class RelationshipStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RelationshipStatus_None: _ClassVar[RelationshipStatus]
    RelationshipStatus_Blocked: _ClassVar[RelationshipStatus]
    RelationshipStatus_Initiator: _ClassVar[RelationshipStatus]
    RelationshipStatus_Friend: _ClassVar[RelationshipStatus]
    RelationshipStatus_Recipient: _ClassVar[RelationshipStatus]
    RelationshipStatus_Ignored: _ClassVar[RelationshipStatus]

class HuaweiAuthResponse_TicketsOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HuaweiAuthResponse_TicketsOneofCase_None: _ClassVar[HuaweiAuthResponse_TicketsOneofCase]
    HuaweiAuthResponse_TicketsOneofCase_Ticket: _ClassVar[HuaweiAuthResponse_TicketsOneofCase]
    HuaweiAuthResponse_TicketsOneofCase_TicketBinary: _ClassVar[HuaweiAuthResponse_TicketsOneofCase]

class AppleIdAuthResponse_TicketsOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AppleIdAuthResponse_TicketsOneofCase_None: _ClassVar[AppleIdAuthResponse_TicketsOneofCase]
    AppleIdAuthResponse_TicketsOneofCase_Ticket: _ClassVar[AppleIdAuthResponse_TicketsOneofCase]
    AppleIdAuthResponse_TicketsOneofCase_TicketBinary: _ClassVar[AppleIdAuthResponse_TicketsOneofCase]

class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MatchType_Simple: _ClassVar[MatchType]
    MatchType_Win32: _ClassVar[MatchType]

class AuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AuthType_Test: _ClassVar[AuthType]
    AuthType_Guest: _ClassVar[AuthType]
    AuthType_GooglePlay: _ClassVar[AuthType]
    AuthType_Facebook: _ClassVar[AuthType]
    AuthType_GameCenter: _ClassVar[AuthType]
    AuthType_AppleId: _ClassVar[AuthType]
    AuthType_Huawei: _ClassVar[AuthType]
    AuthType_Vk: _ClassVar[AuthType]
    AuthType_BoltId: _ClassVar[AuthType]

class GameCenterAuthResponse_TicketsOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GameCenterAuthResponse_TicketsOneofCase_None: _ClassVar[GameCenterAuthResponse_TicketsOneofCase]
    GameCenterAuthResponse_TicketsOneofCase_Ticket: _ClassVar[GameCenterAuthResponse_TicketsOneofCase]
    GameCenterAuthResponse_TicketsOneofCase_TicketBinary: _ClassVar[GameCenterAuthResponse_TicketsOneofCase]

class PropertySetByType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PropertySetByType_GameServer: _ClassVar[PropertySetByType]
    PropertySetByType_Client: _ClassVar[PropertySetByType]

class FacebookAuthResponse_TicketsOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FacebookAuthResponse_TicketsOneofCase_None: _ClassVar[FacebookAuthResponse_TicketsOneofCase]
    FacebookAuthResponse_TicketsOneofCase_Ticket: _ClassVar[FacebookAuthResponse_TicketsOneofCase]
    FacebookAuthResponse_TicketsOneofCase_TicketBinary: _ClassVar[FacebookAuthResponse_TicketsOneofCase]

class Property_ValueOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Property_ValueOneofCase_None: _ClassVar[Property_ValueOneofCase]
    Property_ValueOneofCase_IntValue: _ClassVar[Property_ValueOneofCase]
    Property_ValueOneofCase_FloatValue: _ClassVar[Property_ValueOneofCase]
    Property_ValueOneofCase_LongValue: _ClassVar[Property_ValueOneofCase]
    Property_ValueOneofCase_StringValue: _ClassVar[Property_ValueOneofCase]
    Property_ValueOneofCase_BooleanValue: _ClassVar[Property_ValueOneofCase]

class TestAuthResponse_TicketsOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TestAuthResponse_TicketsOneofCase_None: _ClassVar[TestAuthResponse_TicketsOneofCase]
    TestAuthResponse_TicketsOneofCase_Ticket: _ClassVar[TestAuthResponse_TicketsOneofCase]
    TestAuthResponse_TicketsOneofCase_TicketBinary: _ClassVar[TestAuthResponse_TicketsOneofCase]

class Filter_ValueOneofCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Filter_ValueOneofCase_None: _ClassVar[Filter_ValueOneofCase]
    Filter_ValueOneofCase_IntValue: _ClassVar[Filter_ValueOneofCase]
    Filter_ValueOneofCase_FloatValue: _ClassVar[Filter_ValueOneofCase]
    Filter_ValueOneofCase_StringValue: _ClassVar[Filter_ValueOneofCase]
    Filter_ValueOneofCase_Strings: _ClassVar[Filter_ValueOneofCase]

class Comparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Comparison_Equals: _ClassVar[Comparison]
    Comparison_NotEquals: _ClassVar[Comparison]
    Comparison_GreaterThan: _ClassVar[Comparison]
    Comparison_GreaterThanOrEqual: _ClassVar[Comparison]
    Comparison_LessThan: _ClassVar[Comparison]
    Comparison_LessThanOrEqual: _ClassVar[Comparison]
    Comparison_In: _ClassVar[Comparison]
    Comparison_NotIn: _ClassVar[Comparison]
ProcessingState_Creating: ProcessingState
ProcessingState_Cancelling: ProcessingState
ProcessingState_Expiring: ProcessingState
OperationValuePair_ValueOneofCase_None: OperationValuePair_ValueOneofCase
OperationValuePair_ValueOneofCase_IntValue: OperationValuePair_ValueOneofCase
OperationValuePair_ValueOneofCase_BoolValue: OperationValuePair_ValueOneofCase
LobbyType_Default: LobbyType
LobbyType_SqlLobby: LobbyType
LobbyType_AsyncRandomLobby: LobbyType
RequestType_NoneTypeRequest: RequestType
RequestType_OpenRequest: RequestType
RequestType_ClosedRequest: RequestType
PropertyType_None: PropertyType
PropertyType_Game: PropertyType
PropertyType_Actor: PropertyType
PropertyType_GameAndActor: PropertyType
OperationValuePair_Types_Operation_Default: OperationValuePair_Types_Operation
OperationValuePair_Types_Operation_Exist: OperationValuePair_Types_Operation
OperationValuePair_Types_Operation_Equals: OperationValuePair_Types_Operation
OnlineStatus_StateOffline: OnlineStatus
OnlineStatus_StateOnline: OnlineStatus
OnlineStatus_StateBusy: OnlineStatus
OnlineStatus_StateAway: OnlineStatus
OnlineStatus_StateSnooze: OnlineStatus
OnlineStatus_StateLookingToTrade: OnlineStatus
OnlineStatus_StateLookingToPlay: OnlineStatus
MarketRequestType_MpNoneType: MarketRequestType
MarketRequestType_SaleRequest: MarketRequestType
MarketRequestType_PurchaseRequest: MarketRequestType
ClanMemberRolePermission_ChangeClanSettings: ClanMemberRolePermission
ClanMemberRolePermission_AcceptMember: ClanMemberRolePermission
ClanMemberRolePermission_InviteMember: ClanMemberRolePermission
ClanMemberRolePermission_KickMemberLess: ClanMemberRolePermission
ClanMemberRolePermission_KickMemberEqual: ClanMemberRolePermission
ClanMemberRolePermission_AssignRoleLess: ClanMemberRolePermission
ClanMemberRolePermission_AssignRoleEqual: ClanMemberRolePermission
ClanMemberRolePermission_CreateClanBattle: ClanMemberRolePermission
ClanMemberRolePermission_JoinClanBattle: ClanMemberRolePermission
ClanMemberRolePermission_UpgradeClanMembersCount: ClanMemberRolePermission
ClanType_Closed: ClanType
ClanType_ByRequest: ClanType
ClanType_Opened: ClanType
RetrievableType_Unremovable: RetrievableType
RetrievableType_Removable: RetrievableType
RetrievableType_Retrievable: RetrievableType
GoogleAuthResponse_TicketsOneofCase_None: GoogleAuthResponse_TicketsOneofCase
GoogleAuthResponse_TicketsOneofCase_Ticket: GoogleAuthResponse_TicketsOneofCase
GoogleAuthResponse_TicketsOneofCase_TicketBinary: GoogleAuthResponse_TicketsOneofCase
JoinClanType_ByAcceptInviteRequest: JoinClanType
JoinClanType_ByAcceptJoinRequest: JoinClanType
JoinClanType_JoinToOpenClan: JoinClanType
JoinClanType_NoneJoinType: JoinClanType
BanScope_Global: BanScope
BanScope_Marketplace: BanScope
BanScope_MarketplaceSpecial: BanScope
BanScope_Chat: BanScope
BoltIdAuthResponse_TicketsOneofCase_None: BoltIdAuthResponse_TicketsOneofCase
BoltIdAuthResponse_TicketsOneofCase_Ticket: BoltIdAuthResponse_TicketsOneofCase
BoltIdAuthResponse_TicketsOneofCase_TicketBinary: BoltIdAuthResponse_TicketsOneofCase
OfferType_InappPurchase: OfferType
OfferType_Store: OfferType
LobbyPlayerType_Any: LobbyPlayerType
LobbyPlayerType_Member: LobbyPlayerType
LobbyPlayerType_Spectator: LobbyPlayerType
StatDefType_Int: StatDefType
StatDefType_Float: StatDefType
StatDefType_Long: StatDefType
VkAuthResponse_TicketsOneofCase_None: VkAuthResponse_TicketsOneofCase
VkAuthResponse_TicketsOneofCase_Ticket: VkAuthResponse_TicketsOneofCase
VkAuthResponse_TicketsOneofCase_TicketBinary: VkAuthResponse_TicketsOneofCase
SettingType_String: SettingType
SettingType_Integer: SettingType
SettingType_Float: SettingType
SettingType_Bool: SettingType
SettingType_Long: SettingType
ClosingReason_NoneReason: ClosingReason
ClosingReason_SuccessTransaction: ClosingReason
ClosingReason_NotEnoughFunds: ClosingReason
ClosingReason_Cancelled: ClosingReason
ClosingReason_SaleRequestNotFound: ClosingReason
ClosingReason_Expired: ClosingReason
ClosingReason_InventorySizeExceeded: ClosingReason
ExternalPlatform_Default: ExternalPlatform
ExternalPlatform_Vk: ExternalPlatform
ExternalPlatform_Facebook: ExternalPlatform
ExternalPlatform_Youtube: ExternalPlatform
ExternalPlatform_TikTok: ExternalPlatform
ExternalPlatform_Instagram: ExternalPlatform
ExternalPlatform_Twitter: ExternalPlatform
ExternalPlatform_Discord: ExternalPlatform
SystemMessageType_MatchesCanceled: SystemMessageType
SystemMessageType_ReportedPlayersBanned: SystemMessageType
SystemMessageType_FriendshipRequestAccepted: SystemMessageType
SystemMessageType_ClanMembershipAccepted: SystemMessageType
SystemMessageType_ClanMembershipEnded: SystemMessageType
SystemMessageType_AchievementUnlocked: SystemMessageType
SystemMessageType_GiftReceived: SystemMessageType
SystemMessageType_SeasonFinished: SystemMessageType
SystemMessageType_AvatarRejected: SystemMessageType
SystemMessageType_GlobalBanReceived: SystemMessageType
SystemMessageType_MarketplaceTransactionReverted: SystemMessageType
SystemMessageType_DeveloperMessage: SystemMessageType
SystemMessageType_MarketplaceBanReceived: SystemMessageType
SystemMessageType_ChatBanReceived: SystemMessageType
SystemMessageType_InappSucceed: SystemMessageType
SystemMessageType_NewDeviceLogined: SystemMessageType
SystemMessageType_MatchesRestored: SystemMessageType
Platform_Win32S: Platform
Platform_Win32Windows: Platform
Platform_Win32NT: Platform
Platform_WinCE: Platform
Platform_Unix: Platform
Platform_Xbox: Platform
Platform_MacOSX: Platform
MessageType_ClansNoneType: MessageType
MessageType_ChatMessage: MessageType
MessageType_LogMessage: MessageType
Store_GooglePlay: Store
Store_AppStore: Store
Store_AppGallery: Store
Store_Amazon: Store
Store_Dev: Store
Store_Yoo: Store
ProgressGameEventType_Unspecified: ProgressGameEventType
ProgressGameEventType_GamePassBought: ProgressGameEventType
ProgressGameEventType_EventPointsBought: ProgressGameEventType
ProgressGameEventType_GamePassAndEventPointsBought: ProgressGameEventType
BHBHHDGDFCHFACH_Unknown: BHBHHDGDFCHFACH
BHBHHDGDFCHFACH_GroupWaitTimeout: BHBHHDGDFCHFACH
BHBHHDGDFCHFACH_GroupMemberDisconnected: BHBHHDGDFCHFACH
BHBHHDGDFCHFACH_GroupMemberNotConfirmed: BHBHHDGDFCHFACH
BHBHHDGDFCHFACH_GroupMemberIsNotOneClan: BHBHHDGDFCHFACH
MatchState_Finished: MatchState
MatchState_Canceled: MatchState
MatchState_Annulled: MatchState
RelationshipStatus_None: RelationshipStatus
RelationshipStatus_Blocked: RelationshipStatus
RelationshipStatus_Initiator: RelationshipStatus
RelationshipStatus_Friend: RelationshipStatus
RelationshipStatus_Recipient: RelationshipStatus
RelationshipStatus_Ignored: RelationshipStatus
HuaweiAuthResponse_TicketsOneofCase_None: HuaweiAuthResponse_TicketsOneofCase
HuaweiAuthResponse_TicketsOneofCase_Ticket: HuaweiAuthResponse_TicketsOneofCase
HuaweiAuthResponse_TicketsOneofCase_TicketBinary: HuaweiAuthResponse_TicketsOneofCase
AppleIdAuthResponse_TicketsOneofCase_None: AppleIdAuthResponse_TicketsOneofCase
AppleIdAuthResponse_TicketsOneofCase_Ticket: AppleIdAuthResponse_TicketsOneofCase
AppleIdAuthResponse_TicketsOneofCase_TicketBinary: AppleIdAuthResponse_TicketsOneofCase
MatchType_Simple: MatchType
MatchType_Win32: MatchType
AuthType_Test: AuthType
AuthType_Guest: AuthType
AuthType_GooglePlay: AuthType
AuthType_Facebook: AuthType
AuthType_GameCenter: AuthType
AuthType_AppleId: AuthType
AuthType_Huawei: AuthType
AuthType_Vk: AuthType
AuthType_BoltId: AuthType
GameCenterAuthResponse_TicketsOneofCase_None: GameCenterAuthResponse_TicketsOneofCase
GameCenterAuthResponse_TicketsOneofCase_Ticket: GameCenterAuthResponse_TicketsOneofCase
GameCenterAuthResponse_TicketsOneofCase_TicketBinary: GameCenterAuthResponse_TicketsOneofCase
PropertySetByType_GameServer: PropertySetByType
PropertySetByType_Client: PropertySetByType
FacebookAuthResponse_TicketsOneofCase_None: FacebookAuthResponse_TicketsOneofCase
FacebookAuthResponse_TicketsOneofCase_Ticket: FacebookAuthResponse_TicketsOneofCase
FacebookAuthResponse_TicketsOneofCase_TicketBinary: FacebookAuthResponse_TicketsOneofCase
Property_ValueOneofCase_None: Property_ValueOneofCase
Property_ValueOneofCase_IntValue: Property_ValueOneofCase
Property_ValueOneofCase_FloatValue: Property_ValueOneofCase
Property_ValueOneofCase_LongValue: Property_ValueOneofCase
Property_ValueOneofCase_StringValue: Property_ValueOneofCase
Property_ValueOneofCase_BooleanValue: Property_ValueOneofCase
TestAuthResponse_TicketsOneofCase_None: TestAuthResponse_TicketsOneofCase
TestAuthResponse_TicketsOneofCase_Ticket: TestAuthResponse_TicketsOneofCase
TestAuthResponse_TicketsOneofCase_TicketBinary: TestAuthResponse_TicketsOneofCase
Filter_ValueOneofCase_None: Filter_ValueOneofCase
Filter_ValueOneofCase_IntValue: Filter_ValueOneofCase
Filter_ValueOneofCase_FloatValue: Filter_ValueOneofCase
Filter_ValueOneofCase_StringValue: Filter_ValueOneofCase
Filter_ValueOneofCase_Strings: Filter_ValueOneofCase
Comparison_Equals: Comparison
Comparison_NotEquals: Comparison
Comparison_GreaterThan: Comparison
Comparison_GreaterThanOrEqual: Comparison
Comparison_LessThan: Comparison
Comparison_LessThanOrEqual: Comparison
Comparison_In: Comparison
Comparison_NotIn: Comparison

class RequestToJoinClanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BoltIdUnLinkAuthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClanJoinRequestsCountResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class StorePlayerStatsRequest(_message.Message):
    __slots__ = ("storePlayerStats",)
    STOREPLAYERSTATS_FIELD_NUMBER: _ClassVar[int]
    storePlayerStats: StorePlayerStats
    def __init__(self, storePlayerStats: _Optional[_Union[StorePlayerStats, _Mapping]] = ...) -> None: ...

class GetLastRateGameResponse(_message.Message):
    __slots__ = ("rate", "message", "internalData", "context", "timestampAskLater", "dontAskLater", "timestamp", "rateContexts", "reward")
    RATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPASKLATER_FIELD_NUMBER: _ClassVar[int]
    DONTASKLATER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RATECONTEXTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    rate: int
    message: str
    internalData: str
    context: str
    timestampAskLater: int
    dontAskLater: bool
    timestamp: int
    rateContexts: _containers.RepeatedCompositeFieldContainer[RateContext]
    reward: RewardInfo
    def __init__(self, rate: _Optional[int] = ..., message: _Optional[str] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ..., timestampAskLater: _Optional[int] = ..., dontAskLater: bool = ..., timestamp: _Optional[int] = ..., rateContexts: _Optional[_Iterable[_Union[RateContext, _Mapping]]] = ..., reward: _Optional[_Union[RewardInfo, _Mapping]] = ...) -> None: ...

class CreatePurchaseRequestResponse(_message.Message):
    __slots__ = ("purchaseRequestId",)
    PURCHASEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    purchaseRequestId: str
    def __init__(self, purchaseRequestId: _Optional[str] = ...) -> None: ...

class CreateSaleResponse(_message.Message):
    __slots__ = ("requestId",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class OnPlayerStatusChangedEvent(_message.Message):
    __slots__ = ("friendGpid", "newStatus")
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    NEWSTATUS_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    newStatus: PlayerStatus
    def __init__(self, friendGpid: _Optional[str] = ..., newStatus: _Optional[_Union[PlayerStatus, _Mapping]] = ...) -> None: ...

class GetCurrentClanStatsForSeasonResponse(_message.Message):
    __slots__ = ("clanStats", "clanMemberStats")
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    clanStats: ClanStats
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[ClanMemberStats]
    def __init__(self, clanStats: _Optional[_Union[ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[ClanMemberStats, _Mapping]]] = ...) -> None: ...

class GetCurrentStatsResponse(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: Stats
    def __init__(self, stats: _Optional[_Union[Stats, _Mapping]] = ...) -> None: ...

class SetInventoryItemFlagsRequest(_message.Message):
    __slots__ = ("itemFlags",)
    ITEMFLAGS_FIELD_NUMBER: _ClassVar[int]
    itemFlags: ItemFlags
    def __init__(self, itemFlags: _Optional[_Union[ItemFlags, _Mapping]] = ...) -> None: ...

class SetLobbyJoinableResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HuaweiUnLinkAuthResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetInventoryItemFlagsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPlayerInviteRequestsRequest(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class GetPlayerSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPlayerRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AppleIdLinkAuthResponse(_message.Message):
    __slots__ = ("guestLinking",)
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class CancelJoinRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetLobbyTypeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteClosedInviteRequestRequest(_message.Message):
    __slots__ = ("requestId",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class SetOnlineStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUnreadLogMessagesCountRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAccountRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class OnAdRewardEvent(_message.Message):
    __slots__ = ("rewardCurrencies", "rewardItems", "ignore")
    REWARDCURRENCIES_FIELD_NUMBER: _ClassVar[int]
    REWARDITEMS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_FIELD_NUMBER: _ClassVar[int]
    rewardCurrencies: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    rewardItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    ignore: bool
    def __init__(self, rewardCurrencies: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., rewardItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., ignore: bool = ...) -> None: ...

class GetLobbyResponse(_message.Message):
    __slots__ = ("lobby",)
    LOBBY_FIELD_NUMBER: _ClassVar[int]
    lobby: Lobby
    def __init__(self, lobby: _Optional[_Union[Lobby, _Mapping]] = ...) -> None: ...

class OnJoinRequestCancelledEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValidateClanNameResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BoltIdAuthResponse(_message.Message):
    __slots__ = ("ticketsCase",)
    TICKETSCASE_FIELD_NUMBER: _ClassVar[int]
    ticketsCase: BoltIdAuthResponse_TicketsOneofCase
    def __init__(self, ticketsCase: _Optional[_Union[BoltIdAuthResponse_TicketsOneofCase, str]] = ...) -> None: ...

class FindClanRequest(_message.Message):
    __slots__ = ("filter", "page", "size")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filter: str
    page: int
    size: int
    def __init__(self, filter: _Optional[str] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetInvitesToLobbyResponse(_message.Message):
    __slots__ = ("lobbyInvites",)
    LOBBYINVITES_FIELD_NUMBER: _ClassVar[int]
    lobbyInvites: _containers.RepeatedCompositeFieldContainer[LobbyInvite]
    def __init__(self, lobbyInvites: _Optional[_Iterable[_Union[LobbyInvite, _Mapping]]] = ...) -> None: ...

class GetPlayerFriendsRequest(_message.Message):
    __slots__ = ("relationshipStatuses", "page", "size")
    RELATIONSHIPSTATUSES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    relationshipStatuses: _containers.RepeatedScalarFieldContainer[RelationshipStatus]
    page: int
    size: int
    def __init__(self, relationshipStatuses: _Optional[_Iterable[_Union[RelationshipStatus, str]]] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetUnreadChatMessagesCountRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VkUnLinkAuthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetLobbyMaxSpectatorsRequest(_message.Message):
    __slots__ = ("maxSpectators",)
    MAXSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    maxSpectators: int
    def __init__(self, maxSpectators: _Optional[int] = ...) -> None: ...

class AssignLeaderRoleRequest(_message.Message):
    __slots__ = ("newLeaderMemberId", "roleId")
    NEWLEADERMEMBERID_FIELD_NUMBER: _ClassVar[int]
    ROLEID_FIELD_NUMBER: _ClassVar[int]
    newLeaderMemberId: str
    roleId: int
    def __init__(self, newLeaderMemberId: _Optional[str] = ..., roleId: _Optional[int] = ...) -> None: ...

class GetFriendMsgsByOffsetRequest(_message.Message):
    __slots__ = ("friendGpid", "offset")
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    offset: Offset
    def __init__(self, friendGpid: _Optional[str] = ..., offset: _Optional[_Union[Offset, _Mapping]] = ...) -> None: ...

class GetPlayerInventoryRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendClanChatMessageRequest(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class EEBEGEFGBEBEGEH(_message.Message):
    __slots__ = ("CHFFAAGAGAFBEHE", "AHEABGBEHEGHDED")
    CHFFAAGAGAFBEHE_FIELD_NUMBER: _ClassVar[int]
    AHEABGBEHEGHDED_FIELD_NUMBER: _ClassVar[int]
    CHFFAAGAGAFBEHE: int
    AHEABGBEHEGHDED: AAGDEBAFFCFGFCH
    def __init__(self, CHFFAAGAGAFBEHE: _Optional[int] = ..., AHEABGBEHEGHDED: _Optional[_Union[AAGDEBAFFCFGFCH, _Mapping]] = ...) -> None: ...

class OnLobbyDataChangedEvent(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: Dictionary
    def __init__(self, data: _Optional[_Union[Dictionary, _Mapping]] = ...) -> None: ...

class HuaweiLinkAuthResponse(_message.Message):
    __slots__ = ("guestLinking",)
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class AppGalleryBuyInappResponse(_message.Message):
    __slots__ = ("reward",)
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: GivenReward
    def __init__(self, reward: _Optional[_Union[GivenReward, _Mapping]] = ...) -> None: ...

class OnIncomingClanChatMessageEvent(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: ClanUserMessage
    def __init__(self, message: _Optional[_Union[ClanUserMessage, _Mapping]] = ...) -> None: ...

class HandshakeResponse(_message.Message):
    __slots__ = ("country",)
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    country: str
    def __init__(self, country: _Optional[str] = ...) -> None: ...

class SetPlayerAvatarResponse(_message.Message):
    __slots__ = ("avatarId",)
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    def __init__(self, avatarId: _Optional[str] = ...) -> None: ...

class CancelJoinRequestRequest(_message.Message):
    __slots__ = ("requestId",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class SendFriendMsgRequest(_message.Message):
    __slots__ = ("friendGpid", "msg")
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    msg: str
    def __init__(self, friendGpid: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class GetClanMembersByIdRequest(_message.Message):
    __slots__ = ("clanId",)
    CLANID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    def __init__(self, clanId: _Optional[str] = ...) -> None: ...

class OnSystemMessageReceivedEvent(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: SystemMessageDetails
    def __init__(self, message: _Optional[_Union[SystemMessageDetails, _Mapping]] = ...) -> None: ...

class OnAssignedRoleEvent(_message.Message):
    __slots__ = ("newRoleId", "assignatorMemberId", "assigneeMemberId")
    NEWROLEID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNATORMEMBERID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEEMEMBERID_FIELD_NUMBER: _ClassVar[int]
    newRoleId: int
    assignatorMemberId: str
    assigneeMemberId: str
    def __init__(self, newRoleId: _Optional[int] = ..., assignatorMemberId: _Optional[str] = ..., assigneeMemberId: _Optional[str] = ...) -> None: ...

class GetPlayerOpenRequestsResponse(_message.Message):
    __slots__ = ("openRequests",)
    OPENREQUESTS_FIELD_NUMBER: _ClassVar[int]
    openRequests: _containers.RepeatedCompositeFieldContainer[OpenRequest]
    def __init__(self, openRequests: _Optional[_Iterable[_Union[OpenRequest, _Mapping]]] = ...) -> None: ...

class CreateSaleRequest(_message.Message):
    __slots__ = ("itemId", "price")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    itemId: int
    price: float
    def __init__(self, itemId: _Optional[int] = ..., price: _Optional[float] = ...) -> None: ...

class CreatePurchaseRequestBySaleResponse(_message.Message):
    __slots__ = ("purchaseRequestId",)
    PURCHASEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    purchaseRequestId: str
    def __init__(self, purchaseRequestId: _Optional[str] = ...) -> None: ...

class GetPlayerInviteRequestsCountResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class CancelInviteRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnProgressGameEvent(_message.Message):
    __slots__ = ("eventId", "points", "levels", "reward", "context", "levelsToClaimReward")
    class LevelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LevelsToClaimRewardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ListOfLevelsToClaimReward
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ListOfLevelsToClaimReward, _Mapping]] = ...) -> None: ...
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    eventId: str
    points: int
    levels: _containers.ScalarMap[str, int]
    reward: GivenReward
    context: ProgressGameEventContext
    levelsToClaimReward: _containers.MessageMap[str, ListOfLevelsToClaimReward]
    def __init__(self, eventId: _Optional[str] = ..., points: _Optional[int] = ..., levels: _Optional[_Mapping[str, int]] = ..., reward: _Optional[_Union[GivenReward, _Mapping]] = ..., context: _Optional[_Union[ProgressGameEventContext, _Mapping]] = ..., levelsToClaimReward: _Optional[_Mapping[str, ListOfLevelsToClaimReward]] = ...) -> None: ...

class RefuseInvitationToLobbyRequest(_message.Message):
    __slots__ = ("lobbyId",)
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    def __init__(self, lobbyId: _Optional[str] = ...) -> None: ...

class GetItemsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class SetPlayerSettingsRequest(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: PlayerSettings
    def __init__(self, settings: _Optional[_Union[PlayerSettings, _Mapping]] = ...) -> None: ...

class OnClanTagAndNameChanged(_message.Message):
    __slots__ = ("newClanTag", "newClanName")
    NEWCLANTAG_FIELD_NUMBER: _ClassVar[int]
    NEWCLANNAME_FIELD_NUMBER: _ClassVar[int]
    newClanTag: str
    newClanName: str
    def __init__(self, newClanTag: _Optional[str] = ..., newClanName: _Optional[str] = ...) -> None: ...

class DeleteClosedJoinRequestRequest(_message.Message):
    __slots__ = ("requestId",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class GetClanByIdRequest(_message.Message):
    __slots__ = ("clanId",)
    CLANID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    def __init__(self, clanId: _Optional[str] = ...) -> None: ...

class GetPlayerFriendByIdResponse(_message.Message):
    __slots__ = ("playerFriend",)
    PLAYERFRIEND_FIELD_NUMBER: _ClassVar[int]
    playerFriend: PlayerFriend
    def __init__(self, playerFriend: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class BoltIdUnLinkAuthResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOtherPlayerItemsRequest(_message.Message):
    __slots__ = ("gpid", "itemDefinitionIds")
    GPID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONIDS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    itemDefinitionIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gpid: _Optional[str] = ..., itemDefinitionIds: _Optional[_Iterable[int]] = ...) -> None: ...

class SetClanAvatarResponse(_message.Message):
    __slots__ = ("avatarId",)
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    def __init__(self, avatarId: _Optional[str] = ...) -> None: ...

class SendLobbyChatMsgResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LeaveClanRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GameCenterLinkAuthResponse(_message.Message):
    __slots__ = ("guestLinking",)
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class FacebookAuthRequest(_message.Message):
    __slots__ = ("authFacebook", "appVerification", "deviceInfo")
    AUTHFACEBOOK_FIELD_NUMBER: _ClassVar[int]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    authFacebook: AuthFacebook
    appVerification: AppVerification
    deviceInfo: DeviceInfo
    def __init__(self, authFacebook: _Optional[_Union[AuthFacebook, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class GetSpecialOffersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnPlayerRequestOpenedEvent(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: OpenRequest
    def __init__(self, request: _Optional[_Union[OpenRequest, _Mapping]] = ...) -> None: ...

class OnInviteRequestCancelledEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInventoryItemPropertyDefinitionsRequest(_message.Message):
    __slots__ = ("lastUpdated",)
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    lastUpdated: str
    def __init__(self, lastUpdated: _Optional[str] = ...) -> None: ...

class ReadFriendMsgsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateClanResponse(_message.Message):
    __slots__ = ("clan",)
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: Clan
    def __init__(self, clan: _Optional[_Union[Clan, _Mapping]] = ...) -> None: ...

class GetFriendMsgsByOffsetResponse(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[UserMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[UserMessage, _Mapping]]] = ...) -> None: ...

class ChangeClanTypeRequest(_message.Message):
    __slots__ = ("clanType",)
    CLANTYPE_FIELD_NUMBER: _ClassVar[int]
    clanType: ClanType
    def __init__(self, clanType: _Optional[_Union[ClanType, str]] = ...) -> None: ...

class OnStatsUpdatedEvent(_message.Message):
    __slots__ = ("updatedStats", "updatedDate")
    UPDATEDSTATS_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    updatedStats: _containers.RepeatedCompositeFieldContainer[PlayerStat]
    updatedDate: int
    def __init__(self, updatedStats: _Optional[_Iterable[_Union[PlayerStat, _Mapping]]] = ..., updatedDate: _Optional[int] = ...) -> None: ...

class GetPlayerStatsRequest(_message.Message):
    __slots__ = ("gpid", "apiNames", "addLeaderboardStats")
    GPID_FIELD_NUMBER: _ClassVar[int]
    APINAMES_FIELD_NUMBER: _ClassVar[int]
    ADDLEADERBOARDSTATS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    apiNames: _containers.RepeatedScalarFieldContainer[str]
    addLeaderboardStats: bool
    def __init__(self, gpid: _Optional[str] = ..., apiNames: _Optional[_Iterable[str]] = ..., addLeaderboardStats: bool = ...) -> None: ...

class OnPlayerNameChangedEvent(_message.Message):
    __slots__ = ("gpid", "name")
    GPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    name: str
    def __init__(self, gpid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetPlayerClosedJoinRequestsCountResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class UnblockFriendResponse(_message.Message):
    __slots__ = ("relationshipStatus",)
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class GetTradeResponse(_message.Message):
    __slots__ = ("trade",)
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class SendClanChatMessageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GameCenterUnLinkAuthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLobbyRequest(_message.Message):
    __slots__ = ("lobbyId",)
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    def __init__(self, lobbyId: _Optional[str] = ...) -> None: ...

class InvitePlayerToLobbyAsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetPlayerSettingsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnJoinRequestTakenEvent(_message.Message):
    __slots__ = ("requestId", "player")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    player: Player
    def __init__(self, requestId: _Optional[str] = ..., player: _Optional[_Union[Player, _Mapping]] = ...) -> None: ...

class OnNewPlayerInvitedToLobbyEvent(_message.Message):
    __slots__ = ("inviteSenderGpid", "newPlayer")
    INVITESENDERGPID_FIELD_NUMBER: _ClassVar[int]
    NEWPLAYER_FIELD_NUMBER: _ClassVar[int]
    inviteSenderGpid: str
    newPlayer: PlayerFriend
    def __init__(self, inviteSenderGpid: _Optional[str] = ..., newPlayer: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class SetClanAvatarRequest(_message.Message):
    __slots__ = ("avatar",)
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    avatar: bytes
    def __init__(self, avatar: _Optional[bytes] = ...) -> None: ...

class GetSystemMessagesResponse(_message.Message):
    __slots__ = ("messages", "continuationToken")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    CONTINUATIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[SystemMessagePreview]
    continuationToken: str
    def __init__(self, messages: _Optional[_Iterable[_Union[SystemMessagePreview, _Mapping]]] = ..., continuationToken: _Optional[str] = ...) -> None: ...

class AskLaterRequest(_message.Message):
    __slots__ = ("timestampAskLater", "internalData", "context")
    TIMESTAMPASKLATER_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    timestampAskLater: int
    internalData: str
    context: str
    def __init__(self, timestampAskLater: _Optional[int] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...

class DeleteClosedInviteRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSpecialOffersResponse(_message.Message):
    __slots__ = ("specialOffers",)
    SPECIALOFFERS_FIELD_NUMBER: _ClassVar[int]
    specialOffers: _containers.RepeatedCompositeFieldContainer[SpecialOffer]
    def __init__(self, specialOffers: _Optional[_Iterable[_Union[SpecialOffer, _Mapping]]] = ...) -> None: ...

class GetClanSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnRefuseInviteToLobbyEvent(_message.Message):
    __slots__ = ("inviteSenderGpid", "invitedGpid")
    INVITESENDERGPID_FIELD_NUMBER: _ClassVar[int]
    INVITEDGPID_FIELD_NUMBER: _ClassVar[int]
    inviteSenderGpid: str
    invitedGpid: str
    def __init__(self, inviteSenderGpid: _Optional[str] = ..., invitedGpid: _Optional[str] = ...) -> None: ...

class KickPlayerFromLobbyRequest(_message.Message):
    __slots__ = ("kickedGpid",)
    KICKEDGPID_FIELD_NUMBER: _ClassVar[int]
    kickedGpid: str
    def __init__(self, kickedGpid: _Optional[str] = ...) -> None: ...

class GetClanJoinRequestsCountRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetLobbyPhotonGameRequest(_message.Message):
    __slots__ = ("photonGame",)
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    photonGame: PhotonGame
    def __init__(self, photonGame: _Optional[_Union[PhotonGame, _Mapping]] = ...) -> None: ...

class GetCurrentPlayerAchievementsRequest(_message.Message):
    __slots__ = ("showLocked",)
    SHOWLOCKED_FIELD_NUMBER: _ClassVar[int]
    showLocked: bool
    def __init__(self, showLocked: bool = ...) -> None: ...

class DeleteSystemMessagesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnKickedEvent(_message.Message):
    __slots__ = ("kickingReason",)
    KICKINGREASON_FIELD_NUMBER: _ClassVar[int]
    kickingReason: str
    def __init__(self, kickingReason: _Optional[str] = ...) -> None: ...

class SetPlayerAvatarRequest(_message.Message):
    __slots__ = ("avatar",)
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    avatar: bytes
    def __init__(self, avatar: _Optional[bytes] = ...) -> None: ...

class OnLobbyTypeChangedEvent(_message.Message):
    __slots__ = ("lobbyType",)
    LOBBYTYPE_FIELD_NUMBER: _ClassVar[int]
    lobbyType: LobbyType
    def __init__(self, lobbyType: _Optional[_Union[LobbyType, str]] = ...) -> None: ...

class GetPlayerAchievementsResponse(_message.Message):
    __slots__ = ("playerAchievement",)
    PLAYERACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    playerAchievement: _containers.RepeatedCompositeFieldContainer[PlayerAchievement]
    def __init__(self, playerAchievement: _Optional[_Iterable[_Union[PlayerAchievement, _Mapping]]] = ...) -> None: ...

class TestAuthRequest(_message.Message):
    __slots__ = ("authTest", "verification", "deviceInfo")
    AUTHTEST_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    authTest: AuthTest
    verification: AppVerification
    deviceInfo: DeviceInfo
    def __init__(self, authTest: _Optional[_Union[AuthTest, _Mapping]] = ..., verification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class CreatePurchaseRequestBySaleRequest(_message.Message):
    __slots__ = ("saleId",)
    SALEID_FIELD_NUMBER: _ClassVar[int]
    saleId: str
    def __init__(self, saleId: _Optional[str] = ...) -> None: ...

class GetPlayerFriendsIdsResponse(_message.Message):
    __slots__ = ("friendGpids",)
    FRIENDGPIDS_FIELD_NUMBER: _ClassVar[int]
    friendGpids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, friendGpids: _Optional[_Iterable[str]] = ...) -> None: ...

class AcceptFriendRequestResponse(_message.Message):
    __slots__ = ("relationshipStatus",)
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class ProgressChallengeResponse(_message.Message):
    __slots__ = ("completed", "challengePoints", "challengeReward", "eventPoints", "eventGamePassLevels", "eventReward", "rewardsObtained")
    class EventGamePassLevelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEPOINTS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEREWARD_FIELD_NUMBER: _ClassVar[int]
    EVENTPOINTS_FIELD_NUMBER: _ClassVar[int]
    EVENTGAMEPASSLEVELS_FIELD_NUMBER: _ClassVar[int]
    EVENTREWARD_FIELD_NUMBER: _ClassVar[int]
    REWARDSOBTAINED_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    challengePoints: int
    challengeReward: GivenReward
    eventPoints: int
    eventGamePassLevels: _containers.ScalarMap[str, int]
    eventReward: GivenReward
    rewardsObtained: bool
    def __init__(self, completed: bool = ..., challengePoints: _Optional[int] = ..., challengeReward: _Optional[_Union[GivenReward, _Mapping]] = ..., eventPoints: _Optional[int] = ..., eventGamePassLevels: _Optional[_Mapping[str, int]] = ..., eventReward: _Optional[_Union[GivenReward, _Mapping]] = ..., rewardsObtained: bool = ...) -> None: ...

class CountUnreadSystemMessagesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IgnoreFriendRequestRequest(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class OnLobbyPlayerTypeChangedEvent(_message.Message):
    __slots__ = ("gpid", "playerType")
    GPID_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    playerType: LobbyPlayerType
    def __init__(self, gpid: _Optional[str] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ...) -> None: ...

class FacebookLinkAuthResponse(_message.Message):
    __slots__ = ("guestLinking",)
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class ChangeLobbyOtherPlayerTypeRequest(_message.Message):
    __slots__ = ("gpid", "playerType")
    GPID_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    playerType: LobbyPlayerType
    def __init__(self, gpid: _Optional[str] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ...) -> None: ...

class GetCurrentPlayerAchievementsResponse(_message.Message):
    __slots__ = ("achievements",)
    ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    achievements: _containers.RepeatedCompositeFieldContainer[PlayerAchievement]
    def __init__(self, achievements: _Optional[_Iterable[_Union[PlayerAchievement, _Mapping]]] = ...) -> None: ...

class SetLobbyMaxMembersRequest(_message.Message):
    __slots__ = ("maxMembers",)
    MAXMEMBERS_FIELD_NUMBER: _ClassVar[int]
    maxMembers: int
    def __init__(self, maxMembers: _Optional[int] = ...) -> None: ...

class SearchPlayersRequest(_message.Message):
    __slots__ = ("value", "page", "size")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    value: str
    page: int
    size: int
    def __init__(self, value: _Optional[str] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GoogleUnLinkAuthResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AcceptFriendRequestRequest(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class GetClanRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GoogleUnLinkAuthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetPlayerFirebaseTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetChatUsersLiteResponse(_message.Message):
    __slots__ = ("chatUsers",)
    CHATUSERS_FIELD_NUMBER: _ClassVar[int]
    chatUsers: _containers.RepeatedCompositeFieldContainer[ChatUserLite]
    def __init__(self, chatUsers: _Optional[_Iterable[_Union[ChatUserLite, _Mapping]]] = ...) -> None: ...

class SearchPlayersResponse(_message.Message):
    __slots__ = ("playerFriends",)
    PLAYERFRIENDS_FIELD_NUMBER: _ClassVar[int]
    playerFriends: _containers.RepeatedCompositeFieldContainer[PlayerFriend]
    def __init__(self, playerFriends: _Optional[_Iterable[_Union[PlayerFriend, _Mapping]]] = ...) -> None: ...

class GetCachedPlayerGameEventsRequest(_message.Message):
    __slots__ = ("lastUpdated",)
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    lastUpdated: str
    def __init__(self, lastUpdated: _Optional[str] = ...) -> None: ...

class SearchLobbyRequest(_message.Message):
    __slots__ = ("amount", "filters", "version")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    amount: int
    filters: _containers.RepeatedCompositeFieldContainer[Filter]
    version: int
    def __init__(self, amount: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class DeleteFriendMsgsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPlayerStatsResponse(_message.Message):
    __slots__ = ("playerStats",)
    PLAYERSTATS_FIELD_NUMBER: _ClassVar[int]
    playerStats: PlayerStats
    def __init__(self, playerStats: _Optional[_Union[PlayerStats, _Mapping]] = ...) -> None: ...

class GetAchievementDefinitionsResponse(_message.Message):
    __slots__ = ("achievements",)
    ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    achievements: _containers.RepeatedCompositeFieldContainer[AchievementDefinition]
    def __init__(self, achievements: _Optional[_Iterable[_Union[AchievementDefinition, _Mapping]]] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("filename", "file", "type")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    filename: str
    file: bytes
    type: str
    def __init__(self, filename: _Optional[str] = ..., file: _Optional[bytes] = ..., type: _Optional[str] = ...) -> None: ...

class GetPlayerOpenRequestsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AppStoreBuyInappResponse(_message.Message):
    __slots__ = ("reward",)
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: PlayerInventory
    def __init__(self, reward: _Optional[_Union[PlayerInventory, _Mapping]] = ...) -> None: ...

class OnReceivedInviteToLobbyEvent(_message.Message):
    __slots__ = ("invite",)
    INVITE_FIELD_NUMBER: _ClassVar[int]
    invite: LobbyInvite
    def __init__(self, invite: _Optional[_Union[LobbyInvite, _Mapping]] = ...) -> None: ...

class GetPlayerGameEventsProgressesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeclineInviteRequestRequest(_message.Message):
    __slots__ = ("requestId",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class GetInvitesToLobbyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCachedPlayerGameEventsResponse(_message.Message):
    __slots__ = ("gameEvents", "lastUpdated", "msUntilRefresh")
    GAMEEVENTS_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    MSUNTILREFRESH_FIELD_NUMBER: _ClassVar[int]
    gameEvents: _containers.RepeatedCompositeFieldContainer[GameEventDefinition]
    lastUpdated: str
    msUntilRefresh: int
    def __init__(self, gameEvents: _Optional[_Iterable[_Union[GameEventDefinition, _Mapping]]] = ..., lastUpdated: _Optional[str] = ..., msUntilRefresh: _Optional[int] = ...) -> None: ...

class GetClanMembersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInventoryItemDefinitionsResponse(_message.Message):
    __slots__ = ("inventoryItemDefinitions", "lastUpdated")
    INVENTORYITEMDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    inventoryItemDefinitions: _containers.RepeatedCompositeFieldContainer[InventoryItemDefinition]
    lastUpdated: str
    def __init__(self, inventoryItemDefinitions: _Optional[_Iterable[_Union[InventoryItemDefinition, _Mapping]]] = ..., lastUpdated: _Optional[str] = ...) -> None: ...

class GetPlayerStatsForSeasonRequest(_message.Message):
    __slots__ = ("seasonId", "gpid")
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    seasonId: str
    gpid: str
    def __init__(self, seasonId: _Optional[str] = ..., gpid: _Optional[str] = ...) -> None: ...

class GetClanMembersByIdResponse(_message.Message):
    __slots__ = ("clanMembers",)
    CLANMEMBERS_FIELD_NUMBER: _ClassVar[int]
    clanMembers: _containers.RepeatedCompositeFieldContainer[ClanMember]
    def __init__(self, clanMembers: _Optional[_Iterable[_Union[ClanMember, _Mapping]]] = ...) -> None: ...

class AppGalleryBuyInappRequest(_message.Message):
    __slots__ = ("productId", "purchaseToken")
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    PURCHASETOKEN_FIELD_NUMBER: _ClassVar[int]
    productId: str
    purchaseToken: str
    def __init__(self, productId: _Optional[str] = ..., purchaseToken: _Optional[str] = ...) -> None: ...

class GetClanLogMessagesRequest(_message.Message):
    __slots__ = ("count",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ..., **kwargs) -> None: ...

class GetClanJoinRequestsRequest(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class UnmountInventoryItemRequest(_message.Message):
    __slots__ = ("modifiedItemId", "modificationName")
    MODIFIEDITEMID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONNAME_FIELD_NUMBER: _ClassVar[int]
    modifiedItemId: int
    modificationName: str
    def __init__(self, modifiedItemId: _Optional[int] = ..., modificationName: _Optional[str] = ...) -> None: ...

class GetTradesResponse(_message.Message):
    __slots__ = ("trades",)
    TRADES_FIELD_NUMBER: _ClassVar[int]
    trades: _containers.RepeatedCompositeFieldContainer[Trade]
    def __init__(self, trades: _Optional[_Iterable[_Union[Trade, _Mapping]]] = ...) -> None: ...

class CancelInviteRequestRequest(_message.Message):
    __slots__ = ("requestId",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class SubscribeCreatorRequest(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class VkLinkAuthResponse(_message.Message):
    __slots__ = ("guestLinking",)
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class CreateRequestEncryptedRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class ExecuteRecipeEncrypted2Response(_message.Message):
    __slots__ = ("exchangeResult",)
    EXCHANGERESULT_FIELD_NUMBER: _ClassVar[int]
    exchangeResult: ExchangeRecipeResult
    def __init__(self, exchangeResult: _Optional[_Union[ExchangeRecipeResult, _Mapping]] = ...) -> None: ...

class GetClanJoinRequestsResponse(_message.Message):
    __slots__ = ("clanJoinRequests",)
    CLANJOINREQUESTS_FIELD_NUMBER: _ClassVar[int]
    clanJoinRequests: _containers.RepeatedCompositeFieldContainer[ClanJoinRequest]
    def __init__(self, clanJoinRequests: _Optional[_Iterable[_Union[ClanJoinRequest, _Mapping]]] = ...) -> None: ...

class GetTradeOpenSaleRequestsResponse(_message.Message):
    __slots__ = ("openRequests",)
    OPENREQUESTS_FIELD_NUMBER: _ClassVar[int]
    openRequests: _containers.RepeatedCompositeFieldContainer[OpenRequest]
    def __init__(self, openRequests: _Optional[_Iterable[_Union[OpenRequest, _Mapping]]] = ...) -> None: ...

class ReadClanLogMessagesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClanChatMessagesResponse(_message.Message):
    __slots__ = ("clanUserMessage",)
    CLANUSERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    clanUserMessage: _containers.RepeatedCompositeFieldContainer[ClanUserMessage]
    def __init__(self, clanUserMessage: _Optional[_Iterable[_Union[ClanUserMessage, _Mapping]]] = ...) -> None: ...

class SetLobbyTypeRequest(_message.Message):
    __slots__ = ("lobbyType",)
    LOBBYTYPE_FIELD_NUMBER: _ClassVar[int]
    lobbyType: LobbyType
    def __init__(self, lobbyType: _Optional[_Union[LobbyType, str]] = ...) -> None: ...

class GetPlayerClosedJoinRequestsCountRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnsubscribeRequest(_message.Message):
    __slots__ = ("topic",)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str
    def __init__(self, topic: _Optional[str] = ...) -> None: ...

class GetCurrentClanStatsRequest(_message.Message):
    __slots__ = ("addLeaderboardStats",)
    ADDLEADERBOARDSTATS_FIELD_NUMBER: _ClassVar[int]
    addLeaderboardStats: bool
    def __init__(self, addLeaderboardStats: bool = ...) -> None: ...

class GetPlayerFriendByUidRequest(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class GetItemsRequest(_message.Message):
    __slots__ = ("count",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ..., **kwargs) -> None: ...

class GetClanInviteRequestsRequest(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class OnLobbyChatMessageEvent(_message.Message):
    __slots__ = ("gpid", "message")
    GPID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    message: str
    def __init__(self, gpid: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class RequestToJoinClanRequest(_message.Message):
    __slots__ = ("clanId",)
    CLANID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    def __init__(self, clanId: _Optional[str] = ...) -> None: ...

class CreateLobbyWithSpectatorsResponse(_message.Message):
    __slots__ = ("lobby",)
    LOBBY_FIELD_NUMBER: _ClassVar[int]
    lobby: Lobby
    def __init__(self, lobby: _Optional[_Union[Lobby, _Mapping]] = ...) -> None: ...

class GetSystemMessageDetailsResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: SystemMessageDetails
    def __init__(self, message: _Optional[_Union[SystemMessageDetails, _Mapping]] = ...) -> None: ...

class GetSubscribedCreatorRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscribeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VkAuthRequest(_message.Message):
    __slots__ = ("authVk", "appVerification", "deviceInfo")
    AUTHVK_FIELD_NUMBER: _ClassVar[int]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    authVk: AuthVk
    appVerification: AppVerification
    deviceInfo: DeviceInfo
    def __init__(self, authVk: _Optional[_Union[AuthVk, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class AppleIdUnLinkAuthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnClanStatsUpdatedEvent(_message.Message):
    __slots__ = ("clanStats", "clanMemberStats")
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    clanStats: ClanStats
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[ClanMemberStats]
    def __init__(self, clanStats: _Optional[_Union[ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[ClanMemberStats, _Mapping]]] = ...) -> None: ...

class OnJoinRequestDeclinedEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteSystemMessagesRequest(_message.Message):
    __slots__ = ("messageIds", "deleteAll")
    MESSAGEIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEALL_FIELD_NUMBER: _ClassVar[int]
    messageIds: _containers.RepeatedScalarFieldContainer[str]
    deleteAll: bool
    def __init__(self, messageIds: _Optional[_Iterable[str]] = ..., deleteAll: bool = ...) -> None: ...

class SetLobbyMaxMembersResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPlayerJoinRequestsRequest(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class GoogleAuthResponse(_message.Message):
    __slots__ = ("ticketsCase",)
    TICKETSCASE_FIELD_NUMBER: _ClassVar[int]
    ticketsCase: GoogleAuthResponse_TicketsOneofCase
    def __init__(self, ticketsCase: _Optional[_Union[GoogleAuthResponse_TicketsOneofCase, str]] = ...) -> None: ...

class GameCenterUnLinkAuthResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnKickedMemberEvent(_message.Message):
    __slots__ = ("kickerMemberId", "kickedMemberId")
    KICKERMEMBERID_FIELD_NUMBER: _ClassVar[int]
    KICKEDMEMBERID_FIELD_NUMBER: _ClassVar[int]
    kickerMemberId: str
    kickedMemberId: str
    def __init__(self, kickerMemberId: _Optional[str] = ..., kickedMemberId: _Optional[str] = ...) -> None: ...

class SetLobbyPhotonGameResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMarketplaceSettingsResponse(_message.Message):
    __slots__ = ("marketplaceSettings",)
    MARKETPLACESETTINGS_FIELD_NUMBER: _ClassVar[int]
    marketplaceSettings: MarketplaceSettings
    def __init__(self, marketplaceSettings: _Optional[_Union[MarketplaceSettings, _Mapping]] = ...) -> None: ...

class AssignRoleToMemberRequest(_message.Message):
    __slots__ = ("memberId", "roleId")
    MEMBERID_FIELD_NUMBER: _ClassVar[int]
    ROLEID_FIELD_NUMBER: _ClassVar[int]
    memberId: str
    roleId: int
    def __init__(self, memberId: _Optional[str] = ..., roleId: _Optional[int] = ...) -> None: ...

class SetClanDescriptionRequest(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class GetPlayerStatsForSeasonResponse(_message.Message):
    __slots__ = ("stat",)
    STAT_FIELD_NUMBER: _ClassVar[int]
    stat: _containers.RepeatedCompositeFieldContainer[PlayerStat]
    def __init__(self, stat: _Optional[_Iterable[_Union[PlayerStat, _Mapping]]] = ...) -> None: ...

class StorePlayerStatsResponse(_message.Message):
    __slots__ = ("gpid", "updatedDate")
    GPID_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    updatedDate: int
    def __init__(self, gpid: _Optional[str] = ..., updatedDate: _Optional[int] = ...) -> None: ...

class GetClanSettingsResponse(_message.Message):
    __slots__ = ("clanSettings",)
    CLANSETTINGS_FIELD_NUMBER: _ClassVar[int]
    clanSettings: ClanSettings
    def __init__(self, clanSettings: _Optional[_Union[ClanSettings, _Mapping]] = ...) -> None: ...

class CancelRequestRequest(_message.Message):
    __slots__ = ("requestId",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class HuaweiUnLinkAuthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DontAskLaterRequest(_message.Message):
    __slots__ = ("internalData", "context")
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    internalData: str
    context: str
    def __init__(self, internalData: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...

class GetClanByTagResponse(_message.Message):
    __slots__ = ("clan",)
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: Clan
    def __init__(self, clan: _Optional[_Union[Clan, _Mapping]] = ...) -> None: ...

class FacebookAuthResponse(_message.Message):
    __slots__ = ("ticketsCase",)
    TICKETSCASE_FIELD_NUMBER: _ClassVar[int]
    ticketsCase: FacebookAuthResponse_TicketsOneofCase
    def __init__(self, ticketsCase: _Optional[_Union[FacebookAuthResponse_TicketsOneofCase, str]] = ...) -> None: ...

class JoinLobbyAsResponse(_message.Message):
    __slots__ = ("lobby",)
    LOBBY_FIELD_NUMBER: _ClassVar[int]
    lobby: Lobby
    def __init__(self, lobby: _Optional[_Union[Lobby, _Mapping]] = ...) -> None: ...

class GetPlayerSettingsResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: PlayerSettings
    def __init__(self, settings: _Optional[_Union[PlayerSettings, _Mapping]] = ...) -> None: ...

class RevokePlayerInvitationToLobbyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateClanRequest(_message.Message):
    __slots__ = ("tag", "name", "clanType")
    TAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLANTYPE_FIELD_NUMBER: _ClassVar[int]
    tag: str
    name: str
    clanType: ClanType
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[str] = ..., clanType: _Optional[_Union[ClanType, str]] = ...) -> None: ...

class BoltIdLinkAuthRequest(_message.Message):
    __slots__ = ("authBoltId",)
    AUTHBOLTID_FIELD_NUMBER: _ClassVar[int]
    authBoltId: AuthBoltId
    def __init__(self, authBoltId: _Optional[_Union[AuthBoltId, _Mapping]] = ...) -> None: ...

class GetChatUserResponse(_message.Message):
    __slots__ = ("chatUser",)
    CHATUSER_FIELD_NUMBER: _ClassVar[int]
    chatUser: ChatUser
    def __init__(self, chatUser: _Optional[_Union[ChatUser, _Mapping]] = ...) -> None: ...

class GetClanByIdResponse(_message.Message):
    __slots__ = ("clan",)
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: Clan
    def __init__(self, clan: _Optional[_Union[Clan, _Mapping]] = ...) -> None: ...

class GetLastRateGameRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnOnlineStatusChangedEvent(_message.Message):
    __slots__ = ("onlineStatus",)
    ONLINESTATUS_FIELD_NUMBER: _ClassVar[int]
    onlineStatus: PlayerStatus
    def __init__(self, onlineStatus: _Optional[_Union[PlayerStatus, _Mapping]] = ...) -> None: ...

class GetUnreadLogMessagesCountResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class DeleteClosedJoinRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteFriendMsgsRequest(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class ReadFilesResponse(_message.Message):
    __slots__ = ("files",)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[Storage]
    def __init__(self, files: _Optional[_Iterable[_Union[Storage, _Mapping]]] = ...) -> None: ...

class SearchLobbyResponse(_message.Message):
    __slots__ = ("lobbies",)
    LOBBIES_FIELD_NUMBER: _ClassVar[int]
    lobbies: _containers.RepeatedCompositeFieldContainer[Lobby]
    def __init__(self, lobbies: _Optional[_Iterable[_Union[Lobby, _Mapping]]] = ...) -> None: ...

class GetAllGameAnnouncementsResponse(_message.Message):
    __slots__ = ("announcements",)
    ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    announcements: _containers.RepeatedCompositeFieldContainer[GameAnnouncement]
    def __init__(self, announcements: _Optional[_Iterable[_Union[GameAnnouncement, _Mapping]]] = ...) -> None: ...

class OnInviteRequestDeclinedEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClanLogMessagesResponse(_message.Message):
    __slots__ = ("clanUserMessage",)
    CLANUSERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    clanUserMessage: _containers.RepeatedCompositeFieldContainer[ClanUserMessage]
    def __init__(self, clanUserMessage: _Optional[_Iterable[_Union[ClanUserMessage, _Mapping]]] = ...) -> None: ...

class GetClanStatsRequest(_message.Message):
    __slots__ = ("clanId", "addLeaderboardStats")
    CLANID_FIELD_NUMBER: _ClassVar[int]
    ADDLEADERBOARDSTATS_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    addLeaderboardStats: bool
    def __init__(self, clanId: _Optional[str] = ..., addLeaderboardStats: bool = ...) -> None: ...

class SetLobbyDataRequest(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: Dictionary
    def __init__(self, data: _Optional[_Union[Dictionary, _Mapping]] = ...) -> None: ...

class SubscribeCreatorResponse(_message.Message):
    __slots__ = ("creator",)
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    creator: Creator
    def __init__(self, creator: _Optional[_Union[Creator, _Mapping]] = ...) -> None: ...

class ReadClanChatMessagesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JoinLobbyAsRequest(_message.Message):
    __slots__ = ("lobbyId", "playerType", "token")
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    playerType: LobbyPlayerType
    token: str
    def __init__(self, lobbyId: _Optional[str] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ..., token: _Optional[str] = ...) -> None: ...

class OnPlayerAvatarChangedEvent(_message.Message):
    __slots__ = ("gpid", "avatarId")
    GPID_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    avatarId: str
    def __init__(self, gpid: _Optional[str] = ..., avatarId: _Optional[str] = ...) -> None: ...

class SetOnlineStatusResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRecommendedClansRequest(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetIdTokenResponse(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class InvitePlayerToLobbyAsRequest(_message.Message):
    __slots__ = ("invitedGpid", "playerType")
    INVITEDGPID_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    invitedGpid: str
    playerType: LobbyPlayerType
    def __init__(self, invitedGpid: _Optional[str] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ...) -> None: ...

class SendFriendMsgResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValidateClanTagRequest(_message.Message):
    __slots__ = ("tag",)
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class OnReceivedSpectatorInviteToLobbyEvent(_message.Message):
    __slots__ = ("invite",)
    INVITE_FIELD_NUMBER: _ClassVar[int]
    invite: LobbyInvite
    def __init__(self, invite: _Optional[_Union[LobbyInvite, _Mapping]] = ...) -> None: ...

class OnJoinedToClanEvent(_message.Message):
    __slots__ = ("clan",)
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: Clan
    def __init__(self, clan: _Optional[_Union[Clan, _Mapping]] = ...) -> None: ...

class ChangeClanTypeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetDefaultAvatarRequest(_message.Message):
    __slots__ = ("avatarId",)
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    def __init__(self, avatarId: _Optional[str] = ...) -> None: ...

class RateGameResponse(_message.Message):
    __slots__ = ("rate", "message", "internalData", "context", "timestamp", "reward")
    RATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    rate: int
    message: str
    internalData: str
    context: str
    timestamp: int
    reward: GivenReward
    def __init__(self, rate: _Optional[int] = ..., message: _Optional[str] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ..., timestamp: _Optional[int] = ..., reward: _Optional[_Union[GivenReward, _Mapping]] = ...) -> None: ...

class OnLobbyOwnerChangedEvent(_message.Message):
    __slots__ = ("lobbyOwnerGpid",)
    LOBBYOWNERGPID_FIELD_NUMBER: _ClassVar[int]
    lobbyOwnerGpid: str
    def __init__(self, lobbyOwnerGpid: _Optional[str] = ...) -> None: ...

class OnLobbyMaxSpectatorsChangedEvent(_message.Message):
    __slots__ = ("maxSpectators",)
    MAXSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    maxSpectators: int
    def __init__(self, maxSpectators: _Optional[int] = ...) -> None: ...

class SendFriendRequestResponse(_message.Message):
    __slots__ = ("relationshipStatus",)
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class OnInventoryChangedEvent(_message.Message):
    __slots__ = ("addedItems", "changedItems", "currencies")
    ADDEDITEMS_FIELD_NUMBER: _ClassVar[int]
    CHANGEDITEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    addedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    changedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    currencies: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    def __init__(self, addedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., changedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ...) -> None: ...

class SetPlayerFirebaseTokenRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class VkLinkAuthRequest(_message.Message):
    __slots__ = ("authVk",)
    AUTHVK_FIELD_NUMBER: _ClassVar[int]
    authVk: AuthVk
    def __init__(self, authVk: _Optional[_Union[AuthVk, _Mapping]] = ...) -> None: ...

class RateGameRequest(_message.Message):
    __slots__ = ("rate", "message", "internalData", "context")
    RATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    rate: int
    message: str
    internalData: str
    context: str
    def __init__(self, rate: _Optional[int] = ..., message: _Optional[str] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ...) -> None: ...

class ReadSystemMessagesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KickMemberResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetLobbyDataResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInventoryItemPropertyDefinitionsResponse(_message.Message):
    __slots__ = ("inventoryItemPropertyDefinitions", "lastUpdated")
    INVENTORYITEMPROPERTYDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    inventoryItemPropertyDefinitions: _containers.RepeatedCompositeFieldContainer[InventoryItemPropertyDefinitions]
    lastUpdated: str
    def __init__(self, inventoryItemPropertyDefinitions: _Optional[_Iterable[_Union[InventoryItemPropertyDefinitions, _Mapping]]] = ..., lastUpdated: _Optional[str] = ...) -> None: ...

class GetGameSettingsEncryptedResponse(_message.Message):
    __slots__ = ("gameSettings",)
    GAMESETTINGS_FIELD_NUMBER: _ClassVar[int]
    gameSettings: _containers.RepeatedCompositeFieldContainer[GameSetting]
    def __init__(self, gameSettings: _Optional[_Iterable[_Union[GameSetting, _Mapping]]] = ...) -> None: ...

class SendFriendRequestRequest(_message.Message):
    __slots__ = ("friendGpid", "msg")
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    msg: str
    def __init__(self, friendGpid: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class HuaweiLinkAuthRequest(_message.Message):
    __slots__ = ("authHuawei",)
    AUTHHUAWEI_FIELD_NUMBER: _ClassVar[int]
    authHuawei: AuthHuawei
    def __init__(self, authHuawei: _Optional[_Union[AuthHuawei, _Mapping]] = ...) -> None: ...

class ReadClanLogMessagesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnMemberJoinedToClanEvent(_message.Message):
    __slots__ = ("clanMember", "joinClanType", "joinRequestAcceptor")
    CLANMEMBER_FIELD_NUMBER: _ClassVar[int]
    JOINCLANTYPE_FIELD_NUMBER: _ClassVar[int]
    JOINREQUESTACCEPTOR_FIELD_NUMBER: _ClassVar[int]
    clanMember: ClanMember
    joinClanType: JoinClanType
    joinRequestAcceptor: str
    def __init__(self, clanMember: _Optional[_Union[ClanMember, _Mapping]] = ..., joinClanType: _Optional[_Union[JoinClanType, str]] = ..., joinRequestAcceptor: _Optional[str] = ...) -> None: ...

class GetPlayerResponse(_message.Message):
    __slots__ = ("player", "permissions", "uuid", "intercomHMAC", "email")
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    INTERCOMHMAC_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    player: Player
    permissions: _containers.RepeatedScalarFieldContainer[int]
    uuid: str
    intercomHMAC: str
    email: str
    def __init__(self, player: _Optional[_Union[Player, _Mapping]] = ..., permissions: _Optional[_Iterable[int]] = ..., uuid: _Optional[str] = ..., intercomHMAC: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class CreateRequestEncryptedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClanStatsForSeasonRequest(_message.Message):
    __slots__ = ("seasonId", "clanId")
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    seasonId: str
    clanId: str
    def __init__(self, seasonId: _Optional[str] = ..., clanId: _Optional[str] = ...) -> None: ...

class BEBFABBECGCAFCH(_message.Message):
    __slots__ = ("AHEABGBEHEGHDED", "EGFBCGECDCHABCB")
    AHEABGBEHEGHDED_FIELD_NUMBER: _ClassVar[int]
    EGFBCGECDCHABCB_FIELD_NUMBER: _ClassVar[int]
    AHEABGBEHEGHDED: AAGDEBAFFCFGFCH
    EGFBCGECDCHABCB: _containers.RepeatedCompositeFieldContainer[DBAFACADFEBGFED]
    def __init__(self, AHEABGBEHEGHDED: _Optional[_Union[AAGDEBAFFCFGFCH, _Mapping]] = ..., EGFBCGECDCHABCB: _Optional[_Iterable[_Union[DBAFACADFEBGFED, _Mapping]]] = ...) -> None: ...

class GetCurrentStatsRequest(_message.Message):
    __slots__ = ("addLeaderboardStats",)
    ADDLEADERBOARDSTATS_FIELD_NUMBER: _ClassVar[int]
    addLeaderboardStats: bool
    def __init__(self, addLeaderboardStats: bool = ...) -> None: ...

class OnLobbyPhotonGameChangedEvent(_message.Message):
    __slots__ = ("photonGame",)
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    photonGame: PhotonGame
    def __init__(self, photonGame: _Optional[_Union[PhotonGame, _Mapping]] = ...) -> None: ...

class AppStoreBuyInappRequest(_message.Message):
    __slots__ = ("base64", "price", "productInfos")
    BASE64_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTINFOS_FIELD_NUMBER: _ClassVar[int]
    base64: str
    price: Money
    productInfos: _containers.RepeatedCompositeFieldContainer[ProductInfo]
    def __init__(self, base64: _Optional[str] = ..., price: _Optional[_Union[Money, _Mapping]] = ..., productInfos: _Optional[_Iterable[_Union[ProductInfo, _Mapping]]] = ...) -> None: ...

class ReleasedDlcRequest(_message.Message):
    __slots__ = ("version", "gameUid", "platform")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GAMEUID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    version: str
    gameUid: str
    platform: Platform
    def __init__(self, version: _Optional[str] = ..., gameUid: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ...) -> None: ...

class GetChatUsersLiteRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreatePurchaseRequestRequest(_message.Message):
    __slots__ = ("itemDefinitionId", "price", "quantity")
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    price: float
    quantity: int
    def __init__(self, itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ...) -> None: ...

class GetClanStatsForSeasonResponse(_message.Message):
    __slots__ = ("clanStats", "clanMemberStats")
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    clanStats: ClanStats
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[ClanMemberStats]
    def __init__(self, clanStats: _Optional[_Union[ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[ClanMemberStats, _Mapping]]] = ...) -> None: ...

class GetClanClosedInviteRequestsCountResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetPlayerProcessingRequestRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnMatchFinishedEvent(_message.Message):
    __slots__ = ("match",)
    MATCH_FIELD_NUMBER: _ClassVar[int]
    match: FinishedMatch
    def __init__(self, match: _Optional[_Union[FinishedMatch, _Mapping]] = ...) -> None: ...

class GetGameSettingsEncryptedRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadClanChatMessagesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnPlayerRequestClosedEvent(_message.Message):
    __slots__ = ("request", "item")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    request: ClosedRequest
    item: PlayerInventoryItem
    def __init__(self, request: _Optional[_Union[ClosedRequest, _Mapping]] = ..., item: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class OnLeftFromClan(_message.Message):
    __slots__ = ("memberId",)
    MEMBERID_FIELD_NUMBER: _ClassVar[int]
    memberId: str
    def __init__(self, memberId: _Optional[str] = ...) -> None: ...

class AGCBFBCDCGGECGA(_message.Message):
    __slots__ = ("EFBFADAAEGEDGDE", "AHEABGBEHEGHDED")
    EFBFADAAEGEDGDE_FIELD_NUMBER: _ClassVar[int]
    AHEABGBEHEGHDED_FIELD_NUMBER: _ClassVar[int]
    EFBFADAAEGEDGDE: str
    AHEABGBEHEGHDED: AAGDEBAFFCFGFCH
    def __init__(self, EFBFADAAEGEDGDE: _Optional[str] = ..., AHEABGBEHEGHDED: _Optional[_Union[AAGDEBAFFCFGFCH, _Mapping]] = ...) -> None: ...

class GetPlayerInventoryResponse(_message.Message):
    __slots__ = ("playerInventory",)
    PLAYERINVENTORY_FIELD_NUMBER: _ClassVar[int]
    playerInventory: PlayerInventory
    def __init__(self, playerInventory: _Optional[_Union[PlayerInventory, _Mapping]] = ...) -> None: ...

class GetOtherPlayerItemsResponse(_message.Message):
    __slots__ = ("playerInventoryItems",)
    PLAYERINVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, playerInventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class GoogleBuyInappResponse(_message.Message):
    __slots__ = ("reward",)
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: PlayerInventory
    def __init__(self, reward: _Optional[_Union[PlayerInventory, _Mapping]] = ...) -> None: ...

class KickPlayerFromLobbyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChangeLobbyOtherPlayerTypeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BuyInventoryItemRequest(_message.Message):
    __slots__ = ("inventoryItemId", "quantity", "currencyId", "toManyItems")
    INVENTORYITEMID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CURRENCYID_FIELD_NUMBER: _ClassVar[int]
    TOMANYITEMS_FIELD_NUMBER: _ClassVar[int]
    inventoryItemId: int
    quantity: int
    currencyId: int
    toManyItems: bool
    def __init__(self, inventoryItemId: _Optional[int] = ..., quantity: _Optional[int] = ..., currencyId: _Optional[int] = ..., toManyItems: bool = ...) -> None: ...

class MountInventoryItemRequest(_message.Message):
    __slots__ = ("consumedItemId", "modifiedItemId", "modificationName")
    CONSUMEDITEMID_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDITEMID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONNAME_FIELD_NUMBER: _ClassVar[int]
    consumedItemId: int
    modifiedItemId: int
    modificationName: str
    def __init__(self, consumedItemId: _Optional[int] = ..., modifiedItemId: _Optional[int] = ..., modificationName: _Optional[str] = ...) -> None: ...

class OnPlayerLeftLobbyEvent(_message.Message):
    __slots__ = ("leftGpid",)
    LEFTGPID_FIELD_NUMBER: _ClassVar[int]
    leftGpid: str
    def __init__(self, leftGpid: _Optional[str] = ...) -> None: ...

class DeclineJoinRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveFriendResponse(_message.Message):
    __slots__ = ("relationshipStatus",)
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class GoogleAuthRequest(_message.Message):
    __slots__ = ("authGoogle", "appVerification", "deviceInfo")
    AUTHGOOGLE_FIELD_NUMBER: _ClassVar[int]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    authGoogle: AuthGoogle
    appVerification: AppVerification
    deviceInfo: DeviceInfo
    def __init__(self, authGoogle: _Optional[_Union[AuthGoogle, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class OnPlayerKickedFromLobbyEvent(_message.Message):
    __slots__ = ("kickInitiatorGpid", "kickedGpid")
    KICKINITIATORGPID_FIELD_NUMBER: _ClassVar[int]
    KICKEDGPID_FIELD_NUMBER: _ClassVar[int]
    kickInitiatorGpid: str
    kickedGpid: str
    def __init__(self, kickInitiatorGpid: _Optional[str] = ..., kickedGpid: _Optional[str] = ...) -> None: ...

class FacebookUnLinkAuthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadFilesRequest(_message.Message):
    __slots__ = ("filenames",)
    FILENAMES_FIELD_NUMBER: _ClassVar[int]
    filenames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, filenames: _Optional[_Iterable[str]] = ...) -> None: ...

class GACHFBFBBEHDAAD(_message.Message):
    __slots__ = ("GFCCADHDDFAFHFE",)
    GFCCADHDDFAFHFE_FIELD_NUMBER: _ClassVar[int]
    GFCCADHDDFAFHFE: str
    def __init__(self, GFCCADHDDFAFHFE: _Optional[str] = ...) -> None: ...

class LeaveClanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AskLaterResponse(_message.Message):
    __slots__ = ("timestampAskLater", "internalData", "context", "timestamp")
    TIMESTAMPASKLATER_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestampAskLater: int
    internalData: str
    context: str
    timestamp: int
    def __init__(self, timestampAskLater: _Optional[int] = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class SetLobbyJoinableRequest(_message.Message):
    __slots__ = ("joinable",)
    JOINABLE_FIELD_NUMBER: _ClassVar[int]
    joinable: bool
    def __init__(self, joinable: bool = ...) -> None: ...

class AssignRoleToMemberResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LeaveLobbyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetAwayStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadSystemMessagesRequest(_message.Message):
    __slots__ = ("messageIds", "readAll")
    MESSAGEIDS_FIELD_NUMBER: _ClassVar[int]
    READALL_FIELD_NUMBER: _ClassVar[int]
    messageIds: _containers.RepeatedScalarFieldContainer[str]
    readAll: bool
    def __init__(self, messageIds: _Optional[_Iterable[str]] = ..., readAll: bool = ...) -> None: ...

class SetClanDescriptionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnCouponActivatedEvent(_message.Message):
    __slots__ = ("reward",)
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: GivenReward
    def __init__(self, reward: _Optional[_Union[GivenReward, _Mapping]] = ...) -> None: ...

class CHGACEEHFADEDHH(_message.Message):
    __slots__ = ("DCAGCDFCHBBDCDB", "GABAFEDDDBEGGAE", "CGCGBGBEGCADABH")
    DCAGCDFCHBBDCDB_FIELD_NUMBER: _ClassVar[int]
    GABAFEDDDBEGGAE_FIELD_NUMBER: _ClassVar[int]
    CGCGBGBEGCADABH_FIELD_NUMBER: _ClassVar[int]
    DCAGCDFCHBBDCDB: bytes
    GABAFEDDDBEGGAE: bytes
    CGCGBGBEGCADABH: bytes
    def __init__(self, DCAGCDFCHBBDCDB: _Optional[bytes] = ..., GABAFEDDDBEGGAE: _Optional[bytes] = ..., CGCGBGBEGCADABH: _Optional[bytes] = ...) -> None: ...

class GetClanInviteRequestsResponse(_message.Message):
    __slots__ = ("clanInviteRequests",)
    CLANINVITEREQUESTS_FIELD_NUMBER: _ClassVar[int]
    clanInviteRequests: _containers.RepeatedCompositeFieldContainer[ClanInviteRequest]
    def __init__(self, clanInviteRequests: _Optional[_Iterable[_Union[ClanInviteRequest, _Mapping]]] = ...) -> None: ...

class GetPlayerFriendByIdRequest(_message.Message):
    __slots__ = ("gpid",)
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class OnClanMemberDeclinedRequestEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnNewPlayerJoinedLobbyEvent(_message.Message):
    __slots__ = ("newPlayer",)
    NEWPLAYER_FIELD_NUMBER: _ClassVar[int]
    newPlayer: PlayerFriend
    def __init__(self, newPlayer: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class GetLinkedAuthResponse(_message.Message):
    __slots__ = ("authTypes",)
    AUTHTYPES_FIELD_NUMBER: _ClassVar[int]
    authTypes: _containers.RepeatedCompositeFieldContainer[LinkedAuth]
    def __init__(self, authTypes: _Optional[_Iterable[_Union[LinkedAuth, _Mapping]]] = ...) -> None: ...

class SetLobbyOwnerRequest(_message.Message):
    __slots__ = ("gpid",)
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class RevokeFriendRequestRequest(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class ADHHEGBDFBEBGGC(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KickMemberRequest(_message.Message):
    __slots__ = ("memberId", "kickingReason")
    MEMBERID_FIELD_NUMBER: _ClassVar[int]
    KICKINGREASON_FIELD_NUMBER: _ClassVar[int]
    memberId: str
    kickingReason: str
    def __init__(self, memberId: _Optional[str] = ..., kickingReason: _Optional[str] = ...) -> None: ...

class RecoverAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPlayerGameEventsProgressesResponse(_message.Message):
    __slots__ = ("gameEventsProgresses",)
    GAMEEVENTSPROGRESSES_FIELD_NUMBER: _ClassVar[int]
    gameEventsProgresses: _containers.RepeatedCompositeFieldContainer[GameEventProgress]
    def __init__(self, gameEventsProgresses: _Optional[_Iterable[_Union[GameEventProgress, _Mapping]]] = ...) -> None: ...

class BBFGDBCEGCBFBEE(_message.Message):
    __slots__ = ("FBHHACGFCHFEEED", "FCBHCCCADBCHHGB")
    FBHHACGFCHFEEED_FIELD_NUMBER: _ClassVar[int]
    FCBHCCCADBCHHGB_FIELD_NUMBER: _ClassVar[int]
    FBHHACGFCHFEEED: bytes
    FCBHCCCADBCHHGB: str
    def __init__(self, FBHHACGFCHFEEED: _Optional[bytes] = ..., FCBHCCCADBCHHGB: _Optional[str] = ...) -> None: ...

class SetPlayerNameResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefuseInvitationToLobbyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnTradeRequestOpenedEvent(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: OpenRequest
    def __init__(self, request: _Optional[_Union[OpenRequest, _Mapping]] = ...) -> None: ...

class BlockFriendResponse(_message.Message):
    __slots__ = ("relationshipStatus",)
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class GetCurrentClanStatsResponse(_message.Message):
    __slots__ = ("clanId", "stats", "clanStats", "clanMemberStats")
    CLANID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    stats: ClanStatsMap
    clanStats: ClanStats
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[ClanMemberStats]
    def __init__(self, clanId: _Optional[str] = ..., stats: _Optional[_Union[ClanStatsMap, _Mapping]] = ..., clanStats: _Optional[_Union[ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[ClanMemberStats, _Mapping]]] = ...) -> None: ...

class GoogleBuyInappRequest(_message.Message):
    __slots__ = ("json", "signature")
    JSON_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    json: str
    signature: str
    def __init__(self, json: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class ReadFriendMsgsRequest(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class InviteToClanRequest(_message.Message):
    __slots__ = ("gpid",)
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class GetLinkedAuthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnLobbyNameChangedEvent(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class OnTradeUpdatedEvent(_message.Message):
    __slots__ = ("trade",)
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ("topic",)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str
    def __init__(self, topic: _Optional[str] = ...) -> None: ...

class GetPlayerFriendsIdsRequest(_message.Message):
    __slots__ = ("relationshipStatuses",)
    RELATIONSHIPSTATUSES_FIELD_NUMBER: _ClassVar[int]
    relationshipStatuses: _containers.RepeatedScalarFieldContainer[RelationshipStatus]
    def __init__(self, relationshipStatuses: _Optional[_Iterable[_Union[RelationshipStatus, str]]] = ...) -> None: ...

class ActivateCouponResponse(_message.Message):
    __slots__ = ("currencies", "inventoryItems")
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    inventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, currencies: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., inventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class BoltIdLinkAuthResponse(_message.Message):
    __slots__ = ("guestLinking",)
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class GetTradeOpenSaleRequestsRequest(_message.Message):
    __slots__ = ("id", "page", "size", "tradeFilters")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TRADEFILTERS_FIELD_NUMBER: _ClassVar[int]
    id: int
    page: int
    size: int
    tradeFilters: TradeFilters
    def __init__(self, id: _Optional[int] = ..., page: _Optional[int] = ..., size: _Optional[int] = ..., tradeFilters: _Optional[_Union[TradeFilters, _Mapping]] = ...) -> None: ...

class GetUnreadChatMessagesCountResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class DeclineInviteRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnsubscribeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClanClosedInviteRequestsCountRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DontAskLaterResponse(_message.Message):
    __slots__ = ("dontAskLater", "internalData", "context", "timestamp")
    DONTASKLATER_FIELD_NUMBER: _ClassVar[int]
    INTERNALDATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    dontAskLater: bool
    internalData: str
    context: str
    timestamp: int
    def __init__(self, dontAskLater: bool = ..., internalData: _Optional[str] = ..., context: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class GetClanMembersResponse(_message.Message):
    __slots__ = ("clanMembers",)
    CLANMEMBERS_FIELD_NUMBER: _ClassVar[int]
    clanMembers: _containers.RepeatedCompositeFieldContainer[ClanMember]
    def __init__(self, clanMembers: _Optional[_Iterable[_Union[ClanMember, _Mapping]]] = ...) -> None: ...

class VkUnLinkAuthResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HuaweiAuthResponse(_message.Message):
    __slots__ = ("ticketsCase",)
    TICKETSCASE_FIELD_NUMBER: _ClassVar[int]
    ticketsCase: HuaweiAuthResponse_TicketsOneofCase
    def __init__(self, ticketsCase: _Optional[_Union[HuaweiAuthResponse_TicketsOneofCase, str]] = ...) -> None: ...

class OnReadClosedInviteRequestEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BuyInventoryItemResponse(_message.Message):
    __slots__ = ("playerInventoryItems",)
    PLAYERINVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, playerInventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class OnLobbyJoinableChangedEvent(_message.Message):
    __slots__ = ("joinable",)
    JOINABLE_FIELD_NUMBER: _ClassVar[int]
    joinable: bool
    def __init__(self, joinable: bool = ...) -> None: ...

class ActivateCouponRequest(_message.Message):
    __slots__ = ("couponId",)
    COUPONID_FIELD_NUMBER: _ClassVar[int]
    couponId: str
    def __init__(self, couponId: _Optional[str] = ...) -> None: ...

class GetIdTokenRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetLobbyOwnerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeclineJoinRequestRequest(_message.Message):
    __slots__ = ("requestId",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class FindClanResponse(_message.Message):
    __slots__ = ("clan",)
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: _containers.RepeatedCompositeFieldContainer[Clan]
    def __init__(self, clan: _Optional[_Iterable[_Union[Clan, _Mapping]]] = ...) -> None: ...

class GetAchievementDefinitionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateLobbyWithSpectatorsRequest(_message.Message):
    __slots__ = ("name", "lobbyType", "maxMembers", "maxSpectators", "dataVisibleInSearch")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOBBYTYPE_FIELD_NUMBER: _ClassVar[int]
    MAXMEMBERS_FIELD_NUMBER: _ClassVar[int]
    MAXSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    DATAVISIBLEINSEARCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    lobbyType: LobbyType
    maxMembers: int
    maxSpectators: int
    dataVisibleInSearch: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., lobbyType: _Optional[_Union[LobbyType, str]] = ..., maxMembers: _Optional[int] = ..., maxSpectators: _Optional[int] = ..., dataVisibleInSearch: _Optional[_Iterable[str]] = ...) -> None: ...

class HuaweiAuthRequest(_message.Message):
    __slots__ = ("authHuawei", "appVerification", "deviceInfo")
    AUTHHUAWEI_FIELD_NUMBER: _ClassVar[int]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    authHuawei: AuthHuawei
    appVerification: AppVerification
    deviceInfo: DeviceInfo
    def __init__(self, authHuawei: _Optional[_Union[AuthHuawei, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class OnInvitedToClanEvent(_message.Message):
    __slots__ = ("requestId", "clan", "player")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    clan: Clan
    player: Player
    def __init__(self, requestId: _Optional[str] = ..., clan: _Optional[_Union[Clan, _Mapping]] = ..., player: _Optional[_Union[Player, _Mapping]] = ...) -> None: ...

class OnNewSpectatorJoinedLobbyEvent(_message.Message):
    __slots__ = ("newSpectator",)
    NEWSPECTATOR_FIELD_NUMBER: _ClassVar[int]
    newSpectator: PlayerFriend
    def __init__(self, newSpectator: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class GetDefaultAvatarsRequest(_message.Message):
    __slots__ = ("lastUpdated",)
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    lastUpdated: str
    def __init__(self, lastUpdated: _Optional[str] = ...) -> None: ...

class OnFriendNameChangedEvent(_message.Message):
    __slots__ = ("friendGpid", "newName")
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    NEWNAME_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    newName: str
    def __init__(self, friendGpid: _Optional[str] = ..., newName: _Optional[str] = ...) -> None: ...

class OnRevokeFriendshipRequestEvent(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class OnNewSpectatorInvitedToLobbyEvent(_message.Message):
    __slots__ = ("inviteSenderGpid", "newSpectator")
    INVITESENDERGPID_FIELD_NUMBER: _ClassVar[int]
    NEWSPECTATOR_FIELD_NUMBER: _ClassVar[int]
    inviteSenderGpid: str
    newSpectator: PlayerFriend
    def __init__(self, inviteSenderGpid: _Optional[str] = ..., newSpectator: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class CFCGDGEAEHDEABF(_message.Message):
    __slots__ = ("EGHCDGCBDAGFAEC", "GAFABGFBEDACDEB", "GDBDGGFADACEHGC")
    EGHCDGCBDAGFAEC_FIELD_NUMBER: _ClassVar[int]
    GAFABGFBEDACDEB_FIELD_NUMBER: _ClassVar[int]
    GDBDGGFADACEHGC_FIELD_NUMBER: _ClassVar[int]
    EGHCDGCBDAGFAEC: BHBHHDGDFCHFACH
    GAFABGFBEDACDEB: str
    GDBDGGFADACEHGC: HGBAGDBBFADCDGA
    def __init__(self, EGHCDGCBDAGFAEC: _Optional[_Union[BHBHHDGDFCHFACH, str]] = ..., GAFABGFBEDACDEB: _Optional[str] = ..., GDBDGGFADACEHGC: _Optional[_Union[HGBAGDBBFADCDGA, _Mapping]] = ...) -> None: ...

class FacebookUnLinkAuthResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokePlayerInvitationToLobbyRequest(_message.Message):
    __slots__ = ("revokedGpid",)
    REVOKEDGPID_FIELD_NUMBER: _ClassVar[int]
    revokedGpid: str
    def __init__(self, revokedGpid: _Optional[str] = ...) -> None: ...

class TestAuthResponse(_message.Message):
    __slots__ = ("ticketsCase",)
    TICKETSCASE_FIELD_NUMBER: _ClassVar[int]
    ticketsCase: TestAuthResponse_TicketsOneofCase
    def __init__(self, ticketsCase: _Optional[_Union[TestAuthResponse_TicketsOneofCase, str]] = ...) -> None: ...

class ProgressChallengeRequest(_message.Message):
    __slots__ = ("gameEventChallengeId", "points")
    GAMEEVENTCHALLENGEID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    gameEventChallengeId: str
    points: int
    def __init__(self, gameEventChallengeId: _Optional[str] = ..., points: _Optional[int] = ...) -> None: ...

class GameCenterAuthResponse(_message.Message):
    __slots__ = ("ticketsCase",)
    TICKETSCASE_FIELD_NUMBER: _ClassVar[int]
    ticketsCase: GameCenterAuthResponse_TicketsOneofCase
    def __init__(self, ticketsCase: _Optional[_Union[GameCenterAuthResponse_TicketsOneofCase, str]] = ...) -> None: ...

class AppleIdLinkAuthRequest(_message.Message):
    __slots__ = ("authAppleId",)
    AUTHAPPLEID_FIELD_NUMBER: _ClassVar[int]
    authAppleId: AuthAppleId
    def __init__(self, authAppleId: _Optional[_Union[AuthAppleId, _Mapping]] = ...) -> None: ...

class GameCenterAuthRequest(_message.Message):
    __slots__ = ("authGameCenter", "appVerification", "deviceInfo")
    AUTHGAMECENTER_FIELD_NUMBER: _ClassVar[int]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    authGameCenter: AuthGameCenter
    appVerification: AppVerification
    deviceInfo: DeviceInfo
    def __init__(self, authGameCenter: _Optional[_Union[AuthGameCenter, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class VkAuthResponse(_message.Message):
    __slots__ = ("ticketsCase",)
    TICKETSCASE_FIELD_NUMBER: _ClassVar[int]
    ticketsCase: VkAuthResponse_TicketsOneofCase
    def __init__(self, ticketsCase: _Optional[_Union[VkAuthResponse_TicketsOneofCase, str]] = ...) -> None: ...

class FacebookLinkAuthRequest(_message.Message):
    __slots__ = ("authFacebook",)
    AUTHFACEBOOK_FIELD_NUMBER: _ClassVar[int]
    authFacebook: AuthFacebook
    def __init__(self, authFacebook: _Optional[_Union[AuthFacebook, _Mapping]] = ...) -> None: ...

class OnPlayerAttributesChanged(_message.Message):
    __slots__ = ("gpid", "attributes")
    GPID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    attributes: Attributes
    def __init__(self, gpid: _Optional[str] = ..., attributes: _Optional[_Union[Attributes, _Mapping]] = ...) -> None: ...

class GetPlayerClosedRequestsResponse(_message.Message):
    __slots__ = ("closedRequests",)
    CLOSEDREQUESTS_FIELD_NUMBER: _ClassVar[int]
    closedRequests: _containers.RepeatedCompositeFieldContainer[ClosedRequest]
    def __init__(self, closedRequests: _Optional[_Iterable[_Union[ClosedRequest, _Mapping]]] = ...) -> None: ...

class ExecuteRecipeRequest(_message.Message):
    __slots__ = ("recipeCode", "inventoryItemIds")
    RECIPECODE_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEMIDS_FIELD_NUMBER: _ClassVar[int]
    recipeCode: str
    inventoryItemIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, recipeCode: _Optional[str] = ..., inventoryItemIds: _Optional[_Iterable[int]] = ...) -> None: ...

class GetClanResponse(_message.Message):
    __slots__ = ("clan",)
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: Clan
    def __init__(self, clan: _Optional[_Union[Clan, _Mapping]] = ...) -> None: ...

class OnInAppEvent(_message.Message):
    __slots__ = ("reward", "store")
    REWARD_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    reward: GivenReward
    store: Store
    def __init__(self, reward: _Optional[_Union[GivenReward, _Mapping]] = ..., store: _Optional[_Union[Store, str]] = ...) -> None: ...

class GetPlayerFriendsResponse(_message.Message):
    __slots__ = ("playerFriends",)
    PLAYERFRIENDS_FIELD_NUMBER: _ClassVar[int]
    playerFriends: _containers.RepeatedCompositeFieldContainer[PlayerFriend]
    def __init__(self, playerFriends: _Optional[_Iterable[_Union[PlayerFriend, _Mapping]]] = ...) -> None: ...

class GetClanStatsResponse(_message.Message):
    __slots__ = ("clanId", "stats", "clanStats", "clanMemberStats")
    CLANID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    stats: ClanStatsMap
    clanStats: ClanStats
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[ClanMemberStats]
    def __init__(self, clanId: _Optional[str] = ..., stats: _Optional[_Union[ClanStatsMap, _Mapping]] = ..., clanStats: _Optional[_Union[ClanStats, _Mapping]] = ..., clanMemberStats: _Optional[_Iterable[_Union[ClanMemberStats, _Mapping]]] = ...) -> None: ...

class AppleIdAuthResponse(_message.Message):
    __slots__ = ("ticketsCase",)
    TICKETSCASE_FIELD_NUMBER: _ClassVar[int]
    ticketsCase: AppleIdAuthResponse_TicketsOneofCase
    def __init__(self, ticketsCase: _Optional[_Union[AppleIdAuthResponse_TicketsOneofCase, str]] = ...) -> None: ...

class AssignLeaderRoleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveFriendRequest(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class GetClanChatMessagesRequest(_message.Message):
    __slots__ = ("count",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ..., **kwargs) -> None: ...

class BoltIdAuthRequest(_message.Message):
    __slots__ = ("authBoltId", "appVerification", "deviceInfo")
    AUTHBOLTID_FIELD_NUMBER: _ClassVar[int]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    authBoltId: AuthBoltId
    appVerification: AppVerification
    deviceInfo: DeviceInfo
    def __init__(self, authBoltId: _Optional[_Union[AuthBoltId, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class OnGamePassChangedEvent(_message.Message):
    __slots__ = ("eventId", "points", "levels", "reward", "levelsToClaimReward")
    class LevelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LevelsToClaimRewardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ListOfLevelsToClaimReward
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ListOfLevelsToClaimReward, _Mapping]] = ...) -> None: ...
    EVENTID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    eventId: str
    points: int
    levels: _containers.ScalarMap[str, int]
    reward: GivenReward
    levelsToClaimReward: _containers.MessageMap[str, ListOfLevelsToClaimReward]
    def __init__(self, eventId: _Optional[str] = ..., points: _Optional[int] = ..., levels: _Optional[_Mapping[str, int]] = ..., reward: _Optional[_Union[GivenReward, _Mapping]] = ..., levelsToClaimReward: _Optional[_Mapping[str, ListOfLevelsToClaimReward]] = ...) -> None: ...

class GameCenterLinkAuthRequest(_message.Message):
    __slots__ = ("authGameCenter",)
    AUTHGAMECENTER_FIELD_NUMBER: _ClassVar[int]
    authGameCenter: AuthGameCenter
    def __init__(self, authGameCenter: _Optional[_Union[AuthGameCenter, _Mapping]] = ...) -> None: ...

class DlcResponse(_message.Message):
    __slots__ = ("dlcs", "cdnUrls")
    DLCS_FIELD_NUMBER: _ClassVar[int]
    CDNURLS_FIELD_NUMBER: _ClassVar[int]
    dlcs: _containers.RepeatedCompositeFieldContainer[Dlc]
    cdnUrls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dlcs: _Optional[_Iterable[_Union[Dlc, _Mapping]]] = ..., cdnUrls: _Optional[_Iterable[str]] = ...) -> None: ...

class SetItemsModificationsRequest(_message.Message):
    __slots__ = ("itemsModifications",)
    ITEMSMODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    itemsModifications: _containers.RepeatedCompositeFieldContainer[ItemModifications]
    def __init__(self, itemsModifications: _Optional[_Iterable[_Union[ItemModifications, _Mapping]]] = ...) -> None: ...

class OnFriendRemovedEvent(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class BlockFriendRequest(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class LeaveLobbyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMarketplaceSettingsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnClanMaxMembersCountIncreased(_message.Message):
    __slots__ = ("newMembersCountValue",)
    NEWMEMBERSCOUNTVALUE_FIELD_NUMBER: _ClassVar[int]
    newMembersCountValue: int
    def __init__(self, newMembersCountValue: _Optional[int] = ...) -> None: ...

class OnClanDescriptionChangedEvent(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class GetAllGameAnnouncementsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPlayerProcessingRequestResponse(_message.Message):
    __slots__ = ("processingRequests",)
    PROCESSINGREQUESTS_FIELD_NUMBER: _ClassVar[int]
    processingRequests: _containers.RepeatedCompositeFieldContainer[ProcessingRequest]
    def __init__(self, processingRequests: _Optional[_Iterable[_Union[ProcessingRequest, _Mapping]]] = ...) -> None: ...

class GetSystemMessagesRequest(_message.Message):
    __slots__ = ("continuationToken", "unreadOnly")
    CONTINUATIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREADONLY_FIELD_NUMBER: _ClassVar[int]
    continuationToken: ContinuationToken
    unreadOnly: bool
    def __init__(self, continuationToken: _Optional[_Union[ContinuationToken, _Mapping]] = ..., unreadOnly: bool = ...) -> None: ...

class GetPlayerFriendByUidResponse(_message.Message):
    __slots__ = ("playerFriend",)
    PLAYERFRIEND_FIELD_NUMBER: _ClassVar[int]
    playerFriend: PlayerFriend
    def __init__(self, playerFriend: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class InviteToClanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInventoryItemDefinitionsRequest(_message.Message):
    __slots__ = ("lastUpdated",)
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    lastUpdated: str
    def __init__(self, lastUpdated: _Optional[str] = ...) -> None: ...

class AppleIdUnLinkAuthResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetAwayStatusResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSystemMessageDetailsRequest(_message.Message):
    __slots__ = ("messageId",)
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    messageId: str
    def __init__(self, messageId: _Optional[str] = ...) -> None: ...

class IgnoreFriendRequestResponse(_message.Message):
    __slots__ = ("relationshipStatus",)
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class GetPlayerInviteRequestsCountRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPlayerClosedRequestsRequest(_message.Message):
    __slots__ = ("type", "reason", "page", "size")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    type: MarketRequestType
    reason: ClosingReason
    page: int
    size: int
    def __init__(self, type: _Optional[_Union[MarketRequestType, str]] = ..., reason: _Optional[_Union[ClosingReason, str]] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetSubscribedCreatorResponse(_message.Message):
    __slots__ = ("creator",)
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    creator: Creator
    def __init__(self, creator: _Optional[_Union[Creator, _Mapping]] = ...) -> None: ...

class OnLobbyGameServerChangedEvent(_message.Message):
    __slots__ = ("gameServer",)
    GAMESERVER_FIELD_NUMBER: _ClassVar[int]
    gameServer: GameServer
    def __init__(self, gameServer: _Optional[_Union[GameServer, _Mapping]] = ...) -> None: ...

class UnblockFriendRequest(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class GetPlayerJoinRequestsResponse(_message.Message):
    __slots__ = ("clanJoinRequests",)
    CLANJOINREQUESTS_FIELD_NUMBER: _ClassVar[int]
    clanJoinRequests: _containers.RepeatedCompositeFieldContainer[ClanJoinRequest]
    def __init__(self, clanJoinRequests: _Optional[_Iterable[_Union[ClanJoinRequest, _Mapping]]] = ...) -> None: ...

class GetRolesResponse(_message.Message):
    __slots__ = ("clanMemberRole",)
    CLANMEMBERROLE_FIELD_NUMBER: _ClassVar[int]
    clanMemberRole: _containers.RepeatedCompositeFieldContainer[ClanMemberRole]
    def __init__(self, clanMemberRole: _Optional[_Iterable[_Union[ClanMemberRole, _Mapping]]] = ...) -> None: ...

class ValidateClanTagResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValidateClanNameRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class OnProgressChallengeEvent(_message.Message):
    __slots__ = ("gameEventChallengeId", "challengeCompleted", "challengePoints", "challengeReward", "gameEventId", "eventPoints", "eventLevels", "eventReward", "levelsToClaimReward", "challengeRewardsObtained")
    class EventLevelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LevelsToClaimRewardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ListOfLevelsToClaimReward
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ListOfLevelsToClaimReward, _Mapping]] = ...) -> None: ...
    GAMEEVENTCHALLENGEID_FIELD_NUMBER: _ClassVar[int]
    CHALLENGECOMPLETED_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEPOINTS_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEREWARD_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    EVENTPOINTS_FIELD_NUMBER: _ClassVar[int]
    EVENTLEVELS_FIELD_NUMBER: _ClassVar[int]
    EVENTREWARD_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEREWARDSOBTAINED_FIELD_NUMBER: _ClassVar[int]
    gameEventChallengeId: str
    challengeCompleted: bool
    challengePoints: int
    challengeReward: GivenReward
    gameEventId: str
    eventPoints: int
    eventLevels: _containers.ScalarMap[str, int]
    eventReward: GivenReward
    levelsToClaimReward: _containers.MessageMap[str, ListOfLevelsToClaimReward]
    challengeRewardsObtained: bool
    def __init__(self, gameEventChallengeId: _Optional[str] = ..., challengeCompleted: bool = ..., challengePoints: _Optional[int] = ..., challengeReward: _Optional[_Union[GivenReward, _Mapping]] = ..., gameEventId: _Optional[str] = ..., eventPoints: _Optional[int] = ..., eventLevels: _Optional[_Mapping[str, int]] = ..., eventReward: _Optional[_Union[GivenReward, _Mapping]] = ..., levelsToClaimReward: _Optional[_Mapping[str, ListOfLevelsToClaimReward]] = ..., challengeRewardsObtained: bool = ...) -> None: ...

class FindCreatorRequest(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class GetClanByTagRequest(_message.Message):
    __slots__ = ("tag",)
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class OnFriendAvatarChangedEvent(_message.Message):
    __slots__ = ("friendGpid", "avatarId")
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    avatarId: str
    def __init__(self, friendGpid: _Optional[str] = ..., avatarId: _Optional[str] = ...) -> None: ...

class OnLobbyMaxMembersChangedEvent(_message.Message):
    __slots__ = ("maxMembers",)
    MAXMEMBERS_FIELD_NUMBER: _ClassVar[int]
    maxMembers: int
    def __init__(self, maxMembers: _Optional[int] = ...) -> None: ...

class OnClanTypeChanged(_message.Message):
    __slots__ = ("newClanType",)
    NEWCLANTYPE_FIELD_NUMBER: _ClassVar[int]
    newClanType: ClanType
    def __init__(self, newClanType: _Optional[_Union[ClanType, str]] = ...) -> None: ...

class OnTradeRequestClosedEvent(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: ClosedRequest
    def __init__(self, request: _Optional[_Union[ClosedRequest, _Mapping]] = ...) -> None: ...

class OnMsgFromFriendEvent(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: UserMessage
    def __init__(self, message: _Optional[_Union[UserMessage, _Mapping]] = ...) -> None: ...

class GetStatsForSeasonRequest(_message.Message):
    __slots__ = ("seasonId",)
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    seasonId: str
    def __init__(self, seasonId: _Optional[str] = ...) -> None: ...

class SendLobbyChatMsgRequest(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Handshake(_message.Message):
    __slots__ = ("ticket",)
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: str
    def __init__(self, ticket: _Optional[str] = ...) -> None: ...

class OnFriendAddedEvent(_message.Message):
    __slots__ = ("friend",)
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    friend: PlayerFriend
    def __init__(self, friend: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class GetRolesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetDefaultAvatarResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetItemsModificationsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTradeRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class OnAssignedLeaderRoleEvent(_message.Message):
    __slots__ = ("oldLeaderRole", "newLeaderId")
    OLDLEADERROLE_FIELD_NUMBER: _ClassVar[int]
    NEWLEADERID_FIELD_NUMBER: _ClassVar[int]
    oldLeaderRole: int
    newLeaderId: str
    def __init__(self, oldLeaderRole: _Optional[int] = ..., newLeaderId: _Optional[str] = ...) -> None: ...

class RevokeFriendRequestResponse(_message.Message):
    __slots__ = ("relationshipStatus",)
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class OnRevokeInviteToLobbyEvent(_message.Message):
    __slots__ = ("inviteSenderGpid", "invitedGpid")
    INVITESENDERGPID_FIELD_NUMBER: _ClassVar[int]
    INVITEDGPID_FIELD_NUMBER: _ClassVar[int]
    inviteSenderGpid: str
    invitedGpid: str
    def __init__(self, inviteSenderGpid: _Optional[str] = ..., invitedGpid: _Optional[str] = ...) -> None: ...

class DeleteAccountResponse(_message.Message):
    __slots__ = ("email", "daysLeft")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DAYSLEFT_FIELD_NUMBER: _ClassVar[int]
    email: str
    daysLeft: int
    def __init__(self, email: _Optional[str] = ..., daysLeft: _Optional[int] = ...) -> None: ...

class CancelRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetLobbyMaxSpectatorsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPlayerInviteRequestsResponse(_message.Message):
    __slots__ = ("clanInviteRequests",)
    CLANINVITEREQUESTS_FIELD_NUMBER: _ClassVar[int]
    clanInviteRequests: _containers.RepeatedCompositeFieldContainer[ClanInviteRequest]
    def __init__(self, clanInviteRequests: _Optional[_Iterable[_Union[ClanInviteRequest, _Mapping]]] = ...) -> None: ...

class OnNewFriendshipRequestEvent(_message.Message):
    __slots__ = ("friend", "msg")
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    friend: PlayerFriend
    msg: str
    def __init__(self, friend: _Optional[_Union[PlayerFriend, _Mapping]] = ..., msg: _Optional[str] = ...) -> None: ...

class GetCurrentClanStatsForSeasonRequest(_message.Message):
    __slots__ = ("seasonId",)
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    seasonId: str
    def __init__(self, seasonId: _Optional[str] = ...) -> None: ...

class FindCreatorResponse(_message.Message):
    __slots__ = ("creator",)
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    creator: Creator
    def __init__(self, creator: _Optional[_Union[Creator, _Mapping]] = ...) -> None: ...

class PreviewDlcRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnmountInventoryItemResponse(_message.Message):
    __slots__ = ("unmountedItem",)
    UNMOUNTEDITEM_FIELD_NUMBER: _ClassVar[int]
    unmountedItem: PlayerInventoryItem
    def __init__(self, unmountedItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class SetPlayerNameRequest(_message.Message):
    __slots__ = ("newName",)
    NEWNAME_FIELD_NUMBER: _ClassVar[int]
    newName: str
    def __init__(self, newName: _Optional[str] = ...) -> None: ...

class OnClanAvatarChangedEvent(_message.Message):
    __slots__ = ("avatarId", "avatar")
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    avatar: bytes
    def __init__(self, avatarId: _Optional[str] = ..., avatar: _Optional[bytes] = ...) -> None: ...

class CountUnreadSystemMessagesResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class MountInventoryItemResponse(_message.Message):
    __slots__ = ("modifiedItem", "unmountedItem")
    MODIFIEDITEM_FIELD_NUMBER: _ClassVar[int]
    UNMOUNTEDITEM_FIELD_NUMBER: _ClassVar[int]
    modifiedItem: PlayerInventoryItem
    unmountedItem: PlayerInventoryItem
    def __init__(self, modifiedItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ..., unmountedItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class GetDefaultAvatarsResponse(_message.Message):
    __slots__ = ("avatars", "lastUpdated")
    AVATARS_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    avatars: _containers.RepeatedCompositeFieldContainer[DefaultAvatar]
    lastUpdated: str
    def __init__(self, avatars: _Optional[_Iterable[_Union[DefaultAvatar, _Mapping]]] = ..., lastUpdated: _Optional[str] = ...) -> None: ...

class GetTradesRequest(_message.Message):
    __slots__ = ("itemDefinitionIds",)
    ITEMDEFINITIONIDS_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, itemDefinitionIds: _Optional[_Iterable[int]] = ...) -> None: ...

class AppleIdAuthRequest(_message.Message):
    __slots__ = ("authAppleId", "appVerification", "deviceInfo")
    AUTHAPPLEID_FIELD_NUMBER: _ClassVar[int]
    APPVERIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEVICEINFO_FIELD_NUMBER: _ClassVar[int]
    authAppleId: AuthAppleId
    appVerification: AppVerification
    deviceInfo: DeviceInfo
    def __init__(self, authAppleId: _Optional[_Union[AuthAppleId, _Mapping]] = ..., appVerification: _Optional[_Union[AppVerification, _Mapping]] = ..., deviceInfo: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class RecoverAccountRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GoogleLinkAuthRequest(_message.Message):
    __slots__ = ("authGoogle",)
    AUTHGOOGLE_FIELD_NUMBER: _ClassVar[int]
    authGoogle: AuthGoogle
    def __init__(self, authGoogle: _Optional[_Union[AuthGoogle, _Mapping]] = ...) -> None: ...

class GetRecommendedClansResponse(_message.Message):
    __slots__ = ("clan",)
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: _containers.RepeatedCompositeFieldContainer[Clan]
    def __init__(self, clan: _Optional[_Iterable[_Union[Clan, _Mapping]]] = ...) -> None: ...

class GetPlayerAchievementsRequest(_message.Message):
    __slots__ = ("gpid", "showLocked")
    GPID_FIELD_NUMBER: _ClassVar[int]
    SHOWLOCKED_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    showLocked: bool
    def __init__(self, gpid: _Optional[str] = ..., showLocked: bool = ...) -> None: ...

class GetChatUserRequest(_message.Message):
    __slots__ = ("friendGpid",)
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class GoogleLinkAuthResponse(_message.Message):
    __slots__ = ("guestLinking",)
    GUESTLINKING_FIELD_NUMBER: _ClassVar[int]
    guestLinking: bool
    def __init__(self, guestLinking: bool = ...) -> None: ...

class StorePlayerStats(_message.Message):
    __slots__ = ("gpid", "stats", "seasonId")
    GPID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    stats: _containers.RepeatedCompositeFieldContainer[StorePlayerStat]
    seasonId: str
    def __init__(self, gpid: _Optional[str] = ..., stats: _Optional[_Iterable[_Union[StorePlayerStat, _Mapping]]] = ..., seasonId: _Optional[str] = ...) -> None: ...

class RateContext(_message.Message):
    __slots__ = ("id", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: str
    def __init__(self, id: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class RewardInfo(_message.Message):
    __slots__ = ("items", "currencies", "recipes")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[InventoryItemAmount]
    currencies: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    recipes: _containers.RepeatedCompositeFieldContainer[RecipeInfo]
    def __init__(self, items: _Optional[_Iterable[_Union[InventoryItemAmount, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., recipes: _Optional[_Iterable[_Union[RecipeInfo, _Mapping]]] = ...) -> None: ...

class PlayerStatus(_message.Message):
    __slots__ = ("gpid", "playInGame", "onlineStatus")
    GPID_FIELD_NUMBER: _ClassVar[int]
    PLAYINGAME_FIELD_NUMBER: _ClassVar[int]
    ONLINESTATUS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    playInGame: PlayInGame
    onlineStatus: OnlineStatus
    def __init__(self, gpid: _Optional[str] = ..., playInGame: _Optional[_Union[PlayInGame, _Mapping]] = ..., onlineStatus: _Optional[_Union[OnlineStatus, str]] = ...) -> None: ...

class ClanStats(_message.Message):
    __slots__ = ("clanId", "stats", "seasonId")
    CLANID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    stats: _containers.RepeatedCompositeFieldContainer[ClanStat]
    seasonId: str
    def __init__(self, clanId: _Optional[str] = ..., stats: _Optional[_Iterable[_Union[ClanStat, _Mapping]]] = ..., seasonId: _Optional[str] = ...) -> None: ...

class ClanMemberStats(_message.Message):
    __slots__ = ("gpid", "stats", "version")
    GPID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    stats: _containers.RepeatedCompositeFieldContainer[ClanMemberStat]
    version: int
    def __init__(self, gpid: _Optional[str] = ..., stats: _Optional[_Iterable[_Union[ClanMemberStat, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class Stats(_message.Message):
    __slots__ = ("stat", "seasonId", "updatedDate")
    STAT_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    stat: _containers.RepeatedCompositeFieldContainer[PlayerStat]
    seasonId: str
    updatedDate: int
    def __init__(self, stat: _Optional[_Iterable[_Union[PlayerStat, _Mapping]]] = ..., seasonId: _Optional[str] = ..., updatedDate: _Optional[int] = ...) -> None: ...

class ItemFlags(_message.Message):
    __slots__ = ("flags",)
    class FlagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    flags: _containers.ScalarMap[int, int]
    def __init__(self, flags: _Optional[_Mapping[int, int]] = ...) -> None: ...

class CurrencyAmount(_message.Message):
    __slots__ = ("currencyId", "oldValue", "value")
    CURRENCYID_FIELD_NUMBER: _ClassVar[int]
    OLDVALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    currencyId: int
    oldValue: int
    value: float
    def __init__(self, currencyId: _Optional[int] = ..., oldValue: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...

class PlayerInventoryItem(_message.Message):
    __slots__ = ("id", "itemDefinitionId", "quantity", "flags", "date", "modifications", "block")
    class ModificationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    itemDefinitionId: int
    quantity: int
    flags: int
    date: int
    modifications: _containers.MessageMap[str, ItemModificationValue]
    block: BlockedAction
    def __init__(self, id: _Optional[int] = ..., itemDefinitionId: _Optional[int] = ..., quantity: _Optional[int] = ..., flags: _Optional[int] = ..., date: _Optional[int] = ..., modifications: _Optional[_Mapping[str, ItemModificationValue]] = ..., block: _Optional[_Union[BlockedAction, _Mapping]] = ...) -> None: ...

class Lobby(_message.Message):
    __slots__ = ("id", "ownerGpid", "name", "lobbyType", "joinable", "maxMembers", "data", "members", "invites", "gameServer", "photonGame", "maxSpectators", "spectators", "spectatorInvites", "numberOfMembers", "numberOfSpectators", "token")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNERGPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOBBYTYPE_FIELD_NUMBER: _ClassVar[int]
    JOINABLE_FIELD_NUMBER: _ClassVar[int]
    MAXMEMBERS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    INVITES_FIELD_NUMBER: _ClassVar[int]
    GAMESERVER_FIELD_NUMBER: _ClassVar[int]
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    MAXSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    SPECTATORS_FIELD_NUMBER: _ClassVar[int]
    SPECTATORINVITES_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFMEMBERS_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFSPECTATORS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    ownerGpid: str
    name: str
    lobbyType: LobbyType
    joinable: bool
    maxMembers: int
    data: _containers.ScalarMap[str, str]
    members: _containers.RepeatedCompositeFieldContainer[PlayerFriend]
    invites: _containers.RepeatedCompositeFieldContainer[PlayerFriend]
    gameServer: GameServer
    photonGame: PhotonGame
    maxSpectators: int
    spectators: _containers.RepeatedCompositeFieldContainer[PlayerFriend]
    spectatorInvites: _containers.RepeatedCompositeFieldContainer[PlayerFriend]
    numberOfMembers: int
    numberOfSpectators: int
    token: str
    def __init__(self, id: _Optional[str] = ..., ownerGpid: _Optional[str] = ..., name: _Optional[str] = ..., lobbyType: _Optional[_Union[LobbyType, str]] = ..., joinable: bool = ..., maxMembers: _Optional[int] = ..., data: _Optional[_Mapping[str, str]] = ..., members: _Optional[_Iterable[_Union[PlayerFriend, _Mapping]]] = ..., invites: _Optional[_Iterable[_Union[PlayerFriend, _Mapping]]] = ..., gameServer: _Optional[_Union[GameServer, _Mapping]] = ..., photonGame: _Optional[_Union[PhotonGame, _Mapping]] = ..., maxSpectators: _Optional[int] = ..., spectators: _Optional[_Iterable[_Union[PlayerFriend, _Mapping]]] = ..., spectatorInvites: _Optional[_Iterable[_Union[PlayerFriend, _Mapping]]] = ..., numberOfMembers: _Optional[int] = ..., numberOfSpectators: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class LobbyInvite(_message.Message):
    __slots__ = ("lobbyId", "inviteSender", "date", "playerType", "lobbyName")
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    INVITESENDER_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    PLAYERTYPE_FIELD_NUMBER: _ClassVar[int]
    LOBBYNAME_FIELD_NUMBER: _ClassVar[int]
    lobbyId: str
    inviteSender: PlayerFriend
    date: int
    playerType: LobbyPlayerType
    lobbyName: str
    def __init__(self, lobbyId: _Optional[str] = ..., inviteSender: _Optional[_Union[PlayerFriend, _Mapping]] = ..., date: _Optional[int] = ..., playerType: _Optional[_Union[LobbyPlayerType, str]] = ..., lobbyName: _Optional[str] = ...) -> None: ...

class Offset(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class AAGDEBAFFCFGFCH(_message.Message):
    __slots__ = ("GHEGBECBCEBHBDF", "EBGDDAACACBFAED", "ACHAFHDFCCBHDFD")
    GHEGBECBCEBHBDF_FIELD_NUMBER: _ClassVar[int]
    EBGDDAACACBFAED_FIELD_NUMBER: _ClassVar[int]
    ACHAFHDFCCBHDFD_FIELD_NUMBER: _ClassVar[int]
    GHEGBECBCEBHBDF: _containers.RepeatedCompositeFieldContainer[HGGCCFDEHCGDEAD]
    EBGDDAACACBFAED: str
    ACHAFHDFCCBHDFD: str
    def __init__(self, GHEGBECBCEBHBDF: _Optional[_Iterable[_Union[HGGCCFDEHCGDEAD, _Mapping]]] = ..., EBGDDAACACBFAED: _Optional[str] = ..., ACHAFHDFCCBHDFD: _Optional[str] = ...) -> None: ...

class Dictionary(_message.Message):
    __slots__ = ("content",)
    class ContentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: _containers.ScalarMap[str, str]
    def __init__(self, content: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GivenReward(_message.Message):
    __slots__ = ("items", "currencies", "changedItems", "stats")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    CHANGEDITEMS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    currencies: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    changedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    stats: _containers.RepeatedCompositeFieldContainer[StatAmount]
    def __init__(self, items: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., changedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., stats: _Optional[_Iterable[_Union[StatAmount, _Mapping]]] = ...) -> None: ...

class ClanUserMessage(_message.Message):
    __slots__ = ("id", "timestamp", "messageType", "chatMessage", "logMessage")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGETYPE_FIELD_NUMBER: _ClassVar[int]
    CHATMESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOGMESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: int
    messageType: MessageType
    chatMessage: ClanChatMessage
    logMessage: ClanLogMessage
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[int] = ..., messageType: _Optional[_Union[MessageType, str]] = ..., chatMessage: _Optional[_Union[ClanChatMessage, _Mapping]] = ..., logMessage: _Optional[_Union[ClanLogMessage, _Mapping]] = ...) -> None: ...

class SystemMessageDetails(_message.Message):
    __slots__ = ("messageId", "type", "created", "deleteAt", "achievementUnlocked", "avatarRejected", "clanMembershipAccepted", "clanMembershipEnded", "developersMessageReceived", "friendshipRequestAccepted", "giftReceived", "marketplaceTransactionReverted", "matchesCanceled", "globalBanReceived", "reportedPlayersBanned", "seasonFinished", "marketplaceBanReceived", "chatBanReceived", "matchesRestored", "inAppSucceed", "newDeviceLogined")
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETEAT_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENTUNLOCKED_FIELD_NUMBER: _ClassVar[int]
    AVATARREJECTED_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSHIPACCEPTED_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSHIPENDED_FIELD_NUMBER: _ClassVar[int]
    DEVELOPERSMESSAGERECEIVED_FIELD_NUMBER: _ClassVar[int]
    FRIENDSHIPREQUESTACCEPTED_FIELD_NUMBER: _ClassVar[int]
    GIFTRECEIVED_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACETRANSACTIONREVERTED_FIELD_NUMBER: _ClassVar[int]
    MATCHESCANCELED_FIELD_NUMBER: _ClassVar[int]
    GLOBALBANRECEIVED_FIELD_NUMBER: _ClassVar[int]
    REPORTEDPLAYERSBANNED_FIELD_NUMBER: _ClassVar[int]
    SEASONFINISHED_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACEBANRECEIVED_FIELD_NUMBER: _ClassVar[int]
    CHATBANRECEIVED_FIELD_NUMBER: _ClassVar[int]
    MATCHESRESTORED_FIELD_NUMBER: _ClassVar[int]
    INAPPSUCCEED_FIELD_NUMBER: _ClassVar[int]
    NEWDEVICELOGINED_FIELD_NUMBER: _ClassVar[int]
    messageId: str
    type: SystemMessageType
    created: int
    deleteAt: int
    achievementUnlocked: SMAchievementUnlocked
    avatarRejected: SMAvatarRejected
    clanMembershipAccepted: SMClanMembershipAccepted
    clanMembershipEnded: SMClanMembershipEnded
    developersMessageReceived: SMDevelopersMessageReceived
    friendshipRequestAccepted: SMFriendshipRequestAccepted
    giftReceived: SMGiftReceived
    marketplaceTransactionReverted: SMMarketplaceTransactionReverted
    matchesCanceled: SMMatchesCanceled
    globalBanReceived: SMGlobalBanReceived
    reportedPlayersBanned: SMReportedPlayersBanned
    seasonFinished: SMSeasonFinished
    marketplaceBanReceived: SMMarketplaceBanReceived
    chatBanReceived: SMChatBanReceived
    matchesRestored: SMMatchesRestored
    inAppSucceed: SMInAppSucceed
    newDeviceLogined: SMNewDeviceLogined
    def __init__(self, messageId: _Optional[str] = ..., type: _Optional[_Union[SystemMessageType, str]] = ..., created: _Optional[int] = ..., deleteAt: _Optional[int] = ..., achievementUnlocked: _Optional[_Union[SMAchievementUnlocked, _Mapping]] = ..., avatarRejected: _Optional[_Union[SMAvatarRejected, _Mapping]] = ..., clanMembershipAccepted: _Optional[_Union[SMClanMembershipAccepted, _Mapping]] = ..., clanMembershipEnded: _Optional[_Union[SMClanMembershipEnded, _Mapping]] = ..., developersMessageReceived: _Optional[_Union[SMDevelopersMessageReceived, _Mapping]] = ..., friendshipRequestAccepted: _Optional[_Union[SMFriendshipRequestAccepted, _Mapping]] = ..., giftReceived: _Optional[_Union[SMGiftReceived, _Mapping]] = ..., marketplaceTransactionReverted: _Optional[_Union[SMMarketplaceTransactionReverted, _Mapping]] = ..., matchesCanceled: _Optional[_Union[SMMatchesCanceled, _Mapping]] = ..., globalBanReceived: _Optional[_Union[SMGlobalBanReceived, _Mapping]] = ..., reportedPlayersBanned: _Optional[_Union[SMReportedPlayersBanned, _Mapping]] = ..., seasonFinished: _Optional[_Union[SMSeasonFinished, _Mapping]] = ..., marketplaceBanReceived: _Optional[_Union[SMMarketplaceBanReceived, _Mapping]] = ..., chatBanReceived: _Optional[_Union[SMChatBanReceived, _Mapping]] = ..., matchesRestored: _Optional[_Union[SMMatchesRestored, _Mapping]] = ..., inAppSucceed: _Optional[_Union[SMInAppSucceed, _Mapping]] = ..., newDeviceLogined: _Optional[_Union[SMNewDeviceLogined, _Mapping]] = ...) -> None: ...

class OpenRequest(_message.Message):
    __slots__ = ("id", "creator", "itemDefinitionId", "price", "createDate", "type", "quantity", "modifications", "isCreator")
    class ModificationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    ISCREATOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    creator: Player
    itemDefinitionId: int
    price: float
    createDate: int
    type: MarketRequestType
    quantity: int
    modifications: _containers.MessageMap[str, ItemModificationValue]
    isCreator: bool
    def __init__(self, id: _Optional[str] = ..., creator: _Optional[_Union[Player, _Mapping]] = ..., itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., createDate: _Optional[int] = ..., type: _Optional[_Union[MarketRequestType, str]] = ..., quantity: _Optional[int] = ..., modifications: _Optional[_Mapping[str, ItemModificationValue]] = ..., isCreator: bool = ...) -> None: ...

class ProgressGameEventContext(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ProgressGameEventType
    def __init__(self, type: _Optional[_Union[ProgressGameEventType, str]] = ...) -> None: ...

class ListOfLevelsToClaimReward(_message.Message):
    __slots__ = ("levels",)
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, levels: _Optional[_Iterable[int]] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("id", "definitionId", "gpid", "itemText", "timestamp")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    ITEMTEXT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    definitionId: str
    gpid: str
    itemText: str
    timestamp: int
    def __init__(self, id: _Optional[str] = ..., definitionId: _Optional[str] = ..., gpid: _Optional[str] = ..., itemText: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class PlayerSettings(_message.Message):
    __slots__ = ("settings",)
    class SettingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.ScalarMap[str, str]
    def __init__(self, settings: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PlayerFriend(_message.Message):
    __slots__ = ("player", "relationshipStatus", "lastRelationshipUpdate", "msg")
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    LASTRELATIONSHIPUPDATE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    player: Player
    relationshipStatus: RelationshipStatus
    lastRelationshipUpdate: int
    msg: str
    def __init__(self, player: _Optional[_Union[Player, _Mapping]] = ..., relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ..., lastRelationshipUpdate: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...

class AuthFacebook(_message.Message):
    __slots__ = ("gameId", "gameVersion", "platform", "token", "locale", "store")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    platform: Platform
    token: str
    locale: str
    store: Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., token: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[Store, str]] = ...) -> None: ...

class AppVerification(_message.Message):
    __slots__ = ("isRooted", "apkHash", "jsonForbiddenApps", "path", "contentHash", "appSnapshot", "n", "e", "environment", "token")
    class AppSnapshotEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ISROOTED_FIELD_NUMBER: _ClassVar[int]
    APKHASH_FIELD_NUMBER: _ClassVar[int]
    JSONFORBIDDENAPPS_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENTHASH_FIELD_NUMBER: _ClassVar[int]
    APPSNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    E_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    isRooted: bool
    apkHash: str
    jsonForbiddenApps: _containers.RepeatedScalarFieldContainer[str]
    path: str
    contentHash: str
    appSnapshot: _containers.ScalarMap[str, str]
    n: bytes
    e: bytes
    environment: EnvironmentInfo
    token: str
    def __init__(self, isRooted: bool = ..., apkHash: _Optional[str] = ..., jsonForbiddenApps: _Optional[_Iterable[str]] = ..., path: _Optional[str] = ..., contentHash: _Optional[str] = ..., appSnapshot: _Optional[_Mapping[str, str]] = ..., n: _Optional[bytes] = ..., e: _Optional[bytes] = ..., environment: _Optional[_Union[EnvironmentInfo, _Mapping]] = ..., token: _Optional[str] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ("deviceId", "deviceModel", "adsId")
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    DEVICEMODEL_FIELD_NUMBER: _ClassVar[int]
    ADSID_FIELD_NUMBER: _ClassVar[int]
    deviceId: str
    deviceModel: str
    adsId: str
    def __init__(self, deviceId: _Optional[str] = ..., deviceModel: _Optional[str] = ..., adsId: _Optional[str] = ...) -> None: ...

class Clan(_message.Message):
    __slots__ = ("id", "name", "tag", "clanType", "avatarId", "createDate", "mebersCount", "maxMemberCount", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    CLANTYPE_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    MEBERSCOUNT_FIELD_NUMBER: _ClassVar[int]
    MAXMEMBERCOUNT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    tag: str
    clanType: ClanType
    avatarId: str
    createDate: int
    mebersCount: int
    maxMemberCount: int
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., tag: _Optional[str] = ..., clanType: _Optional[_Union[ClanType, str]] = ..., avatarId: _Optional[str] = ..., createDate: _Optional[int] = ..., mebersCount: _Optional[int] = ..., maxMemberCount: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class UserMessage(_message.Message):
    __slots__ = ("senderGpid", "message", "timestamp", "isRead")
    SENDERGPID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ISREAD_FIELD_NUMBER: _ClassVar[int]
    senderGpid: str
    message: str
    timestamp: int
    isRead: bool
    def __init__(self, senderGpid: _Optional[str] = ..., message: _Optional[str] = ..., timestamp: _Optional[int] = ..., isRead: bool = ...) -> None: ...

class PlayerStat(_message.Message):
    __slots__ = ("name", "intValue", "floatValue", "window", "type", "longValue")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    intValue: int
    floatValue: float
    window: float
    type: StatDefType
    longValue: int
    def __init__(self, name: _Optional[str] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., window: _Optional[float] = ..., type: _Optional[_Union[StatDefType, str]] = ..., longValue: _Optional[int] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ("id", "salesCount", "purchasesCount", "salesPrice", "purchasesPrice")
    ID_FIELD_NUMBER: _ClassVar[int]
    SALESCOUNT_FIELD_NUMBER: _ClassVar[int]
    PURCHASESCOUNT_FIELD_NUMBER: _ClassVar[int]
    SALESPRICE_FIELD_NUMBER: _ClassVar[int]
    PURCHASESPRICE_FIELD_NUMBER: _ClassVar[int]
    id: int
    salesCount: int
    purchasesCount: int
    salesPrice: float
    purchasesPrice: float
    def __init__(self, id: _Optional[int] = ..., salesCount: _Optional[int] = ..., purchasesCount: _Optional[int] = ..., salesPrice: _Optional[float] = ..., purchasesPrice: _Optional[float] = ...) -> None: ...

class Player(_message.Message):
    __slots__ = ("gpid", "uid", "name", "avatarId", "timeInGame", "playerStatus", "logoutDate", "registrationDate", "attributes", "testerRole", "bans", "deleted", "tags", "guest")
    GPID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    TIMEINGAME_FIELD_NUMBER: _ClassVar[int]
    PLAYERSTATUS_FIELD_NUMBER: _ClassVar[int]
    LOGOUTDATE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TESTERROLE_FIELD_NUMBER: _ClassVar[int]
    BANS_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    GUEST_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    uid: str
    name: str
    avatarId: str
    timeInGame: int
    playerStatus: PlayerStatus
    logoutDate: int
    registrationDate: int
    attributes: Attributes
    testerRole: str
    bans: _containers.RepeatedCompositeFieldContainer[PlayerBan]
    deleted: bool
    tags: _containers.RepeatedScalarFieldContainer[int]
    guest: bool
    def __init__(self, gpid: _Optional[str] = ..., uid: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., timeInGame: _Optional[int] = ..., playerStatus: _Optional[_Union[PlayerStatus, _Mapping]] = ..., logoutDate: _Optional[int] = ..., registrationDate: _Optional[int] = ..., attributes: _Optional[_Union[Attributes, _Mapping]] = ..., testerRole: _Optional[str] = ..., bans: _Optional[_Iterable[_Union[PlayerBan, _Mapping]]] = ..., deleted: bool = ..., tags: _Optional[_Iterable[int]] = ..., guest: bool = ...) -> None: ...

class SystemMessagePreview(_message.Message):
    __slots__ = ("messageId", "type", "isRead", "created", "deleteAt")
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ISREAD_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETEAT_FIELD_NUMBER: _ClassVar[int]
    messageId: str
    type: SystemMessageType
    isRead: bool
    created: int
    deleteAt: int
    def __init__(self, messageId: _Optional[str] = ..., type: _Optional[_Union[SystemMessageType, str]] = ..., isRead: bool = ..., created: _Optional[int] = ..., deleteAt: _Optional[int] = ...) -> None: ...

class SpecialOffer(_message.Message):
    __slots__ = ("id", "title", "body", "resourceUrl", "type", "inappOffer", "storeOffer", "dateUntil", "offersCount", "dateSince", "settings", "key")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    RESOURCEURL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INAPPOFFER_FIELD_NUMBER: _ClassVar[int]
    STOREOFFER_FIELD_NUMBER: _ClassVar[int]
    DATEUNTIL_FIELD_NUMBER: _ClassVar[int]
    OFFERSCOUNT_FIELD_NUMBER: _ClassVar[int]
    DATESINCE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    body: str
    resourceUrl: str
    type: OfferType
    inappOffer: InAppOffer
    storeOffer: StoreOffer
    dateUntil: int
    offersCount: int
    dateSince: int
    settings: _containers.RepeatedCompositeFieldContainer[Property]
    key: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., resourceUrl: _Optional[str] = ..., type: _Optional[_Union[OfferType, str]] = ..., inappOffer: _Optional[_Union[InAppOffer, _Mapping]] = ..., storeOffer: _Optional[_Union[StoreOffer, _Mapping]] = ..., dateUntil: _Optional[int] = ..., offersCount: _Optional[int] = ..., dateSince: _Optional[int] = ..., settings: _Optional[_Iterable[_Union[Property, _Mapping]]] = ..., key: _Optional[str] = ...) -> None: ...

class PhotonGame(_message.Message):
    __slots__ = ("region", "roomId", "appVersion", "customProperties")
    class CustomPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REGION_FIELD_NUMBER: _ClassVar[int]
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    APPVERSION_FIELD_NUMBER: _ClassVar[int]
    CUSTOMPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    region: str
    roomId: str
    appVersion: str
    customProperties: _containers.ScalarMap[str, str]
    def __init__(self, region: _Optional[str] = ..., roomId: _Optional[str] = ..., appVersion: _Optional[str] = ..., customProperties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PlayerAchievement(_message.Message):
    __slots__ = ("id", "key", "title", "imageLocked", "imageUnlocked", "progressCurrent", "progressTarget", "unlockDate")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGELOCKED_FIELD_NUMBER: _ClassVar[int]
    IMAGEUNLOCKED_FIELD_NUMBER: _ClassVar[int]
    PROGRESSCURRENT_FIELD_NUMBER: _ClassVar[int]
    PROGRESSTARGET_FIELD_NUMBER: _ClassVar[int]
    UNLOCKDATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    title: LocalizedTitle
    imageLocked: str
    imageUnlocked: str
    progressCurrent: int
    progressTarget: int
    unlockDate: int
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., title: _Optional[_Union[LocalizedTitle, _Mapping]] = ..., imageLocked: _Optional[str] = ..., imageUnlocked: _Optional[str] = ..., progressCurrent: _Optional[int] = ..., progressTarget: _Optional[int] = ..., unlockDate: _Optional[int] = ...) -> None: ...

class AuthTest(_message.Message):
    __slots__ = ("gameId", "gameVersion", "platform", "token", "locale", "store")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    platform: Platform
    token: str
    locale: str
    store: Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., token: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[Store, str]] = ...) -> None: ...

class ChatUserLite(_message.Message):
    __slots__ = ("friendGpid", "groupId", "message", "timestamp", "unreadMsgsCount")
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNREADMSGSCOUNT_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    groupId: str
    message: str
    timestamp: int
    unreadMsgsCount: int
    def __init__(self, friendGpid: _Optional[str] = ..., groupId: _Optional[str] = ..., message: _Optional[str] = ..., timestamp: _Optional[int] = ..., unreadMsgsCount: _Optional[int] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("name", "intValue", "floatValue", "stringValue", "comparison", "stringsValue")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    STRINGSVALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    intValue: int
    floatValue: float
    stringValue: str
    comparison: Comparison
    stringsValue: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., stringValue: _Optional[str] = ..., comparison: _Optional[_Union[Comparison, str]] = ..., stringsValue: _Optional[_Iterable[str]] = ...) -> None: ...

class PlayerStats(_message.Message):
    __slots__ = ("gpid", "stats")
    GPID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    stats: Stats
    def __init__(self, gpid: _Optional[str] = ..., stats: _Optional[_Union[Stats, _Mapping]] = ...) -> None: ...

class AchievementDefinition(_message.Message):
    __slots__ = ("id", "key", "title", "imageLocked", "imageUnlocked")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGELOCKED_FIELD_NUMBER: _ClassVar[int]
    IMAGEUNLOCKED_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    title: LocalizedTitle
    imageLocked: str
    imageUnlocked: str
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., title: _Optional[_Union[LocalizedTitle, _Mapping]] = ..., imageLocked: _Optional[str] = ..., imageUnlocked: _Optional[str] = ...) -> None: ...

class PlayerInventory(_message.Message):
    __slots__ = ("currencies", "inventoryItems")
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    inventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, currencies: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., inventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class GameEventDefinition(_message.Message):
    __slots__ = ("id", "code", "dateSince", "dateUntil", "durationDays", "gamePasses", "challenges", "settings", "title")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATESINCE_FIELD_NUMBER: _ClassVar[int]
    DATEUNTIL_FIELD_NUMBER: _ClassVar[int]
    DURATIONDAYS_FIELD_NUMBER: _ClassVar[int]
    GAMEPASSES_FIELD_NUMBER: _ClassVar[int]
    CHALLENGES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    dateSince: int
    dateUntil: int
    durationDays: int
    gamePasses: _containers.RepeatedCompositeFieldContainer[GamePassDefinition]
    challenges: _containers.RepeatedCompositeFieldContainer[ChallengeDefinition]
    settings: _containers.RepeatedCompositeFieldContainer[Property]
    title: LocalizedTitle
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., dateSince: _Optional[int] = ..., dateUntil: _Optional[int] = ..., durationDays: _Optional[int] = ..., gamePasses: _Optional[_Iterable[_Union[GamePassDefinition, _Mapping]]] = ..., challenges: _Optional[_Iterable[_Union[ChallengeDefinition, _Mapping]]] = ..., settings: _Optional[_Iterable[_Union[Property, _Mapping]]] = ..., title: _Optional[_Union[LocalizedTitle, _Mapping]] = ...) -> None: ...

class InventoryItemDefinition(_message.Message):
    __slots__ = ("id", "displayName", "properties", "buyPrice", "sellPrice", "canBeTraded", "definitions", "maxStackSize")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DefinitionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InventoryItemPropertyDefinition
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[InventoryItemPropertyDefinition, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    BUYPRICE_FIELD_NUMBER: _ClassVar[int]
    SELLPRICE_FIELD_NUMBER: _ClassVar[int]
    CANBETRADED_FIELD_NUMBER: _ClassVar[int]
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    MAXSTACKSIZE_FIELD_NUMBER: _ClassVar[int]
    id: int
    displayName: str
    properties: _containers.ScalarMap[str, str]
    buyPrice: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    sellPrice: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    canBeTraded: bool
    definitions: _containers.MessageMap[str, InventoryItemPropertyDefinition]
    maxStackSize: int
    def __init__(self, id: _Optional[int] = ..., displayName: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ..., buyPrice: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., sellPrice: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., canBeTraded: bool = ..., definitions: _Optional[_Mapping[str, InventoryItemPropertyDefinition]] = ..., maxStackSize: _Optional[int] = ...) -> None: ...

class ClanMember(_message.Message):
    __slots__ = ("playerFriend", "clanId", "roleId", "createDate")
    PLAYERFRIEND_FIELD_NUMBER: _ClassVar[int]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    ROLEID_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    playerFriend: PlayerFriend
    clanId: str
    roleId: int
    createDate: int
    def __init__(self, playerFriend: _Optional[_Union[PlayerFriend, _Mapping]] = ..., clanId: _Optional[str] = ..., roleId: _Optional[int] = ..., createDate: _Optional[int] = ...) -> None: ...

class ExchangeRecipeResult(_message.Message):
    __slots__ = ("currencies", "addedItems", "changedItems", "stats")
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ADDEDITEMS_FIELD_NUMBER: _ClassVar[int]
    CHANGEDITEMS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    addedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    changedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    stats: _containers.RepeatedCompositeFieldContainer[StatAmount]
    def __init__(self, currencies: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., addedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., changedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., stats: _Optional[_Iterable[_Union[StatAmount, _Mapping]]] = ...) -> None: ...

class ClanJoinRequest(_message.Message):
    __slots__ = ("id", "clan", "requestSender", "createDate", "closeDate", "requestType")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    REQUESTSENDER_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    CLOSEDATE_FIELD_NUMBER: _ClassVar[int]
    REQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    clan: Clan
    requestSender: Player
    createDate: int
    closeDate: int
    requestType: RequestType
    def __init__(self, id: _Optional[str] = ..., clan: _Optional[_Union[Clan, _Mapping]] = ..., requestSender: _Optional[_Union[Player, _Mapping]] = ..., createDate: _Optional[int] = ..., closeDate: _Optional[int] = ..., requestType: _Optional[_Union[RequestType, str]] = ...) -> None: ...

class AuthVk(_message.Message):
    __slots__ = ("gameId", "gameVersion", "platform", "authCode", "locale", "store")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    AUTHCODE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    platform: Platform
    authCode: str
    locale: str
    store: Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., authCode: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[Store, str]] = ...) -> None: ...

class MarketplaceSettings(_message.Message):
    __slots__ = ("commissionPercent", "minCommission", "currencyId", "enabled", "banned")
    COMMISSIONPERCENT_FIELD_NUMBER: _ClassVar[int]
    MINCOMMISSION_FIELD_NUMBER: _ClassVar[int]
    CURRENCYID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    BANNED_FIELD_NUMBER: _ClassVar[int]
    commissionPercent: float
    minCommission: float
    currencyId: int
    enabled: bool
    banned: Banned
    def __init__(self, commissionPercent: _Optional[float] = ..., minCommission: _Optional[float] = ..., currencyId: _Optional[int] = ..., enabled: bool = ..., banned: _Optional[_Union[Banned, _Mapping]] = ...) -> None: ...

class ClanSettings(_message.Message):
    __slots__ = ("initialMembersCount", "membersCountLimit", "membercCountUpgradeCost", "changeClanNameOrTagCost", "clanCreateCost")
    INITIALMEMBERSCOUNT_FIELD_NUMBER: _ClassVar[int]
    MEMBERSCOUNTLIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMBERCCOUNTUPGRADECOST_FIELD_NUMBER: _ClassVar[int]
    CHANGECLANNAMEORTAGCOST_FIELD_NUMBER: _ClassVar[int]
    CLANCREATECOST_FIELD_NUMBER: _ClassVar[int]
    initialMembersCount: int
    membersCountLimit: int
    membercCountUpgradeCost: CurrencyAmount
    changeClanNameOrTagCost: CurrencyAmount
    clanCreateCost: CurrencyAmount
    def __init__(self, initialMembersCount: _Optional[int] = ..., membersCountLimit: _Optional[int] = ..., membercCountUpgradeCost: _Optional[_Union[CurrencyAmount, _Mapping]] = ..., changeClanNameOrTagCost: _Optional[_Union[CurrencyAmount, _Mapping]] = ..., clanCreateCost: _Optional[_Union[CurrencyAmount, _Mapping]] = ...) -> None: ...

class AuthBoltId(_message.Message):
    __slots__ = ("gameId", "gameVersion", "platform", "token", "locale", "store")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    platform: Platform
    token: str
    locale: str
    store: Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., token: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[Store, str]] = ...) -> None: ...

class ChatUser(_message.Message):
    __slots__ = ("player", "group", "message", "timestamp", "unreadMsgsCount")
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNREADMSGSCOUNT_FIELD_NUMBER: _ClassVar[int]
    player: PlayerFriend
    group: Group
    message: str
    timestamp: int
    unreadMsgsCount: int
    def __init__(self, player: _Optional[_Union[PlayerFriend, _Mapping]] = ..., group: _Optional[_Union[Group, _Mapping]] = ..., message: _Optional[str] = ..., timestamp: _Optional[int] = ..., unreadMsgsCount: _Optional[int] = ...) -> None: ...

class Storage(_message.Message):
    __slots__ = ("filename", "file", "gpid", "token")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    file: bytes
    gpid: str
    token: str
    def __init__(self, filename: _Optional[str] = ..., file: _Optional[bytes] = ..., gpid: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class GameAnnouncement(_message.Message):
    __slots__ = ("id", "title", "body", "resourceUrl", "date", "links", "tags", "pinned", "properties", "code", "untilDate")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    RESOURCEURL_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    UNTILDATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    body: str
    resourceUrl: str
    date: int
    links: _containers.RepeatedCompositeFieldContainer[ExternalLink]
    tags: _containers.RepeatedScalarFieldContainer[str]
    pinned: bool
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    code: str
    untilDate: int
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., resourceUrl: _Optional[str] = ..., date: _Optional[int] = ..., links: _Optional[_Iterable[_Union[ExternalLink, _Mapping]]] = ..., tags: _Optional[_Iterable[str]] = ..., pinned: bool = ..., properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ..., code: _Optional[str] = ..., untilDate: _Optional[int] = ...) -> None: ...

class Creator(_message.Message):
    __slots__ = ("code", "nickName", "until")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    code: str
    nickName: str
    until: int
    def __init__(self, code: _Optional[str] = ..., nickName: _Optional[str] = ..., until: _Optional[int] = ...) -> None: ...

class InventoryItemPropertyDefinitions(_message.Message):
    __slots__ = ("itemDefinitionId", "definitions")
    class DefinitionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InventoryItemPropertyDefinition
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[InventoryItemPropertyDefinition, _Mapping]] = ...) -> None: ...
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    definitions: _containers.MessageMap[str, InventoryItemPropertyDefinition]
    def __init__(self, itemDefinitionId: _Optional[int] = ..., definitions: _Optional[_Mapping[str, InventoryItemPropertyDefinition]] = ...) -> None: ...

class GameSetting(_message.Message):
    __slots__ = ("key", "value", "intValue", "floatValue", "boolValue", "type", "longValue")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    intValue: int
    floatValue: float
    boolValue: bool
    type: SettingType
    longValue: int
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., boolValue: bool = ..., type: _Optional[_Union[SettingType, str]] = ..., longValue: _Optional[int] = ...) -> None: ...

class AuthHuawei(_message.Message):
    __slots__ = ("gameId", "gameVersion", "platform", "idToken", "locale", "store")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    IDTOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    platform: Platform
    idToken: str
    locale: str
    store: Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., idToken: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[Store, str]] = ...) -> None: ...

class DBAFACADFEBGFED(_message.Message):
    __slots__ = ("EFBFADAAEGEDGDE", "GDDFHAECBGFDBEB", "GACEFFAGBAAAHCA", "ACFGFHBDBDDECDC", "GFDFFBHBEDFDCFA")
    EFBFADAAEGEDGDE_FIELD_NUMBER: _ClassVar[int]
    GDDFHAECBGFDBEB_FIELD_NUMBER: _ClassVar[int]
    GACEFFAGBAAAHCA_FIELD_NUMBER: _ClassVar[int]
    ACFGFHBDBDDECDC_FIELD_NUMBER: _ClassVar[int]
    GFDFFBHBEDFDCFA_FIELD_NUMBER: _ClassVar[int]
    EFBFADAAEGEDGDE: str
    GDDFHAECBGFDBEB: str
    GACEFFAGBAAAHCA: bool
    ACFGFHBDBDDECDC: bool
    GFDFFBHBEDFDCFA: str
    def __init__(self, EFBFADAAEGEDGDE: _Optional[str] = ..., GDDFHAECBGFDBEB: _Optional[str] = ..., GACEFFAGBAAAHCA: bool = ..., ACFGFHBDBDDECDC: bool = ..., GFDFFBHBEDFDCFA: _Optional[str] = ...) -> None: ...

class Money(_message.Message):
    __slots__ = ("currencyCode", "units", "nanos")
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    currencyCode: str
    units: int
    nanos: int
    def __init__(self, currencyCode: _Optional[str] = ..., units: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class ProductInfo(_message.Message):
    __slots__ = ("productId", "price", "country")
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    productId: str
    price: Money
    country: str
    def __init__(self, productId: _Optional[str] = ..., price: _Optional[_Union[Money, _Mapping]] = ..., country: _Optional[str] = ...) -> None: ...

class FinishedMatch(_message.Message):
    __slots__ = ("matchId", "matchType", "creatorGpid", "region", "version", "startDate", "finishDate", "seasonId", "state", "properties", "players", "clans")
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    MATCHTYPE_FIELD_NUMBER: _ClassVar[int]
    CREATORGPID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STARTDATE_FIELD_NUMBER: _ClassVar[int]
    FINISHDATE_FIELD_NUMBER: _ClassVar[int]
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    CLANS_FIELD_NUMBER: _ClassVar[int]
    matchId: str
    matchType: MatchType
    creatorGpid: str
    region: str
    version: str
    startDate: int
    finishDate: int
    seasonId: str
    state: MatchState
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    players: _containers.RepeatedCompositeFieldContainer[MatchPlayer]
    clans: _containers.RepeatedCompositeFieldContainer[MatchClan]
    def __init__(self, matchId: _Optional[str] = ..., matchType: _Optional[_Union[MatchType, str]] = ..., creatorGpid: _Optional[str] = ..., region: _Optional[str] = ..., version: _Optional[str] = ..., startDate: _Optional[int] = ..., finishDate: _Optional[int] = ..., seasonId: _Optional[str] = ..., state: _Optional[_Union[MatchState, str]] = ..., properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ..., players: _Optional[_Iterable[_Union[MatchPlayer, _Mapping]]] = ..., clans: _Optional[_Iterable[_Union[MatchClan, _Mapping]]] = ...) -> None: ...

class ClosedRequest(_message.Message):
    __slots__ = ("id", "originId", "creator", "itemDefinitionId", "price", "createDate", "closeDate", "type", "partner", "partnerRequestId", "reason", "quantity", "modifications")
    class ModificationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    CLOSEDATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTNER_FIELD_NUMBER: _ClassVar[int]
    PARTNERREQUESTID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    originId: str
    creator: Player
    itemDefinitionId: int
    price: float
    createDate: int
    closeDate: int
    type: MarketRequestType
    partner: Player
    partnerRequestId: str
    reason: ClosingReason
    quantity: int
    modifications: _containers.MessageMap[str, ItemModificationValue]
    def __init__(self, id: _Optional[str] = ..., originId: _Optional[str] = ..., creator: _Optional[_Union[Player, _Mapping]] = ..., itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., createDate: _Optional[int] = ..., closeDate: _Optional[int] = ..., type: _Optional[_Union[MarketRequestType, str]] = ..., partner: _Optional[_Union[Player, _Mapping]] = ..., partnerRequestId: _Optional[str] = ..., reason: _Optional[_Union[ClosingReason, str]] = ..., quantity: _Optional[int] = ..., modifications: _Optional[_Mapping[str, ItemModificationValue]] = ...) -> None: ...

class AuthGoogle(_message.Message):
    __slots__ = ("gameId", "gameVersion", "platform", "authCode", "locale", "store")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    AUTHCODE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    platform: Platform
    authCode: str
    locale: str
    store: Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., authCode: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[Store, str]] = ...) -> None: ...

class ClanInviteRequest(_message.Message):
    __slots__ = ("id", "clan", "requestSender", "createDate", "closeDate", "requestType", "invitedPlayer")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    REQUESTSENDER_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    CLOSEDATE_FIELD_NUMBER: _ClassVar[int]
    REQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    INVITEDPLAYER_FIELD_NUMBER: _ClassVar[int]
    id: str
    clan: Clan
    requestSender: Player
    createDate: int
    closeDate: int
    requestType: RequestType
    invitedPlayer: Player
    def __init__(self, id: _Optional[str] = ..., clan: _Optional[_Union[Clan, _Mapping]] = ..., requestSender: _Optional[_Union[Player, _Mapping]] = ..., createDate: _Optional[int] = ..., closeDate: _Optional[int] = ..., requestType: _Optional[_Union[RequestType, str]] = ..., invitedPlayer: _Optional[_Union[Player, _Mapping]] = ...) -> None: ...

class LinkedAuth(_message.Message):
    __slots__ = ("authType", "primary")
    AUTHTYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    authType: AuthType
    primary: bool
    def __init__(self, authType: _Optional[_Union[AuthType, str]] = ..., primary: bool = ...) -> None: ...

class GameEventProgress(_message.Message):
    __slots__ = ("id", "points", "gamePassProgresses", "challengeProgresses", "currentDay")
    ID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    GAMEPASSPROGRESSES_FIELD_NUMBER: _ClassVar[int]
    CHALLENGEPROGRESSES_FIELD_NUMBER: _ClassVar[int]
    CURRENTDAY_FIELD_NUMBER: _ClassVar[int]
    id: str
    points: int
    gamePassProgresses: _containers.RepeatedCompositeFieldContainer[GamePassProgress]
    challengeProgresses: _containers.RepeatedCompositeFieldContainer[ChallengeProgress]
    currentDay: int
    def __init__(self, id: _Optional[str] = ..., points: _Optional[int] = ..., gamePassProgresses: _Optional[_Iterable[_Union[GamePassProgress, _Mapping]]] = ..., challengeProgresses: _Optional[_Iterable[_Union[ChallengeProgress, _Mapping]]] = ..., currentDay: _Optional[int] = ...) -> None: ...

class ClanStatsMap(_message.Message):
    __slots__ = ("stats",)
    class StatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ClanStat
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ClanStat, _Mapping]] = ...) -> None: ...
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.MessageMap[str, ClanStat]
    def __init__(self, stats: _Optional[_Mapping[str, ClanStat]] = ...) -> None: ...

class TradeFilters(_message.Message):
    __slots__ = ("filters",)
    class FiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OperationValuePair
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OperationValuePair, _Mapping]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.MessageMap[str, OperationValuePair]
    def __init__(self, filters: _Optional[_Mapping[str, OperationValuePair]] = ...) -> None: ...

class HGBAGDBBFADCDGA(_message.Message):
    __slots__ = ("GBBHBHFEGFDBFDC",)
    GBBHBHFEGFDBFDC_FIELD_NUMBER: _ClassVar[int]
    GBBHBHFEGFDBFDC: _containers.RepeatedCompositeFieldContainer[DBAFACADFEBGFED]
    def __init__(self, GBBHBHFEGFDBFDC: _Optional[_Iterable[_Union[DBAFACADFEBGFED, _Mapping]]] = ...) -> None: ...

class AuthAppleId(_message.Message):
    __slots__ = ("gameId", "gameVersion", "platform", "identityToken", "defaultName", "locale", "store")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    IDENTITYTOKEN_FIELD_NUMBER: _ClassVar[int]
    DEFAULTNAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    platform: Platform
    identityToken: str
    defaultName: str
    locale: str
    store: Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., identityToken: _Optional[str] = ..., defaultName: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[Store, str]] = ...) -> None: ...

class AuthGameCenter(_message.Message):
    __slots__ = ("gameId", "gameVersion", "platform", "gpid", "bundleId", "publicKeyUrl", "signature", "salt", "timestamp", "defaultName", "locale", "store")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    BUNDLEID_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEYURL_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DEFAULTNAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    gameId: str
    gameVersion: str
    platform: Platform
    gpid: str
    bundleId: str
    publicKeyUrl: str
    signature: bytes
    salt: bytes
    timestamp: int
    defaultName: str
    locale: str
    store: Store
    def __init__(self, gameId: _Optional[str] = ..., gameVersion: _Optional[str] = ..., platform: _Optional[_Union[Platform, str]] = ..., gpid: _Optional[str] = ..., bundleId: _Optional[str] = ..., publicKeyUrl: _Optional[str] = ..., signature: _Optional[bytes] = ..., salt: _Optional[bytes] = ..., timestamp: _Optional[int] = ..., defaultName: _Optional[str] = ..., locale: _Optional[str] = ..., store: _Optional[_Union[Store, str]] = ...) -> None: ...

class Attributes(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Attribute
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Attribute, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, Attribute]
    def __init__(self, map: _Optional[_Mapping[str, Attribute]] = ...) -> None: ...

class Dlc(_message.Message):
    __slots__ = ("key", "name", "properties", "files")
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    key: str
    name: str
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    files: _containers.RepeatedCompositeFieldContainer[DlcFile]
    def __init__(self, key: _Optional[str] = ..., name: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ..., files: _Optional[_Iterable[_Union[DlcFile, _Mapping]]] = ...) -> None: ...

class ItemModifications(_message.Message):
    __slots__ = ("id", "modifications")
    class ModificationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    modifications: _containers.MessageMap[str, ItemModificationValue]
    def __init__(self, id: _Optional[int] = ..., modifications: _Optional[_Mapping[str, ItemModificationValue]] = ...) -> None: ...

class ProcessingRequest(_message.Message):
    __slots__ = ("id", "itemDefinitionId", "price", "createDate", "type", "saleRequestId", "state", "quantity", "modifications")
    class ModificationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SALEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    itemDefinitionId: int
    price: float
    createDate: int
    type: MarketRequestType
    saleRequestId: str
    state: ProcessingState
    quantity: int
    modifications: _containers.MessageMap[str, ItemModificationValue]
    def __init__(self, id: _Optional[str] = ..., itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., createDate: _Optional[int] = ..., type: _Optional[_Union[MarketRequestType, str]] = ..., saleRequestId: _Optional[str] = ..., state: _Optional[_Union[ProcessingState, str]] = ..., quantity: _Optional[int] = ..., modifications: _Optional[_Mapping[str, ItemModificationValue]] = ...) -> None: ...

class ContinuationToken(_message.Message):
    __slots__ = ("length", "token")
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    length: int
    token: str
    def __init__(self, length: _Optional[int] = ..., token: _Optional[str] = ...) -> None: ...

class GameServer(_message.Message):
    __slots__ = ("id", "ip", "port")
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ip: str
    port: int
    def __init__(self, id: _Optional[str] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ClanMemberRole(_message.Message):
    __slots__ = ("id", "name", "level", "descripption", "permissions")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    level: int
    descripption: str
    permissions: _containers.RepeatedScalarFieldContainer[ClanMemberRolePermission]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., level: _Optional[int] = ..., descripption: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[ClanMemberRolePermission, str]]] = ...) -> None: ...

class DefaultAvatar(_message.Message):
    __slots__ = ("avatarId",)
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    def __init__(self, avatarId: _Optional[str] = ...) -> None: ...

class StorePlayerStat(_message.Message):
    __slots__ = ("name", "storeInt", "storeFloat", "storeLong")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STOREINT_FIELD_NUMBER: _ClassVar[int]
    STOREFLOAT_FIELD_NUMBER: _ClassVar[int]
    STORELONG_FIELD_NUMBER: _ClassVar[int]
    name: str
    storeInt: int
    storeFloat: float
    storeLong: int
    def __init__(self, name: _Optional[str] = ..., storeInt: _Optional[int] = ..., storeFloat: _Optional[float] = ..., storeLong: _Optional[int] = ...) -> None: ...

class InventoryItemAmount(_message.Message):
    __slots__ = ("inventoryItemDefinitionId", "value")
    INVENTORYITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    inventoryItemDefinitionId: int
    value: int
    def __init__(self, inventoryItemDefinitionId: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class RecipeInfo(_message.Message):
    __slots__ = ("recipe", "entities")
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    recipe: str
    entities: _containers.RepeatedCompositeFieldContainer[ExchangeEntity]
    def __init__(self, recipe: _Optional[str] = ..., entities: _Optional[_Iterable[_Union[ExchangeEntity, _Mapping]]] = ...) -> None: ...

class PlayInGame(_message.Message):
    __slots__ = ("gameCode", "gameVersion", "lobbyId", "photonGame", "lobbyName")
    GAMECODE_FIELD_NUMBER: _ClassVar[int]
    GAMEVERSION_FIELD_NUMBER: _ClassVar[int]
    LOBBYID_FIELD_NUMBER: _ClassVar[int]
    PHOTONGAME_FIELD_NUMBER: _ClassVar[int]
    LOBBYNAME_FIELD_NUMBER: _ClassVar[int]
    gameCode: str
    gameVersion: str
    lobbyId: str
    photonGame: PhotonGame
    lobbyName: str
    def __init__(self, gameCode: _Optional[str] = ..., gameVersion: _Optional[str] = ..., lobbyId: _Optional[str] = ..., photonGame: _Optional[_Union[PhotonGame, _Mapping]] = ..., lobbyName: _Optional[str] = ...) -> None: ...

class ClanStat(_message.Message):
    __slots__ = ("type", "intValue", "floatValue", "longValue", "statId")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    STATID_FIELD_NUMBER: _ClassVar[int]
    type: StatDefType
    intValue: int
    floatValue: float
    longValue: int
    statId: str
    def __init__(self, type: _Optional[_Union[StatDefType, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., longValue: _Optional[int] = ..., statId: _Optional[str] = ...) -> None: ...

class ClanMemberStat(_message.Message):
    __slots__ = ("statId", "type", "intValue", "floatValue", "longValue")
    STATID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    statId: str
    type: StatDefType
    intValue: int
    floatValue: float
    longValue: int
    def __init__(self, statId: _Optional[str] = ..., type: _Optional[_Union[StatDefType, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., longValue: _Optional[int] = ...) -> None: ...

class ItemModificationValue(_message.Message):
    __slots__ = ("type", "intValue", "floatValue", "stringValue", "booleanValue")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLEANVALUE_FIELD_NUMBER: _ClassVar[int]
    type: PropertyType
    intValue: int
    floatValue: float
    stringValue: str
    booleanValue: bool
    def __init__(self, type: _Optional[_Union[PropertyType, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., stringValue: _Optional[str] = ..., booleanValue: bool = ...) -> None: ...

class BlockedAction(_message.Message):
    __slots__ = ("blockMarketplace", "blockMarketplaceUntil")
    BLOCKMARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    BLOCKMARKETPLACEUNTIL_FIELD_NUMBER: _ClassVar[int]
    blockMarketplace: bool
    blockMarketplaceUntil: int
    def __init__(self, blockMarketplace: bool = ..., blockMarketplaceUntil: _Optional[int] = ...) -> None: ...

class HGGCCFDEHCGDEAD(_message.Message):
    __slots__ = ("AAGADDEGFDDEABE",)
    AAGADDEGFDDEABE_FIELD_NUMBER: _ClassVar[int]
    AAGADDEGFDDEABE: _containers.RepeatedCompositeFieldContainer[HGBAGDBBFADCDGA]
    def __init__(self, AAGADDEGFDDEABE: _Optional[_Iterable[_Union[HGBAGDBBFADCDGA, _Mapping]]] = ...) -> None: ...

class StatAmount(_message.Message):
    __slots__ = ("statId", "propertyType", "intValue", "floatValue", "longValue")
    STATID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYTYPE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    statId: str
    propertyType: PropertyType
    intValue: int
    floatValue: float
    longValue: int
    def __init__(self, statId: _Optional[str] = ..., propertyType: _Optional[_Union[PropertyType, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., longValue: _Optional[int] = ...) -> None: ...

class ClanChatMessage(_message.Message):
    __slots__ = ("senderGpid", "message")
    SENDERGPID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    senderGpid: str
    message: str
    def __init__(self, senderGpid: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ClanLogMessage(_message.Message):
    __slots__ = ("clanLogType", "changedClanType", "changedClanName", "changedClanTag", "primaryMember", "secondaryMember", "changedMaxMemberCount", "assignedRole")
    CLANLOGTYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGEDCLANTYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGEDCLANNAME_FIELD_NUMBER: _ClassVar[int]
    CHANGEDCLANTAG_FIELD_NUMBER: _ClassVar[int]
    PRIMARYMEMBER_FIELD_NUMBER: _ClassVar[int]
    SECONDARYMEMBER_FIELD_NUMBER: _ClassVar[int]
    CHANGEDMAXMEMBERCOUNT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEDROLE_FIELD_NUMBER: _ClassVar[int]
    clanLogType: int
    changedClanType: int
    changedClanName: str
    changedClanTag: str
    primaryMember: str
    secondaryMember: str
    changedMaxMemberCount: int
    assignedRole: int
    def __init__(self, clanLogType: _Optional[int] = ..., changedClanType: _Optional[int] = ..., changedClanName: _Optional[str] = ..., changedClanTag: _Optional[str] = ..., primaryMember: _Optional[str] = ..., secondaryMember: _Optional[str] = ..., changedMaxMemberCount: _Optional[int] = ..., assignedRole: _Optional[int] = ...) -> None: ...

class SMAchievementUnlocked(_message.Message):
    __slots__ = ("key", "imageUnlocked", "title")
    KEY_FIELD_NUMBER: _ClassVar[int]
    IMAGEUNLOCKED_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    key: str
    imageUnlocked: str
    title: LocalizedTitle
    def __init__(self, key: _Optional[str] = ..., imageUnlocked: _Optional[str] = ..., title: _Optional[_Union[LocalizedTitle, _Mapping]] = ...) -> None: ...

class SMAvatarRejected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SMClanMembershipAccepted(_message.Message):
    __slots__ = ("tag", "name", "avatarId", "clanAlreadyDeleted")
    TAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    CLANALREADYDELETED_FIELD_NUMBER: _ClassVar[int]
    tag: str
    name: str
    avatarId: str
    clanAlreadyDeleted: bool
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., clanAlreadyDeleted: bool = ...) -> None: ...

class SMClanMembershipEnded(_message.Message):
    __slots__ = ("tag", "name", "avatarId", "clanAlreadyDeleted")
    TAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    CLANALREADYDELETED_FIELD_NUMBER: _ClassVar[int]
    tag: str
    name: str
    avatarId: str
    clanAlreadyDeleted: bool
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., clanAlreadyDeleted: bool = ...) -> None: ...

class SMDevelopersMessageReceived(_message.Message):
    __slots__ = ("message", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
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
    __slots__ = ("playerId", "uid", "name", "avatarId", "playerAlreadyDeleted")
    PLAYERID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    PLAYERALREADYDELETED_FIELD_NUMBER: _ClassVar[int]
    playerId: str
    uid: str
    name: str
    avatarId: str
    playerAlreadyDeleted: bool
    def __init__(self, playerId: _Optional[str] = ..., uid: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., playerAlreadyDeleted: bool = ...) -> None: ...

class SMGiftReceived(_message.Message):
    __slots__ = ("playerInventoryItem", "currencyAmount")
    PLAYERINVENTORYITEM_FIELD_NUMBER: _ClassVar[int]
    CURRENCYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItem: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    currencyAmount: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    def __init__(self, playerInventoryItem: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., currencyAmount: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ...) -> None: ...

class SMMarketplaceTransactionReverted(_message.Message):
    __slots__ = ("requestType", "itemDefinitionId", "modifications", "quantity", "price", "closeDate")
    class ModificationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    REQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CLOSEDATE_FIELD_NUMBER: _ClassVar[int]
    requestType: MarketRequestType
    itemDefinitionId: int
    modifications: _containers.MessageMap[str, ItemModificationValue]
    quantity: int
    price: float
    closeDate: int
    def __init__(self, requestType: _Optional[_Union[MarketRequestType, str]] = ..., itemDefinitionId: _Optional[int] = ..., modifications: _Optional[_Mapping[str, ItemModificationValue]] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., closeDate: _Optional[int] = ...) -> None: ...

class SMMatchesCanceled(_message.Message):
    __slots__ = ("matches",)
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[FinishedMatch]
    def __init__(self, matches: _Optional[_Iterable[_Union[FinishedMatch, _Mapping]]] = ...) -> None: ...

class SMGlobalBanReceived(_message.Message):
    __slots__ = ("code", "message", "until")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    until: int
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ...) -> None: ...

class SMReportedPlayersBanned(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class SMSeasonFinished(_message.Message):
    __slots__ = ("seasonId", "items", "currencies", "playerStats", "clanStats", "clanMemberStats")
    SEASONID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    PLAYERSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANSTATS_FIELD_NUMBER: _ClassVar[int]
    CLANMEMBERSTATS_FIELD_NUMBER: _ClassVar[int]
    seasonId: str
    items: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    currencies: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    playerStats: _containers.RepeatedCompositeFieldContainer[PlayerStat]
    clanStats: _containers.RepeatedCompositeFieldContainer[ClanStat]
    clanMemberStats: _containers.RepeatedCompositeFieldContainer[ClanMemberStat]
    def __init__(self, seasonId: _Optional[str] = ..., items: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., playerStats: _Optional[_Iterable[_Union[PlayerStat, _Mapping]]] = ..., clanStats: _Optional[_Iterable[_Union[ClanStat, _Mapping]]] = ..., clanMemberStats: _Optional[_Iterable[_Union[ClanMemberStat, _Mapping]]] = ...) -> None: ...

class SMMarketplaceBanReceived(_message.Message):
    __slots__ = ("code", "message", "until")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    until: int
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ...) -> None: ...

class SMChatBanReceived(_message.Message):
    __slots__ = ("code", "message", "until")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    until: int
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ...) -> None: ...

class SMMatchesRestored(_message.Message):
    __slots__ = ("matches",)
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[FinishedMatch]
    def __init__(self, matches: _Optional[_Iterable[_Union[FinishedMatch, _Mapping]]] = ...) -> None: ...

class SMInAppSucceed(_message.Message):
    __slots__ = ("productId",)
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    productId: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, productId: _Optional[_Iterable[str]] = ...) -> None: ...

class SMNewDeviceLogined(_message.Message):
    __slots__ = ("deviceModel", "country", "ip")
    DEVICEMODEL_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    deviceModel: str
    country: str
    ip: str
    def __init__(self, deviceModel: _Optional[str] = ..., country: _Optional[str] = ..., ip: _Optional[str] = ...) -> None: ...

class EnvironmentInfo(_message.Message):
    __slots__ = ("version", "environment")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    version: int
    environment: bytes
    def __init__(self, version: _Optional[int] = ..., environment: _Optional[bytes] = ...) -> None: ...

class PlayerBan(_message.Message):
    __slots__ = ("banCode", "message", "until", "banScope")
    BANCODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    BANSCOPE_FIELD_NUMBER: _ClassVar[int]
    banCode: int
    message: str
    until: int
    banScope: BanScope
    def __init__(self, banCode: _Optional[int] = ..., message: _Optional[str] = ..., until: _Optional[int] = ..., banScope: _Optional[_Union[BanScope, str]] = ...) -> None: ...

class InAppOffer(_message.Message):
    __slots__ = ("productId", "reward")
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    productId: str
    reward: RewardInfo
    def __init__(self, productId: _Optional[str] = ..., reward: _Optional[_Union[RewardInfo, _Mapping]] = ...) -> None: ...

class StoreOffer(_message.Message):
    __slots__ = ("itemPackId", "currencyAmounts", "reward")
    ITEMPACKID_FIELD_NUMBER: _ClassVar[int]
    CURRENCYAMOUNTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    itemPackId: str
    currencyAmounts: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    reward: RewardInfo
    def __init__(self, itemPackId: _Optional[str] = ..., currencyAmounts: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ..., reward: _Optional[_Union[RewardInfo, _Mapping]] = ...) -> None: ...

class Property(_message.Message):
    __slots__ = ("name", "type", "valueCase")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUECASE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: PropertyType
    valueCase: Property_ValueOneofCase
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[PropertyType, str]] = ..., valueCase: _Optional[_Union[Property_ValueOneofCase, str]] = ...) -> None: ...

class LocalizedTitle(_message.Message):
    __slots__ = ("name", "description", "resourceUrl")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCEURL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    resourceUrl: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., resourceUrl: _Optional[str] = ...) -> None: ...

class GamePassDefinition(_message.Message):
    __slots__ = ("id", "code", "keyItemDefinitionId", "levels")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    KEYITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    keyItemDefinitionId: int
    levels: _containers.RepeatedCompositeFieldContainer[GamePassLevel]
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., keyItemDefinitionId: _Optional[int] = ..., levels: _Optional[_Iterable[_Union[GamePassLevel, _Mapping]]] = ...) -> None: ...

class ChallengeDefinition(_message.Message):
    __slots__ = ("gameEventChallengeId", "gameEventId", "code", "keyItemDefinitionId", "localizedTitle", "action", "dayRange", "type", "eventPoints", "targetPoints", "reward")
    GAMEEVENTCHALLENGEID_FIELD_NUMBER: _ClassVar[int]
    GAMEEVENTID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    KEYITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    LOCALIZEDTITLE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DAYRANGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENTPOINTS_FIELD_NUMBER: _ClassVar[int]
    TARGETPOINTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    gameEventChallengeId: str
    gameEventId: str
    code: str
    keyItemDefinitionId: int
    localizedTitle: LocalizedTitle
    action: str
    dayRange: DayRange
    type: str
    eventPoints: int
    targetPoints: int
    reward: RewardInfo
    def __init__(self, gameEventChallengeId: _Optional[str] = ..., gameEventId: _Optional[str] = ..., code: _Optional[str] = ..., keyItemDefinitionId: _Optional[int] = ..., localizedTitle: _Optional[_Union[LocalizedTitle, _Mapping]] = ..., action: _Optional[str] = ..., dayRange: _Optional[_Union[DayRange, _Mapping]] = ..., type: _Optional[str] = ..., eventPoints: _Optional[int] = ..., targetPoints: _Optional[int] = ..., reward: _Optional[_Union[RewardInfo, _Mapping]] = ...) -> None: ...

class InventoryItemPropertyDefinition(_message.Message):
    __slots__ = ("name", "propertyType", "saveInTrade", "setByType", "retrievable", "boundExclusive")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTYTYPE_FIELD_NUMBER: _ClassVar[int]
    SAVEINTRADE_FIELD_NUMBER: _ClassVar[int]
    SETBYTYPE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVABLE_FIELD_NUMBER: _ClassVar[int]
    BOUNDEXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    name: str
    propertyType: PropertyType
    saveInTrade: bool
    setByType: PropertySetByType
    retrievable: RetrievableType
    boundExclusive: int
    def __init__(self, name: _Optional[str] = ..., propertyType: _Optional[_Union[PropertyType, str]] = ..., saveInTrade: bool = ..., setByType: _Optional[_Union[PropertySetByType, str]] = ..., retrievable: _Optional[_Union[RetrievableType, str]] = ..., boundExclusive: _Optional[int] = ...) -> None: ...

class Banned(_message.Message):
    __slots__ = ("banned", "untilDate")
    BANNED_FIELD_NUMBER: _ClassVar[int]
    UNTILDATE_FIELD_NUMBER: _ClassVar[int]
    banned: bool
    untilDate: int
    def __init__(self, banned: bool = ..., untilDate: _Optional[int] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("id", "name", "avatarId", "players")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    avatarId: str
    players: _containers.RepeatedCompositeFieldContainer[Player]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., players: _Optional[_Iterable[_Union[Player, _Mapping]]] = ...) -> None: ...

class ExternalLink(_message.Message):
    __slots__ = ("platform", "url")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    platform: ExternalPlatform
    url: str
    def __init__(self, platform: _Optional[_Union[ExternalPlatform, str]] = ..., url: _Optional[str] = ...) -> None: ...

class MatchPlayer(_message.Message):
    __slots__ = ("gpid", "uid", "name", "avatarId", "properties", "reward", "deleted")
    GPID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    uid: str
    name: str
    avatarId: str
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    reward: MatchPlayerReward
    deleted: bool
    def __init__(self, gpid: _Optional[str] = ..., uid: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ..., reward: _Optional[_Union[MatchPlayerReward, _Mapping]] = ..., deleted: bool = ...) -> None: ...

class MatchClan(_message.Message):
    __slots__ = ("clanId", "clanName", "clanTag", "avatarId", "players", "properties", "reward")
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CLANNAME_FIELD_NUMBER: _ClassVar[int]
    CLANTAG_FIELD_NUMBER: _ClassVar[int]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    clanName: str
    clanTag: str
    avatarId: str
    players: _containers.RepeatedCompositeFieldContainer[MatchPlayer]
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    reward: MatchClanReward
    def __init__(self, clanId: _Optional[str] = ..., clanName: _Optional[str] = ..., clanTag: _Optional[str] = ..., avatarId: _Optional[str] = ..., players: _Optional[_Iterable[_Union[MatchPlayer, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ..., reward: _Optional[_Union[MatchClanReward, _Mapping]] = ...) -> None: ...

class GamePassProgress(_message.Message):
    __slots__ = ("id", "currentLevel", "levelsToClaimReward")
    ID_FIELD_NUMBER: _ClassVar[int]
    CURRENTLEVEL_FIELD_NUMBER: _ClassVar[int]
    LEVELSTOCLAIMREWARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    currentLevel: int
    levelsToClaimReward: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[str] = ..., currentLevel: _Optional[int] = ..., levelsToClaimReward: _Optional[_Iterable[int]] = ...) -> None: ...

class ChallengeProgress(_message.Message):
    __slots__ = ("id", "points", "completed", "rewardsObtained")
    ID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    REWARDSOBTAINED_FIELD_NUMBER: _ClassVar[int]
    id: str
    points: int
    completed: bool
    rewardsObtained: bool
    def __init__(self, id: _Optional[str] = ..., points: _Optional[int] = ..., completed: bool = ..., rewardsObtained: bool = ...) -> None: ...

class OperationValuePair(_message.Message):
    __slots__ = ("operation", "valueCase")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALUECASE_FIELD_NUMBER: _ClassVar[int]
    operation: OperationValuePair_Types_Operation
    valueCase: OperationValuePair_ValueOneofCase
    def __init__(self, operation: _Optional[_Union[OperationValuePair_Types_Operation, str]] = ..., valueCase: _Optional[_Union[OperationValuePair_ValueOneofCase, str]] = ...) -> None: ...

class Attribute(_message.Message):
    __slots__ = ("type", "int", "float", "string", "boolean")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    type: PropertyType
    int: int
    float: float
    string: str
    boolean: bool
    def __init__(self, type: _Optional[_Union[PropertyType, str]] = ..., int: _Optional[int] = ..., float: _Optional[float] = ..., string: _Optional[str] = ..., boolean: bool = ...) -> None: ...

class DlcFile(_message.Message):
    __slots__ = ("resourceUrls", "fileSizeInBytes", "signature", "properties", "fileName")
    RESOURCEURLS_FIELD_NUMBER: _ClassVar[int]
    FILESIZEINBYTES_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    resourceUrls: _containers.RepeatedScalarFieldContainer[str]
    fileSizeInBytes: int
    signature: str
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    fileName: str
    def __init__(self, resourceUrls: _Optional[_Iterable[str]] = ..., fileSizeInBytes: _Optional[int] = ..., signature: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ..., fileName: _Optional[str] = ...) -> None: ...

class ExchangeEntity(_message.Message):
    __slots__ = ("items", "currencies")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[InventoryItemAmount]
    currencies: _containers.RepeatedCompositeFieldContainer[CurrencyAmount]
    def __init__(self, items: _Optional[_Iterable[_Union[InventoryItemAmount, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[CurrencyAmount, _Mapping]]] = ...) -> None: ...

class GamePassLevel(_message.Message):
    __slots__ = ("level", "minPoints", "reward", "reoccurringPoints")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MINPOINTS_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    REOCCURRINGPOINTS_FIELD_NUMBER: _ClassVar[int]
    level: int
    minPoints: int
    reward: RewardInfo
    reoccurringPoints: int
    def __init__(self, level: _Optional[int] = ..., minPoints: _Optional[int] = ..., reward: _Optional[_Union[RewardInfo, _Mapping]] = ..., reoccurringPoints: _Optional[int] = ...) -> None: ...

class DayRange(_message.Message):
    __slots__ = ("to",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: int
    def __init__(self, to: _Optional[int] = ..., **kwargs) -> None: ...

class MatchPlayerReward(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[PlayerStat]
    def __init__(self, stats: _Optional[_Iterable[_Union[PlayerStat, _Mapping]]] = ...) -> None: ...

class MatchClanReward(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: ClanStats
    def __init__(self, stats: _Optional[_Union[ClanStats, _Mapping]] = ...) -> None: ...
