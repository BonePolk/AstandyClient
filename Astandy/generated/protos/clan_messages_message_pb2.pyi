import clan_message_pb2 as _clan_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetClanChatMessagesRequest(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ..., **kwargs) -> None: ...

class GetClanChatMessagesResponse(_message.Message):
    __slots__ = ["clanUserMessage"]
    CLANUSERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    clanUserMessage: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanUserMessage]
    def __init__(self, clanUserMessage: _Optional[_Iterable[_Union[_clan_message_pb2.ClanUserMessage, _Mapping]]] = ...) -> None: ...

class GetClanLogMessagesRequest(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ..., **kwargs) -> None: ...

class GetClanLogMessagesResponse(_message.Message):
    __slots__ = ["clanUserMessage"]
    CLANUSERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    clanUserMessage: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanUserMessage]
    def __init__(self, clanUserMessage: _Optional[_Iterable[_Union[_clan_message_pb2.ClanUserMessage, _Mapping]]] = ...) -> None: ...

class GetClanMessagesRequest(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ..., **kwargs) -> None: ...

class GetClanMessagesResponse(_message.Message):
    __slots__ = ["clanUserMessage"]
    CLANUSERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    clanUserMessage: _containers.RepeatedCompositeFieldContainer[_clan_message_pb2.ClanUserMessage]
    def __init__(self, clanUserMessage: _Optional[_Iterable[_Union[_clan_message_pb2.ClanUserMessage, _Mapping]]] = ...) -> None: ...

class GetUnreadChatMessagesCountRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetUnreadChatMessagesCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetUnreadLogMessagesCountRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetUnreadLogMessagesCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class ReadClanChatMessagesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadClanChatMessagesResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadClanLogMessagesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadClanLogMessagesResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendClanChatMessageRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SendClanChatMessageResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
