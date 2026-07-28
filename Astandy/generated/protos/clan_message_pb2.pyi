import player_message_pb2 as _player_message_pb2
import currency_message_pb2 as _currency_message_pb2
import friends_message_pb2 as _friends_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACCEPT_MEMBER: ClanMemberRolePermission
ASSIGN_ROLE_EQUAL: ClanMemberRolePermission
ASSIGN_ROLE_LESS: ClanMemberRolePermission
BY_ACCEPT_INVITE_REQUEST: JoinClanType
BY_ACCEPT_JOIN_REQUEST: JoinClanType
BY_REQUEST: ClanType
CHANGE_CLAN_SETTINGS: ClanMemberRolePermission
CHAT_MESSAGE: MessageType
CLANS_NONE_TYPE: MessageType
CLOSED: ClanType
CLOSED_REQUEST: RequestType
CREATE_CLAN_BATTLE: ClanMemberRolePermission
DESCRIPTOR: _descriptor.FileDescriptor
INVITE_MEMBER: ClanMemberRolePermission
JOIN_CLAN_BATTLE: ClanMemberRolePermission
JOIN_TO_OPEN_CLAN: JoinClanType
KICK_MEMBER_EQUAL: ClanMemberRolePermission
KICK_MEMBER_LESS: ClanMemberRolePermission
LOG_MESSAGE: MessageType
NONE_JOIN_TYPE: JoinClanType
NONE_TYPE_REQUEST: RequestType
OPENED: ClanType
OPEN_REQUEST: RequestType
UPGRADE_CLAN_MEMBERS_COUNT: ClanMemberRolePermission

class Clan(_message.Message):
    __slots__ = ["avatarId", "clanType", "createDate", "description", "id", "maxMemberCount", "mebersCount", "name", "tag"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    CLANTYPE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAXMEMBERCOUNT_FIELD_NUMBER: _ClassVar[int]
    MEBERSCOUNT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    clanType: ClanType
    createDate: int
    description: str
    id: str
    maxMemberCount: int
    mebersCount: int
    name: str
    tag: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., tag: _Optional[str] = ..., clanType: _Optional[_Union[ClanType, str]] = ..., avatarId: _Optional[str] = ..., createDate: _Optional[int] = ..., mebersCount: _Optional[int] = ..., maxMemberCount: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class ClanChatMessage(_message.Message):
    __slots__ = ["message", "senderGpid"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDERGPID_FIELD_NUMBER: _ClassVar[int]
    message: str
    senderGpid: str
    def __init__(self, senderGpid: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ClanInviteRequest(_message.Message):
    __slots__ = ["clan", "closeDate", "createDate", "id", "invited", "invitedPlayer", "requestSender", "requestType", "sender"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    CLOSEDATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INVITEDPLAYER_FIELD_NUMBER: _ClassVar[int]
    INVITED_FIELD_NUMBER: _ClassVar[int]
    REQUESTSENDER_FIELD_NUMBER: _ClassVar[int]
    REQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    clan: Clan
    closeDate: int
    createDate: int
    id: str
    invited: _friends_message_pb2.PlayerFriend
    invitedPlayer: _player_message_pb2.Player
    requestSender: _player_message_pb2.Player
    requestType: RequestType
    sender: _friends_message_pb2.PlayerFriend
    def __init__(self, id: _Optional[str] = ..., clan: _Optional[_Union[Clan, _Mapping]] = ..., requestSender: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., createDate: _Optional[int] = ..., closeDate: _Optional[int] = ..., requestType: _Optional[_Union[RequestType, str]] = ..., invitedPlayer: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., sender: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ..., invited: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ...) -> None: ...

class ClanJoinRequest(_message.Message):
    __slots__ = ["clan", "closeDate", "createDate", "id", "requestSender", "requestType", "sender"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    CLOSEDATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTSENDER_FIELD_NUMBER: _ClassVar[int]
    REQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    clan: Clan
    closeDate: int
    createDate: int
    id: str
    requestSender: _player_message_pb2.Player
    requestType: RequestType
    sender: _friends_message_pb2.PlayerFriend
    def __init__(self, id: _Optional[str] = ..., clan: _Optional[_Union[Clan, _Mapping]] = ..., requestSender: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., createDate: _Optional[int] = ..., closeDate: _Optional[int] = ..., requestType: _Optional[_Union[RequestType, str]] = ..., sender: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ...) -> None: ...

class ClanLogMessage(_message.Message):
    __slots__ = ["assignedRole", "changedClanName", "changedClanTag", "changedClanType", "changedMaxMemberCount", "clanLogType", "primaryMember", "secondaryMember"]
    ASSIGNEDROLE_FIELD_NUMBER: _ClassVar[int]
    CHANGEDCLANNAME_FIELD_NUMBER: _ClassVar[int]
    CHANGEDCLANTAG_FIELD_NUMBER: _ClassVar[int]
    CHANGEDCLANTYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGEDMAXMEMBERCOUNT_FIELD_NUMBER: _ClassVar[int]
    CLANLOGTYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARYMEMBER_FIELD_NUMBER: _ClassVar[int]
    SECONDARYMEMBER_FIELD_NUMBER: _ClassVar[int]
    assignedRole: int
    changedClanName: str
    changedClanTag: str
    changedClanType: int
    changedMaxMemberCount: int
    clanLogType: int
    primaryMember: str
    secondaryMember: str
    def __init__(self, clanLogType: _Optional[int] = ..., changedClanType: _Optional[int] = ..., changedClanName: _Optional[str] = ..., changedClanTag: _Optional[str] = ..., primaryMember: _Optional[str] = ..., secondaryMember: _Optional[str] = ..., changedMaxMemberCount: _Optional[int] = ..., assignedRole: _Optional[int] = ...) -> None: ...

class ClanMember(_message.Message):
    __slots__ = ["clanId", "createDate", "playerFriend", "roleId"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    PLAYERFRIEND_FIELD_NUMBER: _ClassVar[int]
    ROLEID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    createDate: int
    playerFriend: _friends_message_pb2.PlayerFriend
    roleId: int
    def __init__(self, playerFriend: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ..., clanId: _Optional[str] = ..., roleId: _Optional[int] = ..., createDate: _Optional[int] = ...) -> None: ...

class ClanMemberRole(_message.Message):
    __slots__ = ["descripption", "id", "level", "name", "permissions"]
    DESCRIPPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    descripption: str
    id: int
    level: int
    name: str
    permissions: _containers.RepeatedScalarFieldContainer[ClanMemberRolePermission]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., level: _Optional[int] = ..., descripption: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[ClanMemberRolePermission, str]]] = ...) -> None: ...

class ClanSettings(_message.Message):
    __slots__ = ["changeClanNameOrTagCost", "clanCreateCost", "initialMembersCount", "membercCountUpgradeCost", "membersCountLimit"]
    CHANGECLANNAMEORTAGCOST_FIELD_NUMBER: _ClassVar[int]
    CLANCREATECOST_FIELD_NUMBER: _ClassVar[int]
    INITIALMEMBERSCOUNT_FIELD_NUMBER: _ClassVar[int]
    MEMBERCCOUNTUPGRADECOST_FIELD_NUMBER: _ClassVar[int]
    MEMBERSCOUNTLIMIT_FIELD_NUMBER: _ClassVar[int]
    changeClanNameOrTagCost: _currency_message_pb2.CurrencyAmount
    clanCreateCost: _currency_message_pb2.CurrencyAmount
    initialMembersCount: int
    membercCountUpgradeCost: _currency_message_pb2.CurrencyAmount
    membersCountLimit: int
    def __init__(self, initialMembersCount: _Optional[int] = ..., membersCountLimit: _Optional[int] = ..., membercCountUpgradeCost: _Optional[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]] = ..., changeClanNameOrTagCost: _Optional[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]] = ..., clanCreateCost: _Optional[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]] = ...) -> None: ...

