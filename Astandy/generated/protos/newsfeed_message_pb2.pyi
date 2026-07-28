import common_message_pb2 as _common_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalLink(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GameAnnouncement(_message.Message):
    __slots__ = ["body", "code", "date", "id", "links", "pinned", "properties", "resourceUrl", "tags", "title", "untilDate"]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    RESOURCEURL_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNTILDATE_FIELD_NUMBER: _ClassVar[int]
    body: str
    code: str
    date: int
    id: str
    links: _containers.RepeatedCompositeFieldContainer[ExternalLink]
    pinned: bool
    properties: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    resourceUrl: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    title: str
    untilDate: int
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., resourceUrl: _Optional[str] = ..., date: _Optional[int] = ..., links: _Optional[_Iterable[_Union[ExternalLink, _Mapping]]] = ..., tags: _Optional[_Iterable[str]] = ..., pinned: bool = ..., properties: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ..., code: _Optional[str] = ..., untilDate: _Optional[int] = ...) -> None: ...

class GetAllGameAnnouncementsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAllGameAnnouncementsResponse(_message.Message):
    __slots__ = ["announcements"]
    ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    announcements: _containers.RepeatedCompositeFieldContainer[GameAnnouncement]
    def __init__(self, announcements: _Optional[_Iterable[_Union[GameAnnouncement, _Mapping]]] = ...) -> None: ...

class GetItemsRequest(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ..., **kwargs) -> None: ...

class GetItemsResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ["definitionId", "gpid", "id", "itemText", "timestamp"]
    DEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMTEXT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    definitionId: str
    gpid: str
    id: str
    itemText: str
    timestamp: int
    def __init__(self, id: _Optional[str] = ..., definitionId: _Optional[str] = ..., gpid: _Optional[str] = ..., itemText: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class SendNewsRequest(_message.Message):
    __slots__ = ["newsFeedItemDefinitionId"]
    NEWSFEEDITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    newsFeedItemDefinitionId: str
    def __init__(self, newsFeedItemDefinitionId: _Optional[str] = ...) -> None: ...

class SendNewsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
