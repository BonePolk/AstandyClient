import common_message_pb2 as _common_message_pb2
import currency_message_pb2 as _currency_message_pb2
import inventory_message_pb2 as _inventory_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
INAPP_PURCHASE: OfferType
STORE: OfferType

class AcceptSpecialOfferRequest(_message.Message):
    __slots__ = ["specialOfferTargetingId"]
    SPECIALOFFERTARGETINGID_FIELD_NUMBER: _ClassVar[int]
    specialOfferTargetingId: str
    def __init__(self, specialOfferTargetingId: _Optional[str] = ...) -> None: ...

class AcceptSpecialOfferResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSpecialOffersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSpecialOffersResponse(_message.Message):
    __slots__ = ["specialOffers"]
    SPECIALOFFERS_FIELD_NUMBER: _ClassVar[int]
    specialOffers: _containers.RepeatedCompositeFieldContainer[SpecialOffer]
    def __init__(self, specialOffers: _Optional[_Iterable[_Union[SpecialOffer, _Mapping]]] = ...) -> None: ...

class InAppOffer(_message.Message):
    __slots__ = ["productId", "reward"]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    productId: str
    reward: _inventory_message_pb2.RewardInfo
    def __init__(self, productId: _Optional[str] = ..., reward: _Optional[_Union[_inventory_message_pb2.RewardInfo, _Mapping]] = ...) -> None: ...

class OnOfferChangedEvent(_message.Message):
    __slots__ = ["specialOffer"]
    SPECIALOFFER_FIELD_NUMBER: _ClassVar[int]
    specialOffer: SpecialOffer
    def __init__(self, specialOffer: _Optional[_Union[SpecialOffer, _Mapping]] = ...) -> None: ...

class SpecialOffer(_message.Message):
    __slots__ = ["body", "dateSince", "dateUntil", "globalLimit", "id", "inappOffer", "key", "offersCount", "resourceUrl", "settings", "storeOffer", "title", "type"]
    class SpecialOfferGlobalLimit(_message.Message):
        __slots__ = ["remainder", "total"]
        REMAINDER_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        remainder: int
        total: int
        def __init__(self, total: _Optional[int] = ..., remainder: _Optional[int] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    DATESINCE_FIELD_NUMBER: _ClassVar[int]
    DATEUNTIL_FIELD_NUMBER: _ClassVar[int]
    GLOBALLIMIT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INAPPOFFER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OFFERSCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCEURL_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    STOREOFFER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    body: str
    dateSince: int
    dateUntil: int
    globalLimit: SpecialOffer.SpecialOfferGlobalLimit
    id: str
    inappOffer: InAppOffer
    key: str
    offersCount: int
    resourceUrl: str
    settings: _containers.RepeatedCompositeFieldContainer[_common_message_pb2.Property]
    storeOffer: StoreOffer
    title: str
    type: OfferType
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., resourceUrl: _Optional[str] = ..., type: _Optional[_Union[OfferType, str]] = ..., inappOffer: _Optional[_Union[InAppOffer, _Mapping]] = ..., storeOffer: _Optional[_Union[StoreOffer, _Mapping]] = ..., dateUntil: _Optional[int] = ..., offersCount: _Optional[int] = ..., dateSince: _Optional[int] = ..., settings: _Optional[_Iterable[_Union[_common_message_pb2.Property, _Mapping]]] = ..., key: _Optional[str] = ..., globalLimit: _Optional[_Union[SpecialOffer.SpecialOfferGlobalLimit, _Mapping]] = ...) -> None: ...

class StoreOffer(_message.Message):
    __slots__ = ["currencyAmounts", "itemPackId", "reward"]
    CURRENCYAMOUNTS_FIELD_NUMBER: _ClassVar[int]
    ITEMPACKID_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    currencyAmounts: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    itemPackId: str
    reward: _inventory_message_pb2.RewardInfo
    def __init__(self, itemPackId: _Optional[str] = ..., currencyAmounts: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., reward: _Optional[_Union[_inventory_message_pb2.RewardInfo, _Mapping]] = ...) -> None: ...

class OfferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
