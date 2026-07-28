from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnalyticsEventRequest(_message.Message):
    __slots__ = ["userEvents"]
    USEREVENTS_FIELD_NUMBER: _ClassVar[int]
    userEvents: _containers.RepeatedCompositeFieldContainer[UserEvent]
    def __init__(self, userEvents: _Optional[_Iterable[_Union[UserEvent, _Mapping]]] = ...) -> None: ...

class AnalyticsEventResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserEvent(_message.Message):
    __slots__ = ["category", "event", "increment", "storeCountry", "value"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    INCREMENT_FIELD_NUMBER: _ClassVar[int]
    STORECOUNTRY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    category: str
    event: str
    increment: bool
    storeCountry: bool
    value: int
    def __init__(self, category: _Optional[str] = ..., event: _Optional[str] = ..., value: _Optional[int] = ..., increment: bool = ..., storeCountry: bool = ...) -> None: ...
