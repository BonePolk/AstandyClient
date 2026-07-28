from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Creator(_message.Message):
    __slots__ = ["code", "nickName", "until"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    code: str
    nickName: str
    until: int
    def __init__(self, code: _Optional[str] = ..., nickName: _Optional[str] = ..., until: _Optional[int] = ...) -> None: ...

class FindCreatorRequest(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class FindCreatorResponse(_message.Message):
    __slots__ = ["creator"]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    creator: Creator
    def __init__(self, creator: _Optional[_Union[Creator, _Mapping]] = ...) -> None: ...

class GetSubscribedCreatorRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSubscribedCreatorResponse(_message.Message):
    __slots__ = ["creator"]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    creator: Creator
    def __init__(self, creator: _Optional[_Union[Creator, _Mapping]] = ...) -> None: ...

class SubscribeCreatorRequest(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class SubscribeCreatorResponse(_message.Message):
    __slots__ = ["creator"]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    creator: Creator
    def __init__(self, creator: _Optional[_Union[Creator, _Mapping]] = ...) -> None: ...

class UnsubscribeCreatorRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UnsubscribeCreatorResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
