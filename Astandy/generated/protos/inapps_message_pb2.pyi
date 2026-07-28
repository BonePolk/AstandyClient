import common_message_pb2 as _common_message_pb2
import inventory_message_pb2 as _inventory_message_pb2
import money_message_pb2 as _money_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

Canceled: PurchaseStatus
DESCRIPTOR: _descriptor.FileDescriptor
Pending: PurchaseStatus
Purchased: PurchaseStatus
RefundPending: PurchaseStatus
Refunded: PurchaseStatus
UnknownStatus: PurchaseStatus

class AppGalleryBuyInappRequest(_message.Message):
    __slots__ = ["productId", "purchaseToken"]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    PURCHASETOKEN_FIELD_NUMBER: _ClassVar[int]
    productId: str
    purchaseToken: str
    def __init__(self, productId: _Optional[str] = ..., purchaseToken: _Optional[str] = ...) -> None: ...

class AppGalleryBuyInappResponse(_message.Message):
    __slots__ = ["reward"]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: _inventory_message_pb2.GivenReward
    def __init__(self, reward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ...) -> None: ...

class AppStoreBuyInappRequest(_message.Message):
    __slots__ = ["base64", "price", "productInfos"]
    BASE64_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTINFOS_FIELD_NUMBER: _ClassVar[int]
    base64: str
    price: _money_message_pb2.Money
    productInfos: _containers.RepeatedCompositeFieldContainer[ProductInfo]
    def __init__(self, base64: _Optional[str] = ..., price: _Optional[_Union[_money_message_pb2.Money, _Mapping]] = ..., productInfos: _Optional[_Iterable[_Union[ProductInfo, _Mapping]]] = ...) -> None: ...

class AppStoreBuyInappResponse(_message.Message):
    __slots__ = ["reward"]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: _inventory_message_pb2.PlayerInventory
    def __init__(self, reward: _Optional[_Union[_inventory_message_pb2.PlayerInventory, _Mapping]] = ...) -> None: ...

class GetAppsBuyInappRequest(_message.Message):
    __slots__ = ["price", "productId", "purchaseToken"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    PURCHASETOKEN_FIELD_NUMBER: _ClassVar[int]
    price: _money_message_pb2.Money
    productId: str
    purchaseToken: str
    def __init__(self, productId: _Optional[str] = ..., purchaseToken: _Optional[str] = ..., price: _Optional[_Union[_money_message_pb2.Money, _Mapping]] = ...) -> None: ...

class GetAppsBuyInappResponse(_message.Message):
    __slots__ = ["reward"]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: _inventory_message_pb2.GivenReward
    def __init__(self, reward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ...) -> None: ...

class GetInappsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInappsResponse(_message.Message):
    __slots__ = ["inApps"]
    INAPPS_FIELD_NUMBER: _ClassVar[int]
    inApps: _containers.RepeatedCompositeFieldContainer[InApp]
    def __init__(self, inApps: _Optional[_Iterable[_Union[InApp, _Mapping]]] = ...) -> None: ...

class GetPlayersInAppPurchasesByServerFilters(_message.Message):
    __slots__ = ["minDate"]
    MINDATE_FIELD_NUMBER: _ClassVar[int]
    minDate: int
    def __init__(self, minDate: _Optional[int] = ...) -> None: ...

class GetPlayersInAppPurchasesByServerRequest(_message.Message):
    __slots__ = ["filters", "gpids"]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    GPIDS_FIELD_NUMBER: _ClassVar[int]
    filters: GetPlayersInAppPurchasesByServerFilters
    gpids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, gpids: _Optional[_Iterable[str]] = ..., filters: _Optional[_Union[GetPlayersInAppPurchasesByServerFilters, _Mapping]] = ...) -> None: ...

class GetPlayersInAppPurchasesByServerResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GetPlayersInAppPurchasesByServerResult]
    def __init__(self, results: _Optional[_Iterable[_Union[GetPlayersInAppPurchasesByServerResult, _Mapping]]] = ...) -> None: ...

class GetPlayersInAppPurchasesByServerResult(_message.Message):
    __slots__ = ["gpid", "purchases"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    PURCHASES_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    purchases: _containers.RepeatedCompositeFieldContainer[PlayerInAppPurchaseByServer]
    def __init__(self, gpid: _Optional[str] = ..., purchases: _Optional[_Iterable[_Union[PlayerInAppPurchaseByServer, _Mapping]]] = ...) -> None: ...

class GoogleBuyInappRequest(_message.Message):
    __slots__ = ["json", "signature"]
    JSON_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    json: str
    signature: str
    def __init__(self, json: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class GoogleBuyInappResponse(_message.Message):
    __slots__ = ["reward"]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: _inventory_message_pb2.PlayerInventory
    def __init__(self, reward: _Optional[_Union[_inventory_message_pb2.PlayerInventory, _Mapping]] = ...) -> None: ...

class InApp(_message.Message):
    __slots__ = ["created", "orderId", "products", "purchaseDate", "purchaseStatus", "refundDate", "store"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    PURCHASEDATE_FIELD_NUMBER: _ClassVar[int]
    PURCHASESTATUS_FIELD_NUMBER: _ClassVar[int]
    REFUNDDATE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    created: int
    orderId: str
    products: _containers.RepeatedCompositeFieldContainer[InAppProduct]
    purchaseDate: int
    purchaseStatus: PurchaseStatus
    refundDate: int
    store: _common_message_pb2.Store
    def __init__(self, orderId: _Optional[str] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ..., products: _Optional[_Iterable[_Union[InAppProduct, _Mapping]]] = ..., purchaseStatus: _Optional[_Union[PurchaseStatus, str]] = ..., purchaseDate: _Optional[int] = ..., refundDate: _Optional[int] = ..., created: _Optional[int] = ...) -> None: ...

class InAppProduct(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OctCreateInappPreOrderRequest(_message.Message):
    __slots__ = ["productId"]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    productId: str
    def __init__(self, productId: _Optional[str] = ...) -> None: ...

class OctCreateInappPreOrderResponse(_message.Message):
    __slots__ = ["orderId", "sOrderId"]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    SORDERID_FIELD_NUMBER: _ClassVar[int]
    orderId: str
    sOrderId: str
    def __init__(self, orderId: _Optional[str] = ..., sOrderId: _Optional[str] = ...) -> None: ...

class OnInAppEvent(_message.Message):
    __slots__ = ["reward", "store"]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    reward: _inventory_message_pb2.GivenReward
    store: _common_message_pb2.Store
    def __init__(self, reward: _Optional[_Union[_inventory_message_pb2.GivenReward, _Mapping]] = ..., store: _Optional[_Union[_common_message_pb2.Store, str]] = ...) -> None: ...

class PlayerInAppPurchaseByServer(_message.Message):
    __slots__ = ["price", "purchaseDate", "status"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PURCHASEDATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    price: float
    purchaseDate: int
    status: PurchaseStatus
    def __init__(self, status: _Optional[_Union[PurchaseStatus, str]] = ..., price: _Optional[float] = ..., purchaseDate: _Optional[int] = ...) -> None: ...

class ProductInfo(_message.Message):
    __slots__ = ["country", "price", "productId"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    country: str
    price: _money_message_pb2.Money
    productId: str
    def __init__(self, productId: _Optional[str] = ..., price: _Optional[_Union[_money_message_pb2.Money, _Mapping]] = ..., country: _Optional[str] = ...) -> None: ...

class PurchaseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
