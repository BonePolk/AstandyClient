import common_message_pb2 as _common_message_pb2
import player_message_pb2 as _player_message_pb2
import inventory_message_pb2 as _inventory_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CANCELLED: ClosingReason
CANCELLING: ProcessingState
CREATING: ProcessingState
DESCRIPTOR: _descriptor.FileDescriptor
EXPIRED: ClosingReason
EXPIRING: ProcessingState
INVENTORY_SIZE_EXCEEDED: ClosingReason
MP_NONE_TYPE: MarketRequestType
NONE_REASON: ClosingReason
NOT_ENOUGH_FUNDS: ClosingReason
PURCHASE_REQUEST: MarketRequestType
SALE_REQUEST: MarketRequestType
SALE_REQUEST_NOT_FOUND: ClosingReason
SUCCESS_TRANSACTION: ClosingReason

class CancelRequestArgs(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CancelRequestRequest(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class CancelRequestResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ClosedRequest(_message.Message):
    __slots__ = ["closeDate", "createDate", "creator", "id", "itemDefinitionId", "modifications", "originId", "partner", "partnerRequestId", "price", "quantity", "reason", "type"]
    class ModificationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _inventory_message_pb2.ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_inventory_message_pb2.ItemModificationValue, _Mapping]] = ...) -> None: ...
    CLOSEDATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINID_FIELD_NUMBER: _ClassVar[int]
    PARTNERREQUESTID_FIELD_NUMBER: _ClassVar[int]
    PARTNER_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    closeDate: int
    createDate: int
    creator: _player_message_pb2.Player
    id: str
    itemDefinitionId: int
    modifications: _containers.MessageMap[str, _inventory_message_pb2.ItemModificationValue]
    originId: str
    partner: _player_message_pb2.Player
    partnerRequestId: str
    price: float
    quantity: int
    reason: ClosingReason
    type: MarketRequestType
    def __init__(self, id: _Optional[str] = ..., originId: _Optional[str] = ..., creator: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., createDate: _Optional[int] = ..., closeDate: _Optional[int] = ..., type: _Optional[_Union[MarketRequestType, str]] = ..., partner: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., partnerRequestId: _Optional[str] = ..., reason: _Optional[_Union[ClosingReason, str]] = ..., quantity: _Optional[int] = ..., modifications: _Optional[_Mapping[str, _inventory_message_pb2.ItemModificationValue]] = ...) -> None: ...

class CreateMultipleSalesRequest(_message.Message):
    __slots__ = ["itemDefinitionId", "price", "stacks"]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STACKS_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    price: float
    stacks: _containers.RepeatedCompositeFieldContainer[InventoryStackAmount]
    def __init__(self, stacks: _Optional[_Iterable[_Union[InventoryStackAmount, _Mapping]]] = ..., price: _Optional[float] = ..., itemDefinitionId: _Optional[int] = ...) -> None: ...

class CreateMultipleSalesResponse(_message.Message):
    __slots__ = ["requestIds"]
    REQUESTIDS_FIELD_NUMBER: _ClassVar[int]
    requestIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, requestIds: _Optional[_Iterable[str]] = ...) -> None: ...

class CreatePurchaseBySaleArgs(_message.Message):
    __slots__ = ["saleId"]
    SALEID_FIELD_NUMBER: _ClassVar[int]
    saleId: str
    def __init__(self, saleId: _Optional[str] = ...) -> None: ...

class CreatePurchaseRequestArgs(_message.Message):
    __slots__ = ["itemDefinitionId", "price", "quantity"]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    price: float
    quantity: int
    def __init__(self, itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ...) -> None: ...

class CreatePurchaseRequestBySaleRequest(_message.Message):
    __slots__ = ["saleId"]
    SALEID_FIELD_NUMBER: _ClassVar[int]
    saleId: str
    def __init__(self, saleId: _Optional[str] = ...) -> None: ...

class CreatePurchaseRequestBySaleResponse(_message.Message):
    __slots__ = ["purchaseRequestId"]
    PURCHASEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    purchaseRequestId: str
    def __init__(self, purchaseRequestId: _Optional[str] = ...) -> None: ...

class CreatePurchaseRequestRequest(_message.Message):
    __slots__ = ["itemDefinitionId", "price", "quantity"]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    price: float
    quantity: int
    def __init__(self, itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ...) -> None: ...

