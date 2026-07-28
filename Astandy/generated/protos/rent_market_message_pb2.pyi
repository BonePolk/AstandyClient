import common_message_pb2 as _common_message_pb2
import player_message_pb2 as _player_message_pb2
import inventory_message_pb2 as _inventory_message_pb2
import marketplace_message_pb2 as _marketplace_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CancelRentRequestRequest(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class CancelRentRequestResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateRentPurchaseRequestBySaleRequest(_message.Message):
    __slots__ = ["saleId"]
    SALEID_FIELD_NUMBER: _ClassVar[int]
    saleId: str
    def __init__(self, saleId: _Optional[str] = ...) -> None: ...

class CreateRentPurchaseRequestBySaleResponse(_message.Message):
    __slots__ = ["purchaseRequestId"]
    PURCHASEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    purchaseRequestId: str
    def __init__(self, purchaseRequestId: _Optional[str] = ...) -> None: ...

class CreateRentPurchaseRequestRequest(_message.Message):
    __slots__ = ["itemDefinitionId", "price"]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    price: float
    def __init__(self, itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ...) -> None: ...

class CreateRentPurchaseRequestResponse(_message.Message):
    __slots__ = ["purchaseRequestId"]
    PURCHASEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    purchaseRequestId: str
    def __init__(self, purchaseRequestId: _Optional[str] = ...) -> None: ...

class CreateRentSaleRequest(_message.Message):
    __slots__ = ["itemDefinitionId", "itemId", "price"]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    itemId: int
    price: float
    def __init__(self, itemId: _Optional[int] = ..., price: _Optional[float] = ..., itemDefinitionId: _Optional[int] = ...) -> None: ...

class CreateRentSaleRequestRequest(_message.Message):
    __slots__ = ["itemId", "price"]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    itemId: int
    price: float
    def __init__(self, itemId: _Optional[int] = ..., price: _Optional[float] = ...) -> None: ...

class CreateRentSaleRequestResponse(_message.Message):
    __slots__ = ["saleRequestId"]
    SALEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    saleRequestId: str
    def __init__(self, saleRequestId: _Optional[str] = ...) -> None: ...

class CreateRentSaleResponse(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: str
    def __init__(self, requestId: _Optional[str] = ...) -> None: ...

class GetPlayerRentClosedRequestsCountRequest(_message.Message):
    __slots__ = ["reason", "type"]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    reason: _marketplace_message_pb2.ClosingReason
    type: _marketplace_message_pb2.MarketRequestType
    def __init__(self, type: _Optional[_Union[_marketplace_message_pb2.MarketRequestType, str]] = ..., reason: _Optional[_Union[_marketplace_message_pb2.ClosingReason, str]] = ...) -> None: ...

class GetPlayerRentClosedRequestsCountResponse(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetPlayerRentClosedRequestsRequest(_message.Message):
    __slots__ = ["page", "reason", "size", "type"]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    page: int
    reason: _marketplace_message_pb2.ClosingReason
    size: int
    type: _marketplace_message_pb2.MarketRequestType
    def __init__(self, type: _Optional[_Union[_marketplace_message_pb2.MarketRequestType, str]] = ..., reason: _Optional[_Union[_marketplace_message_pb2.ClosingReason, str]] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetPlayerRentClosedRequestsResponse(_message.Message):
    __slots__ = ["closedRequests"]
    CLOSEDREQUESTS_FIELD_NUMBER: _ClassVar[int]
    closedRequests: _containers.RepeatedCompositeFieldContainer[RentClosedRequest]
    def __init__(self, closedRequests: _Optional[_Iterable[_Union[RentClosedRequest, _Mapping]]] = ...) -> None: ...

class GetPlayerRentOpenRequestsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerRentOpenRequestsResponse(_message.Message):
    __slots__ = ["openRequests"]
    OPENREQUESTS_FIELD_NUMBER: _ClassVar[int]
    openRequests: _containers.RepeatedCompositeFieldContainer[RentOpenRequest]
    def __init__(self, openRequests: _Optional[_Iterable[_Union[RentOpenRequest, _Mapping]]] = ...) -> None: ...

class GetPlayerRentProcessingRequestsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerRentProcessingRequestsResponse(_message.Message):
    __slots__ = ["processingRequests"]
    PROCESSINGREQUESTS_FIELD_NUMBER: _ClassVar[int]
    processingRequests: _containers.RepeatedCompositeFieldContainer[RentProcessingRequest]
    def __init__(self, processingRequests: _Optional[_Iterable[_Union[RentProcessingRequest, _Mapping]]] = ...) -> None: ...

class GetRentMarketSettingsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetRentMarketSettingsResponse(_message.Message):
    __slots__ = ["marketplaceSettings"]
    MARKETPLACESETTINGS_FIELD_NUMBER: _ClassVar[int]
    marketplaceSettings: RentMarketSettings
    def __init__(self, marketplaceSettings: _Optional[_Union[RentMarketSettings, _Mapping]] = ...) -> None: ...

class GetRentTradeOpenPurchaseRequestsRequest(_message.Message):
    __slots__ = ["id", "page", "size"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    id: int
    page: int
    size: int
    def __init__(self, id: _Optional[int] = ..., page: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class GetRentTradeOpenPurchaseRequestsResponse(_message.Message):
    __slots__ = ["openRequests"]
    OPENREQUESTS_FIELD_NUMBER: _ClassVar[int]
    openRequests: _containers.RepeatedCompositeFieldContainer[RentOpenRequest]
    def __init__(self, openRequests: _Optional[_Iterable[_Union[RentOpenRequest, _Mapping]]] = ...) -> None: ...

class GetRentTradeOpenSaleRequestsRequest(_message.Message):
    __slots__ = ["id", "page", "size", "tradeFilters"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TRADEFILTERS_FIELD_NUMBER: _ClassVar[int]
    id: int
    page: int
    size: int
    tradeFilters: _marketplace_message_pb2.TradeFilters
    def __init__(self, id: _Optional[int] = ..., page: _Optional[int] = ..., size: _Optional[int] = ..., tradeFilters: _Optional[_Union[_marketplace_message_pb2.TradeFilters, _Mapping]] = ...) -> None: ...

class GetRentTradeOpenSaleRequestsResponse(_message.Message):
    __slots__ = ["openRequests"]
    OPENREQUESTS_FIELD_NUMBER: _ClassVar[int]
    openRequests: _containers.RepeatedCompositeFieldContainer[RentOpenRequest]
    def __init__(self, openRequests: _Optional[_Iterable[_Union[RentOpenRequest, _Mapping]]] = ...) -> None: ...

class GetRentTradeRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetRentTradeResponse(_message.Message):
    __slots__ = ["trade"]
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: RentTrade
    def __init__(self, trade: _Optional[_Union[RentTrade, _Mapping]] = ...) -> None: ...

class GetRentTradesRequest(_message.Message):
    __slots__ = ["itemDefinitionIds"]
    ITEMDEFINITIONIDS_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, itemDefinitionIds: _Optional[_Iterable[int]] = ...) -> None: ...

class GetRentTradesResponse(_message.Message):
    __slots__ = ["trades"]
    TRADES_FIELD_NUMBER: _ClassVar[int]
    trades: _containers.RepeatedCompositeFieldContainer[RentTrade]
    def __init__(self, trades: _Optional[_Iterable[_Union[RentTrade, _Mapping]]] = ...) -> None: ...

class OnPlayerRentRequestClosedEvent(_message.Message):
    __slots__ = ["item", "request"]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    item: _inventory_message_pb2.PlayerInventoryItem
    request: RentClosedRequest
    def __init__(self, request: _Optional[_Union[RentClosedRequest, _Mapping]] = ..., item: _Optional[_Union[_inventory_message_pb2.PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class OnPlayerRentRequestOpenedEvent(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: RentOpenRequest
    def __init__(self, request: _Optional[_Union[RentOpenRequest, _Mapping]] = ...) -> None: ...

class OnRentTradeRequestClosedEvent(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: RentClosedRequest
    def __init__(self, request: _Optional[_Union[RentClosedRequest, _Mapping]] = ...) -> None: ...

class OnRentTradeRequestOpenedEvent(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: RentOpenRequest
    def __init__(self, request: _Optional[_Union[RentOpenRequest, _Mapping]] = ...) -> None: ...

class OnRentTradeUpdatedEvent(_message.Message):
    __slots__ = ["trade"]
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: RentTrade
    def __init__(self, trade: _Optional[_Union[RentTrade, _Mapping]] = ...) -> None: ...

class RentClosedRequest(_message.Message):
    __slots__ = ["closeDate", "createDate", "creator", "id", "itemDefinitionId", "modifications", "originId", "partner", "partnerRequestId", "price", "quantity", "reason", "rentEndDate", "type"]
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
    RENTENDDATE_FIELD_NUMBER: _ClassVar[int]
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
    reason: _marketplace_message_pb2.ClosingReason
    rentEndDate: int
    type: _marketplace_message_pb2.MarketRequestType
    def __init__(self, id: _Optional[str] = ..., originId: _Optional[str] = ..., creator: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., createDate: _Optional[int] = ..., closeDate: _Optional[int] = ..., type: _Optional[_Union[_marketplace_message_pb2.MarketRequestType, str]] = ..., partner: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., partnerRequestId: _Optional[str] = ..., reason: _Optional[_Union[_marketplace_message_pb2.ClosingReason, str]] = ..., quantity: _Optional[int] = ..., modifications: _Optional[_Mapping[str, _inventory_message_pb2.ItemModificationValue]] = ..., rentEndDate: _Optional[int] = ...) -> None: ...

class RentMarketSettings(_message.Message):
    __slots__ = ["banned", "commissionPercent", "currencyId", "enabled", "marketCloseDate", "minCommission", "rentDurationDays"]
    BANNED_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONPERCENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCYID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MARKETCLOSEDATE_FIELD_NUMBER: _ClassVar[int]
    MINCOMMISSION_FIELD_NUMBER: _ClassVar[int]
    RENTDURATIONDAYS_FIELD_NUMBER: _ClassVar[int]
    banned: _common_message_pb2.Banned
    commissionPercent: float
    currencyId: int
    enabled: bool
    marketCloseDate: int
    minCommission: float
    rentDurationDays: int
    def __init__(self, commissionPercent: _Optional[float] = ..., minCommission: _Optional[float] = ..., currencyId: _Optional[int] = ..., enabled: bool = ..., banned: _Optional[_Union[_common_message_pb2.Banned, _Mapping]] = ..., rentDurationDays: _Optional[int] = ..., marketCloseDate: _Optional[int] = ...) -> None: ...

class RentOpenRequest(_message.Message):
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
    type: _marketplace_message_pb2.MarketRequestType
    def __init__(self, id: _Optional[str] = ..., creator: _Optional[_Union[_player_message_pb2.Player, _Mapping]] = ..., itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., createDate: _Optional[int] = ..., type: _Optional[_Union[_marketplace_message_pb2.MarketRequestType, str]] = ..., quantity: _Optional[int] = ..., modifications: _Optional[_Mapping[str, _inventory_message_pb2.ItemModificationValue]] = ..., isCreator: bool = ...) -> None: ...

class RentProcessingRequest(_message.Message):
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
    state: _marketplace_message_pb2.ProcessingState
    type: _marketplace_message_pb2.MarketRequestType
    def __init__(self, id: _Optional[str] = ..., itemDefinitionId: _Optional[int] = ..., price: _Optional[float] = ..., createDate: _Optional[int] = ..., type: _Optional[_Union[_marketplace_message_pb2.MarketRequestType, str]] = ..., saleRequestId: _Optional[str] = ..., state: _Optional[_Union[_marketplace_message_pb2.ProcessingState, str]] = ..., quantity: _Optional[int] = ..., modifications: _Optional[_Mapping[str, _inventory_message_pb2.ItemModificationValue]] = ...) -> None: ...

class RentTrade(_message.Message):
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
