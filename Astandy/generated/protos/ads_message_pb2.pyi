import currency_message_pb2 as _currency_message_pb2
import inventory_message_pb2 as _inventory_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OnAdRewardEvent(_message.Message):
    __slots__ = ["ignore", "rewardCurrencies", "rewardItems"]
    IGNORE_FIELD_NUMBER: _ClassVar[int]
    REWARDCURRENCIES_FIELD_NUMBER: _ClassVar[int]
    REWARDITEMS_FIELD_NUMBER: _ClassVar[int]
    ignore: bool
    rewardCurrencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    rewardItems: _containers.RepeatedCompositeFieldContainer[_inventory_message_pb2.PlayerInventoryItem]
    def __init__(self, rewardCurrencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., rewardItems: _Optional[_Iterable[_Union[_inventory_message_pb2.PlayerInventoryItem, _Mapping]]] = ..., ignore: bool = ...) -> None: ...

class OnOfferWallRewardedEvent(_message.Message):
    __slots__ = ["rewardCurrencies"]
    REWARDCURRENCIES_FIELD_NUMBER: _ClassVar[int]
    rewardCurrencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    def __init__(self, rewardCurrencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...
