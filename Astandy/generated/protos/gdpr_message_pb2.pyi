from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
DONE: RequestStatus
PENDING: RequestStatus

class CreateRequestEncryptedRequest(_message.Message):
    __slots__ = ["email"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class CreateRequestEncryptedResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteAccountRequest(_message.Message):
    __slots__ = ["email"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class DeleteAccountResponse(_message.Message):
    __slots__ = ["daysLeft", "email"]
    DAYSLEFT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    daysLeft: int
    email: str
    def __init__(self, email: _Optional[str] = ..., daysLeft: _Optional[int] = ...) -> None: ...

class GetRequestsEncryptedRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetRequestsEncryptedResponse(_message.Message):
    __slots__ = ["requests"]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[Request]
    def __init__(self, requests: _Optional[_Iterable[_Union[Request, _Mapping]]] = ...) -> None: ...

class RecoverAccountRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RecoverAccountResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Request(_message.Message):
    __slots__ = ["created", "email", "id", "sent", "status"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    created: int
    email: str
    id: str
    sent: int
    status: RequestStatus
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[RequestStatus, str]] = ..., email: _Optional[str] = ..., created: _Optional[int] = ..., sent: _Optional[int] = ...) -> None: ...

class RequestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
