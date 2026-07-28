import common_message_pb2 as _common_message_pb2
import groups_message_pb2 as _groups_message_pb2
import friends_message_pb2 as _friends_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatUser(_message.Message):
    __slots__ = ["group", "message", "player", "timestamp", "unreadMsgsCount"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNREADMSGSCOUNT_FIELD_NUMBER: _ClassVar[int]
    group: _groups_message_pb2.Group
    message: str
    player: _friends_message_pb2.PlayerFriend
    timestamp: int
    unreadMsgsCount: int
    def __init__(self, player: _Optional[_Union[_friends_message_pb2.PlayerFriend, _Mapping]] = ..., group: _Optional[_Union[_groups_message_pb2.Group, _Mapping]] = ..., message: _Optional[str] = ..., timestamp: _Optional[int] = ..., unreadMsgsCount: _Optional[int] = ...) -> None: ...

class ChatUserLite(_message.Message):
    __slots__ = ["friendGpid", "groupId", "message", "timestamp", "unreadMsgsCount"]
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

class DeleteFriendMsgsRequest(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class DeleteFriendMsgsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteGroupMsgsRequest(_message.Message):
    __slots__ = ["groupId"]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    groupId: str
    def __init__(self, groupId: _Optional[str] = ...) -> None: ...

class DeleteGroupMsgsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetChatUserRequest(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class GetChatUserResponse(_message.Message):
    __slots__ = ["chatUser"]
    CHATUSER_FIELD_NUMBER: _ClassVar[int]
    chatUser: ChatUser
    def __init__(self, chatUser: _Optional[_Union[ChatUser, _Mapping]] = ...) -> None: ...

class GetChatUsersByOffsetRequest(_message.Message):
    __slots__ = ["offset"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: _common_message_pb2.Offset
    def __init__(self, offset: _Optional[_Union[_common_message_pb2.Offset, _Mapping]] = ...) -> None: ...

class GetChatUsersByOffsetResponse(_message.Message):
    __slots__ = ["chatUsers"]
    CHATUSERS_FIELD_NUMBER: _ClassVar[int]
    chatUsers: _containers.RepeatedCompositeFieldContainer[ChatUser]
    def __init__(self, chatUsers: _Optional[_Iterable[_Union[ChatUser, _Mapping]]] = ...) -> None: ...

class GetChatUsersByPageRequest(_message.Message):
    __slots__ = ["page"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    page: _common_message_pb2.Page
    def __init__(self, page: _Optional[_Union[_common_message_pb2.Page, _Mapping]] = ...) -> None: ...

class GetChatUsersByPageResponse(_message.Message):
    __slots__ = ["chatUsers"]
    CHATUSERS_FIELD_NUMBER: _ClassVar[int]
    chatUsers: _containers.RepeatedCompositeFieldContainer[ChatUser]
    def __init__(self, chatUsers: _Optional[_Iterable[_Union[ChatUser, _Mapping]]] = ...) -> None: ...

class GetChatUsersLiteRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetChatUsersLiteResponse(_message.Message):
    __slots__ = ["chatUsers"]
    CHATUSERS_FIELD_NUMBER: _ClassVar[int]
    chatUsers: _containers.RepeatedCompositeFieldContainer[ChatUserLite]
    def __init__(self, chatUsers: _Optional[_Iterable[_Union[ChatUserLite, _Mapping]]] = ...) -> None: ...

class GetChatUsersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetChatUsersResponse(_message.Message):
    __slots__ = ["chatUsers"]
    CHATUSERS_FIELD_NUMBER: _ClassVar[int]
    chatUsers: _containers.RepeatedCompositeFieldContainer[ChatUser]
    def __init__(self, chatUsers: _Optional[_Iterable[_Union[ChatUser, _Mapping]]] = ...) -> None: ...

class GetFriendMsgsByOffsetRequest(_message.Message):
    __slots__ = ["friendGpid", "offset"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    offset: _common_message_pb2.Offset
    def __init__(self, friendGpid: _Optional[str] = ..., offset: _Optional[_Union[_common_message_pb2.Offset, _Mapping]] = ...) -> None: ...

class GetFriendMsgsByOffsetResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[UserMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[UserMessage, _Mapping]]] = ...) -> None: ...

class GetFriendMsgsByPageRequest(_message.Message):
    __slots__ = ["friendGpid", "page"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    page: _common_message_pb2.Page
    def __init__(self, friendGpid: _Optional[str] = ..., page: _Optional[_Union[_common_message_pb2.Page, _Mapping]] = ...) -> None: ...

class GetFriendMsgsByPageResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[UserMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[UserMessage, _Mapping]]] = ...) -> None: ...

class GetGlobalMsgsResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[UserMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[UserMessage, _Mapping]]] = ...) -> None: ...

class GetGroupMsgsRequest(_message.Message):
    __slots__ = ["groupId", "page", "pageSize"]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    groupId: str
    page: int
    pageSize: int
    def __init__(self, groupId: _Optional[str] = ..., page: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...

class GetGroupMsgsResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[UserMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[UserMessage, _Mapping]]] = ...) -> None: ...

class GetUnreadChatUsersCountRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetUnreadChatUsersCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GlobalChatUserMessage(_message.Message):
    __slots__ = ["message", "senderGpid", "timestamp"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDERGPID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message: str
    senderGpid: str
    timestamp: int
    def __init__(self, message: _Optional[str] = ..., senderGpid: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class OnIncomingGlobalChatMessageEvent(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: GlobalChatUserMessage
    def __init__(self, message: _Optional[_Union[GlobalChatUserMessage, _Mapping]] = ...) -> None: ...

class OnMsgFromFriendEvent(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: UserMessage
    def __init__(self, message: _Optional[_Union[UserMessage, _Mapping]] = ...) -> None: ...

class ReadFriendMsgsRequest(_message.Message):
    __slots__ = ["friendGpid"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    def __init__(self, friendGpid: _Optional[str] = ...) -> None: ...

class ReadFriendMsgsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadGroupMsgsRequest(_message.Message):
    __slots__ = ["groupId"]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    groupId: str
    def __init__(self, groupId: _Optional[str] = ...) -> None: ...

class ReadGroupMsgsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendFriendMsgRequest(_message.Message):
    __slots__ = ["friendGpid", "msg"]
    FRIENDGPID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    friendGpid: str
    msg: str
    def __init__(self, friendGpid: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class SendFriendMsgResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendGlobalChatMessageRequest(_message.Message):
    __slots__ = ["message", "topic"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    message: str
    topic: str
    def __init__(self, topic: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class SendGlobalChatMessageResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendGlobalMsgRequest(_message.Message):
    __slots__ = ["message", "topic"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    message: str
    topic: str
    def __init__(self, topic: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class SendGroupMsgRequest(_message.Message):
    __slots__ = ["groupId", "msg"]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    groupId: str
    msg: str
    def __init__(self, groupId: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class SendGroupMsgResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserMessage(_message.Message):
    __slots__ = ["isRead", "message", "senderGpid", "timestamp"]
    ISREAD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDERGPID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    isRead: bool
    message: str
    senderGpid: str
    timestamp: int
    def __init__(self, senderGpid: _Optional[str] = ..., message: _Optional[str] = ..., timestamp: _Optional[int] = ..., isRead: bool = ...) -> None: ...
