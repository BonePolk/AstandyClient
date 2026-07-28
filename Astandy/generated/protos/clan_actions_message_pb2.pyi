import clan_message_pb2 as _clan_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignLeaderRoleRequest(_message.Message):
    __slots__ = ["newLeaderMemberId", "roleId"]
    NEWLEADERMEMBERID_FIELD_NUMBER: _ClassVar[int]
    ROLEID_FIELD_NUMBER: _ClassVar[int]
    newLeaderMemberId: str
    roleId: int
    def __init__(self, newLeaderMemberId: _Optional[str] = ..., roleId: _Optional[int] = ...) -> None: ...

class AssignLeaderRoleResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AssignRoleToMemberRequest(_message.Message):
    __slots__ = ["memberId", "roleId"]
    MEMBERID_FIELD_NUMBER: _ClassVar[int]
    ROLEID_FIELD_NUMBER: _ClassVar[int]
    memberId: str
    roleId: int
    def __init__(self, memberId: _Optional[str] = ..., roleId: _Optional[int] = ...) -> None: ...

class AssignRoleToMemberResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CancelInviteRequestRequest(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class CancelInviteRequestResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CancelJoinRequestRequest(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class CancelJoinRequestResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ChangeClanTypeRequest(_message.Message):
    __slots__ = ["clanType"]
    CLANTYPE_FIELD_NUMBER: _ClassVar[int]
    clanType: _clan_message_pb2.ClanType
    def __init__(self, clanType: _Optional[_Union[_clan_message_pb2.ClanType, str]] = ...) -> None: ...

class ChangeClanTypeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateClanRequest(_message.Message):
    __slots__ = ["clanType", "name", "tag"]
    CLANTYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    clanType: _clan_message_pb2.ClanType
    name: str
    tag: str
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[str] = ..., clanType: _Optional[_Union[_clan_message_pb2.ClanType, str]] = ...) -> None: ...

class CreateClanResponse(_message.Message):
    __slots__ = ["clan"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: _clan_message_pb2.Clan
    def __init__(self, clan: _Optional[_Union[_clan_message_pb2.Clan, _Mapping]] = ...) -> None: ...

class DeclineInviteRequestRequest(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class DeclineInviteRequestResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeclineJoinRequestRequest(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class DeclineJoinRequestResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteClosedInviteRequestRequest(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class DeleteClosedInviteRequestResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteClosedJoinRequestRequest(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class DeleteClosedJoinRequestResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FindClanRequest(_message.Message):
    __slots__ = ["filter", "page", "size"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filter: str
    page: int
    size: int
    def __init__(self, filter: _Optional[str] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class FindClanResponse(_message.Message):
    __slots__ = ["clan"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.Clan]
    def __init__(self, clan: _Optional[_Iterable[_Union[_clan_message_pb2.Clan, _Mapping]]] = ...) -> None: ...

class GetClanByIdRequest(_message.Message):
    __slots__ = ["clanId"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    def __init__(self, clanId: _Optional[str] = ...) -> None: ...

class GetClanByIdResponse(_message.Message):
    __slots__ = ["clan"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: _clan_message_pb2.Clan
    def __init__(self, clan: _Optional[_Union[_clan_message_pb2.Clan, _Mapping]] = ...) -> None: ...

class GetClanByTagRequest(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class GetClanByTagResponse(_message.Message):
    __slots__ = ["clan"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: _clan_message_pb2.Clan
    def __init__(self, clan: _Optional[_Union[_clan_message_pb2.Clan, _Mapping]] = ...) -> None: ...

class GetClanClosedInviteRequestsCountRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetClanClosedInviteRequestsCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetClanInviteRequestsRequest(_message.Message):
    __slots__ = ["length", "offset"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    length: int
    offset: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class GetClanInviteRequestsResponse(_message.Message):
    __slots__ = ["clanInviteRequests"]
    CLANINVITEREQUESTS_FIELD_NUMBER: _ClassVar[int]
    clanInviteRequests: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanInviteRequest]
    def __init__(self, clanInviteRequests: _Optional[_Iterable[_Union[_clan_message_pb2.ClanInviteRequest, _Mapping]]] = ...) -> None: ...

class GetClanJoinRequestsCountRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetClanJoinRequestsCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetClanJoinRequestsRequest(_message.Message):
    __slots__ = ["length", "offset"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    length: int
    offset: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class GetClanJoinRequestsResponse(_message.Message):
    __slots__ = ["clanJoinRequests"]
    CLANJOINREQUESTS_FIELD_NUMBER: _ClassVar[int]
    clanJoinRequests: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanJoinRequest]
    def __init__(self, clanJoinRequests: _Optional[_Iterable[_Union[_clan_message_pb2.ClanJoinRequest, _Mapping]]] = ...) -> None: ...

class GetClanMembersByIdRequest(_message.Message):
    __slots__ = ["clanId"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    def __init__(self, clanId: _Optional[str] = ...) -> None: ...

class GetClanMembersByIdResponse(_message.Message):
    __slots__ = ["clanMembers"]
    CLANMEMBERS_FIELD_NUMBER: _ClassVar[int]
    clanMembers: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanMember]
    def __init__(self, clanMembers: _Optional[_Iterable[_Union[_clan_message_pb2.ClanMember, _Mapping]]] = ...) -> None: ...

class GetClanMembersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetClanMembersResponse(_message.Message):
    __slots__ = ["clanMembers"]
    CLANMEMBERS_FIELD_NUMBER: _ClassVar[int]
    clanMembers: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanMember]
    def __init__(self, clanMembers: _Optional[_Iterable[_Union[_clan_message_pb2.ClanMember, _Mapping]]] = ...) -> None: ...

class GetClanRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetClanResponse(_message.Message):
    __slots__ = ["clan"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: _clan_message_pb2.Clan
    def __init__(self, clan: _Optional[_Union[_clan_message_pb2.Clan, _Mapping]] = ...) -> None: ...

class GetClanSettingsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetClanSettingsResponse(_message.Message):
    __slots__ = ["clanSettings"]
    CLANSETTINGS_FIELD_NUMBER: _ClassVar[int]
    clanSettings: _clan_message_pb2.ClanSettings
    def __init__(self, clanSettings: _Optional[_Union[_clan_message_pb2.ClanSettings, _Mapping]] = ...) -> None: ...

class GetPlayerClosedJoinRequestsCountRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerClosedJoinRequestsCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetPlayerInviteRequestsCountRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerInviteRequestsCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetPlayerInviteRequestsRequest(_message.Message):
    __slots__ = ["length", "offset"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    length: int
    offset: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class GetPlayerInviteRequestsResponse(_message.Message):
    __slots__ = ["clanInviteRequests"]
    CLANINVITEREQUESTS_FIELD_NUMBER: _ClassVar[int]
    clanInviteRequests: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanInviteRequest]
    def __init__(self, clanInviteRequests: _Optional[_Iterable[_Union[_clan_message_pb2.ClanInviteRequest, _Mapping]]] = ...) -> None: ...

class GetPlayerJoinRequestsRequest(_message.Message):
    __slots__ = ["length", "offset"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    length: int
    offset: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class GetPlayerJoinRequestsResponse(_message.Message):
    __slots__ = ["clanJoinRequests"]
    CLANJOINREQUESTS_FIELD_NUMBER: _ClassVar[int]
    clanJoinRequests: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanJoinRequest]
    def __init__(self, clanJoinRequests: _Optional[_Iterable[_Union[_clan_message_pb2.ClanJoinRequest, _Mapping]]] = ...) -> None: ...

class GetRecommendedClansRequest(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetRecommendedClansResponse(_message.Message):
    __slots__ = ["clan"]
    CLAN_FIELD_NUMBER: _ClassVar[int]
    clan: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.Clan]
    def __init__(self, clan: _Optional[_Iterable[_Union[_clan_message_pb2.Clan, _Mapping]]] = ...) -> None: ...

class GetRolesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetRolesResponse(_message.Message):
    __slots__ = ["clanMemberRole"]
    CLANMEMBERROLE_FIELD_NUMBER: _ClassVar[int]
    clanMemberRole: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanMemberRole]
    def __init__(self, clanMemberRole: _Optional[_Iterable[_Union[_clan_message_pb2.ClanMemberRole, _Mapping]]] = ...) -> None: ...

class IncreaseMaxMembersCountRequest(_message.Message):
    __slots__ = ["increaseValue"]
    INCREASEVALUE_FIELD_NUMBER: _ClassVar[int]
    increaseValue: int
    def __init__(self, increaseValue: _Optional[int] = ...) -> None: ...

class IncreaseMaxMembersCountResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InviteToClanRequest(_message.Message):
    __slots__ = ["gpid"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class InviteToClanResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class KickMemberRequest(_message.Message):
    __slots__ = ["kickingReason", "memberId"]
    KICKINGREASON_FIELD_NUMBER: _ClassVar[int]
    MEMBERID_FIELD_NUMBER: _ClassVar[int]
    kickingReason: str
    memberId: str
    def __init__(self, memberId: _Optional[str] = ..., kickingReason: _Optional[str] = ...) -> None: ...

class KickMemberResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LeaveClanRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LeaveClanResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RenameClanRequest(_message.Message):
    __slots__ = ["name", "tag"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    tag: str
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RenameClanResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RequestToJoinClanRequest(_message.Message):
    __slots__ = ["clanId"]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    clanId: str
    def __init__(self, clanId: _Optional[str] = ...) -> None: ...

class RequestToJoinClanResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetClanAvatarRequest(_message.Message):
    __slots__ = ["avatar"]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    avatar: bytes
    def __init__(self, avatar: _Optional[bytes] = ...) -> None: ...

class SetClanAvatarResponse(_message.Message):
    __slots__ = ["avatarId"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    def __init__(self, avatarId: _Optional[str] = ...) -> None: ...

class SetClanDescriptionRequest(_message.Message):
    __slots__ = ["description"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class SetClanDescriptionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ValidateClanNameRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ValidateClanNameResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ValidateClanTagRequest(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class ValidateClanTagResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