class CreatePurchaseRequestResponse(_message.Message):
    __slots__ = ["purchaseRequestId"]
    PURCHASEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    purchaseRequestId: str
    def __init__(self, purchaseRequestId: _Optional[str] = ...) -> None: ...

class CreateSaleRequest(_message.Message):
    __slots__ = ["itemDefinitionId", "itemId", "price"]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    itemId: int
    price: float
    def __init__(self, itemId: _Optional[int] = ..., price: _Optional[float] = ..., itemDefinitionId: _Optional[int] = ...) -> None: ...

class CreateSaleRequestArgs(_message.Message):
    __slots__ = ["itemDefinitionId", "itemId", "price"]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    itemId: int
    price: float
    def __init__(self, itemId: _Optional[int] = ..., price: _Optional[float] = ..., itemDefinitionId: _Optional[int] = ...) -> None: ...

class CreateSaleRequestRequest(_message.Message):
    __slots__ = ["itemId", "price"]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    itemId: int
    price: float
    def __init__(self, itemId: _Optional[int] = ..., price: _Optional[float] = ...) -> None: ...

class CreateSaleRequestResponse(_message.Message):
    __slots__ = ["saleRequestId"]
    SALEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    saleRequestId: str
    def __init__(self, saleRequestId: _Optional[str] = ...) -> None: ...