class ClanUserMessage(_message.Message):
    __slots__ = ["chatMessage", "id", "logMessage", "messageType", "timestamp"]
    CHATMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOGMESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGETYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    chatMessage: ClanChatMessage
    id: str
    logMessage: ClanLogMessage
    messageType: MessageType
    timestamp: int
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[int] = ..., messageType: _Optional[_Union[MessageType, str]] = ..., chatMessage: _Optional[_Union[ClanChatMessage, _Mapping]] = ..., logMessage: _Optional[_Union[ClanLogMessage, _Mapping]] = ...) -> None: ...

class OnAssignedLeaderRoleEvent(_message.Message):
    __slots__ = ["newLeaderId", "oldLeaderRole"]
    NEWLEADERID_FIELD_NUMBER: _ClassVar[int]
    OLDLEADERROLE_FIELD_NUMBER: _ClassVar[int]
    newLeaderId: str
    oldLeaderRole: int
    def __init__(self, oldLeaderRole: _Optional[int] = ..., newLeaderId: _Optional[str] = ...) -> None: ...

class OnAssignedRoleEvent(_message.Message):
    __slots__ = ["assignatorMemberId", "assigneeMemberId", "newRoleId"]
    ASSIGNATORMEMBERID_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEEMEMBERID_FIELD_NUMBER: _ClassVar[int]
    NEWROLEID_FIELD_NUMBER: _ClassVar[int]
    assignatorMemberId: str
    assigneeMemberId: str
    newRoleId: int
    def __init__(self, newRoleId: _Optional[int] = ..., assignatorMemberId: _Optional[str] = ..., assigneeMemberId: _Optional[str] = ...) -> None: ...

