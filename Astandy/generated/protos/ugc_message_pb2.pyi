from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListFeedbackRequest(_message.Message):
    __slots__ = ["page", "size", "ugcName"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    UGCNAME_FIELD_NUMBER: _ClassVar[int]
    page: int
    size: int
    ugcName: str
    def __init__(self, ugcName: _Optional[str] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListFeedbackResponse(_message.Message):
    __slots__ = ["ugcFeedbacks"]
    UGCFEEDBACKS_FIELD_NUMBER: _ClassVar[int]
    ugcFeedbacks: _containers.RepeatedCompositeFieldContainer[UgcFeedback]
    def __init__(self, ugcFeedbacks: _Optional[_Iterable[_Union[UgcFeedback, _Mapping]]] = ...) -> None: ...

class ListUgcRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListUgcResponse(_message.Message):
    __slots__ = ["ugcs"]
    UGCS_FIELD_NUMBER: _ClassVar[int]
    ugcs: _containers.RepeatedCompositeFieldContainer[Ugc]
    def __init__(self, ugcs: _Optional[_Iterable[_Union[Ugc, _Mapping]]] = ...) -> None: ...

class SaveFeedbackRequest(_message.Message):
    __slots__ = ["feedback", "rating", "ugcName", "version"]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    UGCNAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    feedback: str
    rating: int
    ugcName: str
    version: str
    def __init__(self, ugcName: _Optional[str] = ..., version: _Optional[str] = ..., rating: _Optional[int] = ..., feedback: _Optional[str] = ...) -> None: ...

class SaveFeedbackResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Ugc(_message.Message):
    __slots__ = ["authorGpid", "date", "description", "downloadUrl", "name", "preview", "rating", "tags", "version"]
    AUTHORGPID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    authorGpid: str
    date: int
    description: str
    downloadUrl: str
    name: str
    preview: bytes
    rating: float
    tags: _containers.RepeatedScalarFieldContainer[str]
    version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., downloadUrl: _Optional[str] = ..., date: _Optional[int] = ..., authorGpid: _Optional[str] = ..., preview: _Optional[bytes] = ..., description: _Optional[str] = ..., rating: _Optional[float] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class UgcFeedback(_message.Message):
    __slots__ = ["authorGpid", "date", "feedback", "name", "rating", "version"]
    AUTHORGPID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    authorGpid: str
    date: int
    feedback: str
    name: str
    rating: int
    version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., authorGpid: _Optional[str] = ..., rating: _Optional[int] = ..., feedback: _Optional[str] = ..., date: _Optional[int] = ...) -> None: ...
