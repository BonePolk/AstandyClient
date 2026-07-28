import player_message_pb2 as _player_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

Blocked: RelationshipStatus
DESCRIPTOR: _descriptor.FileDescriptor
Friend: RelationshipStatus
Ignored: RelationshipStatus
Initiator: RelationshipStatus
None: RelationshipStatus
Read: MessageStatus
Received: MessageStatus
Recipient: RelationshipStatus
Sent: MessageStatus
SentFailed: MessageStatus

class AcceptFriendRequestRequest(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class AcceptFriendRequestResponse(_message.Message):
    __slots__ = ["relationshipStatus"]
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class BlockFriendRequest(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class BlockFriendResponse(_message.Message):
    __slots__ = ["relationshipStatus"]
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class GetPlayerFriendByIdRequest(_message.Message):
    __slots__ = ["gpid"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class GetPlayerFriendByIdResponse(_message.Message):
    __slots__ = ["playerFriend"]
    PLAYERFRIEND_FIELD_NUMBER: _ClassVar[int]
    playerFriend: PlayerFriend
    def __init__(self, playerFriend: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class GetPlayerFriendByUidRequest(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class GetPlayerFriendByUidResponse(_message.Message):
    __slots__ = ["playerFriend"]
    PLAYERFRIEND_FIELD_NUMBER: _ClassVar[int]
    playerFriend: PlayerFriend
    def __init__(self, playerFriend: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class GetPlayerFriendsCountRequest(_message.Message):
    __slots__ = ["relationshipStatuses"]
    RELATIONSHIPSTATUSES_FIELD_NUMBER: _ClassVar[int]
    relationshipStatuses: _containers.RepeatedScalarFieldContainer[RelationshipStatus]
    def __init__(self, relationshipStatuses: _Optional[_Iterable[_Union[RelationshipStatus, str]]] = ...) -> None: ...

class GetPlayerFriendsCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetPlayerFriendsIdsRequest(_message.Message):
    __slots__ = ["relationshipStatuses"]
    RELATIONSHIPSTATUSES_FIELD_NUMBER: _ClassVar[int]
    relationshipStatuses: _containers.RepeatedScalarFieldContainer[RelationshipStatus]
    def __init__(self, relationshipStatuses: _Optional[_Iterable[_Union[RelationshipStatus, str]]] = ...) -> None: ...

class GetPlayerFriendsIdsResponse(_message.Message):
    __slots__ = ["friendGpids"]
    FRIENDGPIDS_FIELD_NUMBER: _ClassVar[int]
    friendGpids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, friendGpids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetPlayerFriendsRequest(_message.Message):
    __slots__ = ["page", "relationshipStatuses", "size"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPSTATUSES_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    relationshipStatuses: _containers.RepeatedScalarFieldContainer[RelationshipStatus]
    size: int
    def __init__(self, relationshipStatuses: _Optional[_Iterable[_Union[RelationshipStatus, str]]] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetPlayerFriendsResponse(_message.Message):
    __slots__ = ["playerFriends"]
    PLAYERFRIENDS_FIELD_NUMBER: _ClassVar[int]
    playerFriends: _containers.RepeatedCompositeFieldContainer[PlayerFriend]
    def __init__(self, playerFriends: _Optional[_Iterable[_Union[PlayerFriend, _Mapping]]] = ...) -> None: ...

class GetPlayersCountRequest(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class GetPlayersCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class IgnoreAllFriendRequestsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IgnoreAllFriendRequestsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IgnoreFriendRequestRequest(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class IgnoreFriendRequestResponse(_message.Message):
    __slots__ = ["relationshipStatus"]
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class OnFriendAddedEvent(_message.Message):
    __slots__ = ["friend"]
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    friend: PlayerFriend
    def __init__(self, friend: _Optional[_Union[PlayerFriend, _Mapping]] = ...) -> None: ...

class OnFriendAvatarChangedEvent(_message.Message):
    __slots__ = ["avatarId", "friendGpid"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ..., avatarId: _Optional[str] = ...) -> None: ...

class OnFriendNameChangedEvent(_message.Message):
    __slots__ = ["friendGpid", "newName"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    NEWNAME_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    newName: str
    def __init__(self, friendGpid: _Optional[str] = ..., newName: _Optional[str] = ...) -> None: ...

class OnFriendRemovedEvent(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class OnNewFriendshipRequestEvent(_message.Message):
    __slots__ = ["friend", "msg"]
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    friend: PlayerFriend
    msg: str
    def __init__(self, friend: _Optional[_Union[PlayerFriend, _Mapping]] = ..., msg: _Optional[str] = ...) -> None: ...

class OnPlayerStatusChangedEvent(_message.Message):
    __slots__ = ["friendGpid", "newStatus"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    NEWSTATUS_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    newStatus: _player_message_pb2.PlayerStatus
    def __init__(self, friendGpid: _Optional[str] = ..., newStatus: _Optional[_Union[_player_message_pb2.PlayerStatus, _Mapping]] = ...) -> None: ...

class OnRevokeFriendshipRequestEvent(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class PlayerFriend(_message.Message):
    __slots__ = ["lastRelationshipUpdate", "msg", "player", "relationshipStatus"]
    LASTRELATIONSHIPUPDATE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    lastRelationshipUpdate: int
    msg: str
    player: _player_message_pb2.Player
    relationshipStatus: RelationshipStatus
    def __init__(self, player: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ..., lastRelationshipUpdate: _Optional[int] = ..., msg: _Optional[str] = ...) -> None: ...

class RemoveFriendRequest(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class RemoveFriendResponse(_message.Message):
    __slots__ = ["relationshipStatus"]
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class RevokeAllFriendRequestsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RevokeAllFriendRequestsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RevokeFriendRequestRequest(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class RevokeFriendRequestResponse(_message.Message):
    __slots__ = ["relationshipStatus"]
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class SearchPlayersRequest(_message.Message):
    __slots__ = ["page", "size", "value"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    page: int
    size: int
    value: str
    def __init__(self, value: _Optional[str] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class SearchPlayersResponse(_message.Message):
    __slots__ = ["playerFriends"]
    PLAYERFRIENDS_FIELD_NUMBER: _ClassVar[int]
    playerFriends: _containers.RepeatedCompositeFieldContainer[PlayerFriend]
    def __init__(self, playerFriends: _Optional[_Iterable[_Union[PlayerFriend, _Mapping]]] = ...) -> None: ...

class SendFriendRequestRequest(_message.Message):
    __slots__ = ["friendGpid", "msg"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    msg: str
    def __init__(self, friendGpid: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class SendFriendRequestResponse(_message.Message):
    __slots__ = ["relationshipStatus"]
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class UnblockFriendRequest(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class UnblockFriendResponse(_message.Message):
    __slots__ = ["relationshipStatus"]
    RELATIONSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    relationshipStatus: RelationshipStatus
    def __init__(self, relationshipStatus: _Optional[_Union[RelationshipStatus, str]] = ...) -> None: ...

class RelationshipStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MessageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
