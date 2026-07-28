from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Currency(_message.Message):
    __slots__ = ["exchangableCurrencies", "exchangeRatio", "id"]
    EXCHANGABLECURRENCIES_FIELD_NUMBER: _ClassVar[int]
    EXCHANGERATIO_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    exchangableCurrencies: _containers.RepeatedScalarFieldContainer[int]
    exchangeRatio: float
    id: int
    def __init__(self, id: _Optional[int] = ..., exchangeRatio: _Optional[float] = ..., exchangableCurrencies: _Optional[_Iterable[int]] = ...) -> None: ...

class CurrencyAmount(_message.Message):
    __slots__ = ["currencyId", "oldValue", "value"]
    CURRENCYID_FIELD_NUMBER: _ClassVar[int]
    OLDVALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    currencyId: int
    oldValue: int
    value: float
    def __init__(self, currencyId: _Optional[int] = ..., oldValue: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