class CreateSaleResponse(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class GetClosedRequestsArgs(_message.Message):
    __slots__ = ["page", "reason", "size", "type"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    page: int
    reason: ClosingReason
    size: int
    type: MarketRequestType
    def __init__(self, type: _Optional[_Union[MarketRequestType, str]] = ..., reason: _Optional[_Union[ClosingReason, str]] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetClosedRequestsCountArgs(_message.Message):
    __slots__ = ["reason", "type"]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    reason: ClosingReason
    type: MarketRequestType
    def __init__(self, type: _Optional[_Union[MarketRequestType, str]] = ..., reason: _Optional[_Union[ClosingReason, str]] = ...) -> None: ...

class GetMarketplaceSettingsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetMarketplaceSettingsResponse(_message.Message):
    __slots__ = ["marketplaceSettings"]
    MARKETPLACESETTINGS_FIELD_NUMBER: _ClassVar[int]
    marketplaceSettings: MarketplaceSettings
    def __init__(self, marketplaceSettings: _Optional[_Union[MarketplaceSettings, _Mapping]] = ...) -> None: ...

class GetPlayerClosedRequestsCountRequest(_message.Message):
    __slots__ = ["reason", "type"]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    reason: ClosingReason
    type: MarketRequestType
    def __init__(self, type: _Optional[_Union[MarketRequestType, str]] = ..., reason: _Optional[_Union[ClosingReason, str]] = ...) -> None: ...

class GetPlayerClosedRequestsCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetPlayerClosedRequestsRequest(_message.Message):
    __slots__ = ["page", "reason", "size", "type"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    page: int
    reason: ClosingReason
    size: int
    type: MarketRequestType
    def __init__(self, type: _Optional[_Union[MarketRequestType, str]] = ..., reason: _Optional[_Union[ClosingReason, str]] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetPlayerClosedRequestsResponse(_message.Message):
    __slots__ = ["closedRequests"]
    CLOSEDREQUESTS_FIELD_NUMBER: _ClassVar[int]
    closedRequests: _containers.RepeatedCompositeFieldContainer[ClosedRequest]
    def __init__(self, closedRequests: _Optional[_Iterable[_Union[ClosedRequest, _Mapping]]] = ...) -> None: ...

class GetPlayerOpenRequestsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerOpenRequestsResponse(_message.Message):
    __slots__ = ["openRequests"]
    OPENREQUESTS_FIELD_NUMBER: _ClassVar[int]
    openRequests: _containers.RepeatedCompositeFieldContainer[OpenRequest]
    def __init__(self, openRequests: _Optional[_Iterable[_Union[OpenRequest, _Mapping]]] = ...) -> None: ...

class GetPlayerProcessingRequestRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerProcessingRequestResponse(_message.Message):
    __slots__ = ["processingRequests"]
    PROCESSINGREQUESTS_FIELD_NUMBER: _ClassVar[int]
    processingRequests: _containers.RepeatedCompositeFieldContainer[ProcessingRequest]
    def __init__(self, processingRequests: _Optional[_Iterable[_Union[ProcessingRequest, _Mapping]]] = ...) -> None: ...

class GetTradeArgs(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetTradeOpenPurchaseRequestsArgs(_message.Message):
    __slots__ = ["id", "page", "size"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    id: int
    page: int
    size: int
    def __init__(self, id: _Optional[int] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetTradeOpenPurchaseRequestsRequest(_message.Message):
    __slots__ = ["id", "page", "size"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    id: int
    page: int
    size: int
    def __init__(self, id: _Optional[int] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetTradeOpenPurchaseRequestsResponse(_message.Message):
    __slots__ = ["openRequests"]
    OPENREQUESTS_FIELD_NUMBER: _ClassVar[int]
    openRequests: _containers.RepeatedCompositeFieldContainer[OpenRequest]
    def __init__(self, openRequests: _Optional[_Iterable[_Union[OpenRequest, _Mapping]]] = ...) -> None: ...

class GetTradeOpenSaleRequestsArgs(_message.Message):
    __slots__ = ["id", "page", "size"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    id: int
    page: int
    size: int
    def __init__(self, id: _Optional[int] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetTradeOpenSaleRequestsRequest(_message.Message):
    __slots__ = ["id", "page", "size", "tradeFilters"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TRADEFILTERS_FIELD_NUMBER: _ClassVar[int]
    id: int
    page: int
    size: int
    tradeFilters: TradeFilters
    def __init__(self, id: _Optional[int] = ..., page: _Optional[int] = ..., size: _Optional[int] = ..., tradeFilters: _Optional[_Union[TradeFilters, _Mapping]] = ...) -> None: ...

class GetTradeOpenSaleRequestsResponse(_message.Message):
    __slots__ = ["openRequests"]
    OPENREQUESTS_FIELD_NUMBER: _ClassVar[int]
    openRequests: _containers.RepeatedCompositeFieldContainer[OpenRequest]
    def __init__(self, openRequests: _Optional[_Iterable[_Union[OpenRequest, _Mapping]]] = ...) -> None: ...

class GetTradeRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetTradeResponse(_message.Message):
    __slots__ = ["trade"]
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class GetTradesArgs(_message.Message):
    __slots__ = ["itemDefinitionIds"]
    ITEMDEFINITIONIDS_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, itemDefinitionIds: _Optional[_Iterable[int]] = ...) -> None: ...

class GetTradesRequest(_message.Message):
    __slots__ = ["itemDefinitionIds"]
    ITEMDEFINITIONIDS_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, itemDefinitionIds: _Optional[_Iterable[int]] = ...) -> None: ...

class GetTradesResponse(_message.Message):
    __slots__ = ["trades"]
    TRADES_FIELD_NUMBER: _ClassVar[int]
    trades: _containers.RepeatedCompositeFieldContainer[Trade]
    def __init__(self, trades: _Optional[_Iterable[_Union[Trade, _Mapping]]] = ...) -> None: ...

class InventoryStackAmount(_message.Message):
    __slots__ = ["inventoryItemStackId", "value"]
    INVENTORYITEMSTACKID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    inventoryItemStackId: int
    value: int
    def __init__(self, inventoryItemStackId: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class MarketplaceSettings(_message.Message):
    __slots__ = ["banned", "commissionPercent", "currencyId", "enabled", "minCommission"]
    BANNED_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONPERCENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCYID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MINCOMMISSION_FIELD_NUMBER: _ClassVar[int]
    banned: _common_message_pb2.Banned
    commissionPercent: float
    currencyId: int
    enabled: bool
    minCommission: float
    def __init__(self, commissionPercent: _Optional[float] = ..., minCommission: _Optional[float] = ..., currencyId: _Optional[int] = ..., enabled: bool = ..., banned: _Optional[_Union[_common_message_pb2.Banned, _Mapping]] = ...) -> None: ...

class OnPlayerRequestClosedEvent(_message.Message):
    __slots__ = ["item", "request"]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    item: _inventory_message_pb2.PlayerInventoryItem
    request: ClosedRequest
    def __init__(self, request: _Optional[_Union[ClosedRequest, _Mapping]] = ..., item: _Optional[_Union[_inventory_message_pb2.PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class OnPlayerRequestOpenedEvent(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: OpenRequest
    def __init__(self, request: _Optional[_Union[OpenRequest, _Mapping]] = ...) -> None: ...

class OnTradeRequestClosedEvent(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: ClosedRequest
    def __init__(self, request: _Optional[_Union[ClosedRequest, _Mapping]] = ...) -> None: ...

class OnTradeRequestOpenedEvent(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: OpenRequest
    def __init__(self, request: _Optional[_Union[OpenRequest, _Mapping]] = ...) -> None: ...

class OnTradeUpdatedEvent(_message.Message):
    __slots__ = ["trade"]
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class OpenRequest(_message.Message):
    __slots__ = ["createDate", "creator", "id", "isCreator", "itemDefinitionId", "modifications", "price", "quantity", "type"]
    class ModificationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _inventory_message_pb2.ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_inventory_message_pb2.ItemModificationValue, _Mapping]] = ...) -> None: ...
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISCREATOR_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    createDate: int
    creator: _player_message_pb2.Player
    id: str
    isCreator: bool
    itemDefinitionId: int
    modifications: _containers.MessageMap[str, _inventory_message_pb2.ItemModificationValue]
    price: float
    quantity: int
    type: MarketRequestType
    def __init__(self, id: _Optional[str] = ..., creator: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., createDate: _Optional[int] = ..., type: _Optional[_Union[MarketRequestType, str]] = ..., quantity: _Optional[int] = ..., modifications: _Optional[_Mapping[str, _inventory_message_pb2.ItemModificationValue]] = ..., isCreator: bool = ...) -> None: ...

class OperationValuePair(_message.Message):
    __slots__ = ["boolValue", "intValue", "operation"]
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT: OperationValuePair.Operation
    EQUALS: OperationValuePair.Operation
    EXIST: OperationValuePair.Operation
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    boolValue: bool
    intValue: int
    operation: OperationValuePair.Operation
    def __init__(self, operation: _Optional[_Union[OperationValuePair.Operation, str]] = ..., intValue: _Optional[int] = ..., boolValue: bool = ...) -> None: ...

class ProcessingRequest(_message.Message):
    __slots__ = ["createDate", "id", "itemDefinitionId", "modifications", "price", "quantity", "saleRequestId", "state", "type"]
    class ModificationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _inventory_message_pb2.ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_inventory_message_pb2.ItemModificationValue, _Mapping]] = ...) -> None: ...
    CREATEDATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SALEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    createDate: int
    id: str
    itemDefinitionId: int
    modifications: _containers.MessageMap[str, _inventory_message_pb2.ItemModificationValue]
    price: float
    quantity: int
    saleRequestId: str
    state: ProcessingState
    type: MarketRequestType
    def __init__(self, id: _Optional[str] = ..., itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., createDate: _Optional[int] = ..., type: _Optional[_Union[MarketRequestType, str]] = ..., saleRequestId: _Optional[str] = ..., state: _Optional[_Union[ProcessingState, str]] = ..., quantity: _Optional[int] = ..., modifications: _Optional[_Mapping[str, _inventory_message_pb2.ItemModificationValue]] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ["id", "purchasesCount", "purchasesPrice", "salesCount", "salesPrice"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PURCHASESCOUNT_FIELD_NUMBER: _ClassVar[int]
    PURCHASESPRICE_FIELD_NUMBER: _ClassVar[int]
    SALESCOUNT_FIELD_NUMBER: _ClassVar[int]
    SALESPRICE_FIELD_NUMBER: _ClassVar[int]
    id: int
    purchasesCount: int
    purchasesPrice: float
    salesCount: int
    salesPrice: float
    def __init__(self, id: _Optional[int] = ..., salesCount: _Optional[int] = ..., purchasesCount: _Optional[int] = ..., salesPrice: _Optional[float] = ..., purchasesPrice: _Optional[float] = ...) -> None: ...

class TradeFilters(_message.Message):
    __slots__ = ["filters"]
    class FiltersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OperationValuePair
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OperationValuePair, _Mapping]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.MessageMap[str, OperationValuePair]
    def __init__(self, filters: _Optional[_Mapping[str, OperationValuePair]] = ...) -> None: ...

class MarketRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ProcessingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ClosingReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