class OnClanAvatarChangedEvent(_message.Message):
    __slots__ = ["avatar", "avatarId"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    avatar: bytes
    avatarId: str
    def __init__(self, avatarId: _Optional[str] = ..., avatar: _Optional[bytes] = ...) -> None: ...

class OnClanDescriptionChangedEvent(_message.Message):
    __slots__ = ["description"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class OnClanMaxMembersCountIncreased(_message.Message):
    __slots__ = ["newMembersCountValue"]
    NEWMEMBERSCOUNTVALUE_FIELD_NUMBER: _ClassVar[int]
    newMembersCountValue: int
    def __init__(self, newMembersCountValue: _Optional[int] = ...) -> None: ...

class OnClanMemberDeclinedRequestEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OnClanTagAndNameChanged(_message.Message):
    __slots__ = ["newClanName", "newClanTag"]
    NEWCLANNAME_FIELD_NUMBER: _ClassVar[int]
    NEWCLANTAG_FIELD_NUMBER: _ClassVar[int]
    newClanName: str
    newClanTag: str
    def __init__(self, newClanTag: _Optional[str] = ..., newClanName: _Optional[str] = ...) -> None: ...

class OnClanTypeChanged(_message.Message):
    __slots__ = ["newClanType"]
    NEWCLANTYPE_FIELD_NUMBER: _ClassVar[int]
    newClanType: ClanType
    def __init__(self, newClanType: _Optional[_Union[ClanType, str]] = ...) -> None: ...

class OnIncomingClanChatMessageEvent(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: ClanUserMessage
    def __init__(self, message: _Optional[_Union[ClanUserMessage, _Mapping]] = ...) -> None: ...

class OnIncomingClanMessage(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: ClanUserMessage
    def __init__(self, message: _Optional[_Union[ClanUserMessage, _Mapping]] = ...) -> None: ...

class OnInviteRequestAcceptedEvent(_message.Message):
    __slots__ = ["player"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    player: _player_message_pb2.Player
    def __init__(self, player: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ...) -> None: ...

class OnInviteRequestCancelledEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OnInviteRequestDeclinedEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OnInvitedToClanEvent(_message.Message):
    __slots__ = ["clan", "player", "requestId"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    clan: Clan
    player: _player_message_pb2.Player
    requestId: str
    def __init__(self, requestId: _Optional[str] = ..., clan: _Optional[_Union[Clan, _Mapping]] = ..., player: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ...) -> None: ...

class OnJoinRequestCancelledEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OnJoinRequestDeclinedEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OnJoinRequestTakenEvent(_message.Message):
    __slots__ = ["player", "requestId"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    player: _player_message_pb2.Player
    requestId: str
    def __init__(self, requestId: _Optional[str] = ..., player: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ...) -> None: ...

class OnJoinedToClanEvent(_message.Message):
    __slots__ = ["clan"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: Clan
    def __init__(self, clan: _Optional[_Union[Clan, _Mapping]] = ...) -> None: ...

class OnKickedEvent(_message.Message):
    __slots__ = ["kickingReason"]
    KICKINGREASON_FIELD_NUMBER: _ClassVar[int]
    kickingReason: str
    def __init__(self, kickingReason: _Optional[str] = ...) -> None: ...

class OnKickedMemberEvent(_message.Message):
    __slots__ = ["kickedMemberId", "kickerMemberId"]
    KICKEDMEMBERID_FIELD_NUMBER: _ClassVar[int]
    KICKERMEMBERID_FIELD_NUMBER: _ClassVar[int]
    kickedMemberId: str
    kickerMemberId: str
    def __init__(self, kickerMemberId: _Optional[str] = ..., kickedMemberId: _Optional[str] = ...) -> None: ...

class OnLeftFromClan(_message.Message):
    __slots__ = ["memberId"]
    MEMBERID_FIELD_NUMBER: _ClassVar[int]
    memberId: str
    def __init__(self, memberId: _Optional[str] = ...) -> None: ...

class OnMemberJoinedToClanEvent(_message.Message):
    __slots__ = ["clanMember", "joinClanType", "joinRequestAcceptor"]
    CLANMEMBER_FIELD_NUMBER: _ClassVar[int]
    JOINCLANTYPE_FIELD_NUMBER: _ClassVar[int]
    JOINREQUESTACCEPTOR_FIELD_NUMBER: _ClassVar[int]
    clanMember: ClanMember
    joinClanType: JoinClanType
    joinRequestAcceptor: str
    def __init__(self, clanMember: _Optional[_Union[ClanMember, _Mapping]] = ..., joinClanType: _Optional[_Union[JoinClanType, str]] = ..., joinRequestAcceptor: _Optional[str] = ...) -> None: ...

class OnOnlineStatusChangedEvent(_message.Message):
    __slots__ = ["onlineStatus"]
    ONLINESTATUS_FIELD_NUMBER: _ClassVar[int]
    onlineStatus: _player_message_pb2.PlayerStatus
    def __init__(self, onlineStatus: _Optional[_Union[_player_message_pb2.PlayerStatus, _Mapping]] = ...) -> None: ...

class OnPlayerAvatarChangedEvent(_message.Message):
    __slots__ = ["avatarId", "gpid"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    gpid: str
    def __init__(self, gpid: _Optional[str] = ..., avatarId: _Optional[str] = ...) -> None: ...

class OnPlayerNameChangedEvent(_message.Message):
    __slots__ = ["gpid", "name"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    name: str
    def __init__(self, gpid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class OnReadClosedInviteRequestEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ClanType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ClanMemberRolePermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class JoinClanType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
