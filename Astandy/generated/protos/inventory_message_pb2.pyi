import common_message_pb2 as _common_message_pb2
import currency_message_pb2 as _currency_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CLIENT: PropertySetByType
DESCRIPTOR: _descriptor.FileDescriptor
GAME_SERVER: PropertySetByType
REMOVABLE: RetrievableType
RETRIEVABLE: RetrievableType
UNREMOVABLE: RetrievableType

class ActivateCouponRequest(_message.Message):
    __slots__ = ["couponId"]
    COUPONID_FIELD_NUMBER: _ClassVar[int]
    couponId: str
    def __init__(self, couponId: _Optional[str] = ...) -> None: ...

class ActivateCouponResponse(_message.Message):
    __slots__ = ["currencies", "inventoryItems"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    inventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., inventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class AddedInventory(_message.Message):
    __slots__ = ["currencies", "items"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    items: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, items: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...

class ApplyInventoryItemRequest(_message.Message):
    __slots__ = ["appliedItemId", "appliedPropertyName", "consumedItemId", "isRemovable"]
    APPLIEDITEMID_FIELD_NUMBER: _ClassVar[int]
    APPLIEDPROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMEDITEMID_FIELD_NUMBER: _ClassVar[int]
    ISREMOVABLE_FIELD_NUMBER: _ClassVar[int]
    appliedItemId: int
    appliedPropertyName: str
    consumedItemId: int
    isRemovable: bool
    def __init__(self, consumedItemId: _Optional[int] = ..., appliedItemId: _Optional[int] = ..., appliedPropertyName: _Optional[str] = ..., isRemovable: bool = ...) -> None: ...

class ApplyInventoryItemResponse(_message.Message):
    __slots__ = ["playerInventoryItem"]
    PLAYERINVENTORYITEM_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItem: PlayerInventoryItem
    def __init__(self, playerInventoryItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class BlockedAction(_message.Message):
    __slots__ = ["blockMarketplace", "blockMarketplaceUntil", "blockedAndExpiresAt", "blockedAndHiddenUntil"]
    BLOCKEDANDEXPIRESAT_FIELD_NUMBER: _ClassVar[int]
    BLOCKEDANDHIDDENUNTIL_FIELD_NUMBER: _ClassVar[int]
    BLOCKMARKETPLACEUNTIL_FIELD_NUMBER: _ClassVar[int]
    BLOCKMARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    blockMarketplace: bool
    blockMarketplaceUntil: int
    blockedAndExpiresAt: int
    blockedAndHiddenUntil: int
    def __init__(self, blockMarketplace: bool = ..., blockMarketplaceUntil: _Optional[int] = ..., blockedAndExpiresAt: _Optional[int] = ..., blockedAndHiddenUntil: _Optional[int] = ...) -> None: ...

class BuyInventoryItemRequest(_message.Message):
    __slots__ = ["currencyId", "itemDefinitionId", "quantity", "toManyItems"]
    CURRENCYID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TOMANYITEMS_FIELD_NUMBER: _ClassVar[int]
    currencyId: int
    itemDefinitionId: int
    quantity: int
    toManyItems: bool
    def __init__(self, itemDefinitionId: _Optional[int] = ..., quantity: _Optional[int] = ..., currencyId: _Optional[int] = ..., toManyItems: bool = ...) -> None: ...

class BuyInventoryItemResponse(_message.Message):
    __slots__ = ["playerInventoryItems"]
    PLAYERINVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, playerInventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class ChangeInventoryRequest(_message.Message):
    __slots__ = ["item_flags", "reset_new_items_quantity"]
    class ResetNewItemsQuantity(_message.Message):
        __slots__ = ["reset_all", "stacks"]
        RESET_ALL_FIELD_NUMBER: _ClassVar[int]
        STACKS_FIELD_NUMBER: _ClassVar[int]
        reset_all: bool
        stacks: ChangeInventoryRequest.Stacks
        def __init__(self, stacks: _Optional[_Union[ChangeInventoryRequest.Stacks, _Mapping]] = ..., reset_all: bool = ...) -> None: ...
    class Stacks(_message.Message):
        __slots__ = ["stack_ids"]
        STACK_IDS_FIELD_NUMBER: _ClassVar[int]
        stack_ids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, stack_ids: _Optional[_Iterable[int]] = ...) -> None: ...
    ITEM_FLAGS_FIELD_NUMBER: _ClassVar[int]
    RESET_NEW_ITEMS_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    item_flags: ItemFlags
    reset_new_items_quantity: ChangeInventoryRequest.ResetNewItemsQuantity
    def __init__(self, item_flags: _Optional[_Union[ItemFlags, _Mapping]] = ..., reset_new_items_quantity: _Optional[_Union[ChangeInventoryRequest.ResetNewItemsQuantity, _Mapping]] = ...) -> None: ...

class ChangeInventoryResponse(_message.Message):
    __slots__ = ["skipped_stacks"]
    class SkippedStacks(_message.Message):
        __slots__ = ["skip_reason", "stack_ids"]
        class SkipReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
        STACK_HIDDEN: ChangeInventoryResponse.SkippedStacks.SkipReason
        STACK_IDS_FIELD_NUMBER: _ClassVar[int]
        STACK_NOT_FOUND: ChangeInventoryResponse.SkippedStacks.SkipReason
        UNSPECIFIED: ChangeInventoryResponse.SkippedStacks.SkipReason
        skip_reason: ChangeInventoryResponse.SkippedStacks.SkipReason
        stack_ids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, stack_ids: _Optional[_Iterable[int]] = ..., skip_reason: _Optional[_Union[ChangeInventoryResponse.SkippedStacks.SkipReason, str]] = ...) -> None: ...
    SKIPPED_STACKS_FIELD_NUMBER: _ClassVar[int]
    skipped_stacks: _containers.RepeatedCompositeFieldContainer[ChangeInventoryResponse.SkippedStacks]
    def __init__(self, skipped_stacks: _Optional[_Iterable[_Union[ChangeInventoryResponse.SkippedStacks, _Mapping]]] = ...) -> None: ...

class ChangePublicityItem(_message.Message):
    __slots__ = ["inventoryItemId", "itemDefinitionId", "public"]
    INVENTORYITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    inventoryItemId: int
    itemDefinitionId: int
    public: bool
    def __init__(self, inventoryItemId: _Optional[int] = ..., itemDefinitionId: _Optional[int] = ..., public: bool = ...) -> None: ...

class ConsumeInventoryItemRequest(_message.Message):
    __slots__ = ["inventoryItemId", "itemDefinitionId", "quantity"]
    INVENTORYITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    inventoryItemId: int
    itemDefinitionId: int
    quantity: int
    def __init__(self, inventoryItemId: _Optional[int] = ..., quantity: _Optional[int] = ..., itemDefinitionId: _Optional[int] = ...) -> None: ...

class ConsumeInventoryItemResponse(_message.Message):
    __slots__ = ["playerInventoryItem"]
    PLAYERINVENTORYITEM_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItem: PlayerInventoryItem
    def __init__(self, playerInventoryItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class ConsumeItemsByServerRequest(_message.Message):
    __slots__ = ["consumptions"]
    CONSUMPTIONS_FIELD_NUMBER: _ClassVar[int]
    consumptions: _containers.RepeatedCompositeFieldContainer[ConsumedItems]
    def __init__(self, consumptions: _Optional[_Iterable[_Union[ConsumedItems, _Mapping]]] = ...) -> None: ...

class ConsumeItemsByServerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ConsumedItems(_message.Message):
    __slots__ = ["gpid", "items"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    items: _containers.RepeatedCompositeFieldContainer[InventoryItemStackAmount]
    def __init__(self, gpid: _Optional[str] = ..., items: _Optional[_Iterable[_Union[InventoryItemStackAmount, _Mapping]]] = ...) -> None: ...

class Coupon(_message.Message):
    __slots__ = ["couponId", "maxActivationsQuantity", "remainingActivationsQuantity", "rewardInfo"]
    COUPONID_FIELD_NUMBER: _ClassVar[int]
    MAXACTIVATIONSQUANTITY_FIELD_NUMBER: _ClassVar[int]
    REMAININGACTIVATIONSQUANTITY_FIELD_NUMBER: _ClassVar[int]
    REWARDINFO_FIELD_NUMBER: _ClassVar[int]
    couponId: str
    maxActivationsQuantity: int
    remainingActivationsQuantity: int
    rewardInfo: RewardInfo
    def __init__(self, couponId: _Optional[str] = ..., maxActivationsQuantity: _Optional[int] = ..., remainingActivationsQuantity: _Optional[int] = ..., rewardInfo: _Optional[_Union[RewardInfo, _Mapping]] = ...) -> None: ...

class ExchangeEntity(_message.Message):
    __slots__ = ["currencies", "items"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    items: _containers.RepeatedCompositeFieldContainer[InventoryItemAmount]
    def __init__(self, items: _Optional[_Iterable[_Union[InventoryItemAmount, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...

class ExchangeRecipeResult(_message.Message):
    __slots__ = ["addedItems", "changedItems", "currencies", "stats"]
    ADDEDITEMS_FIELD_NUMBER: _ClassVar[int]
    CHANGEDITEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    addedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    changedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    stats: _containers.RepeatedCompositeFieldContainer[StatAmount]
    def __init__(self, currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., addedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., changedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., stats: _Optional[_Iterable[_Union[StatAmount, _Mapping]]] = ...) -> None: ...

class ExchangeResult(_message.Message):
    __slots__ = ["currencies", "inventoryItems", "stats"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    inventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    stats: _containers.RepeatedCompositeFieldContainer[StatAmount]
    def __init__(self, currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., inventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., stats: _Optional[_Iterable[_Union[StatAmount, _Mapping]]] = ...) -> None: ...

class ExecuteRecipeByServer(_message.Message):
    __slots__ = ["gpids", "recipeCode"]
    GPIDS_FIELD_NUMBER: _ClassVar[int]
    RECIPECODE_FIELD_NUMBER: _ClassVar[int]
    gpids: _containers.RepeatedScalarFieldContainer[str]
    recipeCode: str
    def __init__(self, recipeCode: _Optional[str] = ..., gpids: _Optional[_Iterable[str]] = ...) -> None: ...

class ExecuteRecipeByServerPlayerResult(_message.Message):
    __slots__ = ["exchangeResult", "gpid", "success"]
    EXCHANGERESULT_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    exchangeResult: ExchangeResult
    gpid: str
    success: bool
    def __init__(self, gpid: _Optional[str] = ..., success: bool = ..., exchangeResult: _Optional[_Union[ExchangeResult, _Mapping]] = ...) -> None: ...

class ExecuteRecipeByServerRequest(_message.Message):
    __slots__ = ["executeRecipeRequests"]
    EXECUTERECIPEREQUESTS_FIELD_NUMBER: _ClassVar[int]
    executeRecipeRequests: _containers.RepeatedCompositeFieldContainer[ExecuteRecipeByServer]
    def __init__(self, executeRecipeRequests: _Optional[_Iterable[_Union[ExecuteRecipeByServer, _Mapping]]] = ...) -> None: ...

class ExecuteRecipeByServerResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ExecuteRecipeByServerResult]
    def __init__(self, results: _Optional[_Iterable[_Union[ExecuteRecipeByServerResult, _Mapping]]] = ...) -> None: ...

class ExecuteRecipeByServerResult(_message.Message):
    __slots__ = ["recipeCode", "results"]
    RECIPECODE_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    recipeCode: str
    results: _containers.RepeatedCompositeFieldContainer[ExecuteRecipeByServerPlayerResult]
    def __init__(self, recipeCode: _Optional[str] = ..., results: _Optional[_Iterable[_Union[ExecuteRecipeByServerPlayerResult, _Mapping]]] = ...) -> None: ...

class ExecuteRecipeEncrypted2Response(_message.Message):
    __slots__ = ["exchangeResult"]
    EXCHANGERESULT_FIELD_NUMBER: _ClassVar[int]
    exchangeResult: ExchangeRecipeResult
    def __init__(self, exchangeResult: _Optional[_Union[ExchangeRecipeResult, _Mapping]] = ...) -> None: ...

class ExecuteRecipeRequest(_message.Message):
    __slots__ = ["executionMultiplier", "inventoryItemIds", "recipeCode"]
    EXECUTIONMULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEMIDS_FIELD_NUMBER: _ClassVar[int]
    RECIPECODE_FIELD_NUMBER: _ClassVar[int]
    executionMultiplier: int
    inventoryItemIds: _containers.RepeatedScalarFieldContainer[int]
    recipeCode: str
    def __init__(self, recipeCode: _Optional[str] = ..., inventoryItemIds: _Optional[_Iterable[int]] = ..., executionMultiplier: _Optional[int] = ...) -> None: ...

class ExecuteRecipeResponse(_message.Message):
    __slots__ = ["exchangeResult"]
    EXCHANGERESULT_FIELD_NUMBER: _ClassVar[int]
    exchangeResult: ExchangeResult
    def __init__(self, exchangeResult: _Optional[_Union[ExchangeResult, _Mapping]] = ...) -> None: ...

class ExpiringRuleInfo(_message.Message):
    __slots__ = ["expiresAfter", "expiresAt"]
    EXPIRESAFTER_FIELD_NUMBER: _ClassVar[int]
    EXPIRESAT_FIELD_NUMBER: _ClassVar[int]
    expiresAfter: int
    expiresAt: int
    def __init__(self, expiresAfter: _Optional[int] = ..., expiresAt: _Optional[int] = ...) -> None: ...

class FilteredItems(_message.Message):
    __slots__ = ["gpid", "items"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    items: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, items: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., gpid: _Optional[str] = ...) -> None: ...

class FlagFilter(_message.Message):
    __slots__ = ["mask", "operation"]
    class MaskOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BITS_ALL_SET: FlagFilter.MaskOperation
    BITS_ANY_SET: FlagFilter.MaskOperation
    EQUALS: FlagFilter.MaskOperation
    MASK_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    mask: int
    operation: FlagFilter.MaskOperation
    def __init__(self, mask: _Optional[int] = ..., operation: _Optional[_Union[FlagFilter.MaskOperation, str]] = ...) -> None: ...

class GenerateCouponRequest(_message.Message):
    __slots__ = ["currencyAmount", "maxActivationsQuantity", "stackAmount"]
    CURRENCYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    MAXACTIVATIONSQUANTITY_FIELD_NUMBER: _ClassVar[int]
    STACKAMOUNT_FIELD_NUMBER: _ClassVar[int]
    currencyAmount: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    maxActivationsQuantity: int
    stackAmount: _containers.RepeatedCompositeFieldContainer[InventoryItemStackAmount]
    def __init__(self, stackAmount: _Optional[_Iterable[_Union[InventoryItemStackAmount, _Mapping]]] = ..., currencyAmount: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., maxActivationsQuantity: _Optional[int] = ...) -> None: ...

class GenerateCouponResponse(_message.Message):
    __slots__ = ["couponId"]
    COUPONID_FIELD_NUMBER: _ClassVar[int]
    couponId: str
    def __init__(self, couponId: _Optional[str] = ...) -> None: ...

class GetAllOtherPlayerPublicItemsRequest(_message.Message):
    __slots__ = ["flagFilter", "gpid"]
    FLAGFILTER_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    flagFilter: FlagFilter
    gpid: str
    def __init__(self, gpid: _Optional[str] = ..., flagFilter: _Optional[_Union[FlagFilter, _Mapping]] = ...) -> None: ...

class GetAllOtherPlayerPublicItemsResponse(_message.Message):
    __slots__ = ["playerInventoryItems"]
    PLAYERINVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, playerInventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class GetGeneratedCouponsRequest(_message.Message):
    __slots__ = ["offset"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: _common_message_pb2.Offset
    def __init__(self, offset: _Optional[_Union[_common_message_pb2.Offset, _Mapping]] = ...) -> None: ...

class GetGeneratedCouponsResponse(_message.Message):
    __slots__ = ["coupon"]
    COUPON_FIELD_NUMBER: _ClassVar[int]
    coupon: _containers.RepeatedCompositeFieldContainer[Coupon]
    def __init__(self, coupon: _Optional[_Iterable[_Union[Coupon, _Mapping]]] = ...) -> None: ...

class GetInventoryItemDefinitionsByServerRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInventoryItemDefinitionsByServerResponse(_message.Message):
    __slots__ = ["inventoryItemDefinitions"]
    INVENTORYITEMDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    inventoryItemDefinitions: _containers.RepeatedCompositeFieldContainer[InventoryItemDefinition]
    def __init__(self, inventoryItemDefinitions: _Optional[_Iterable[_Union[InventoryItemDefinition, _Mapping]]] = ...) -> None: ...

class GetInventoryItemDefinitionsRequest(_message.Message):
    __slots__ = ["lastUpdated"]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    lastUpdated: str
    def __init__(self, lastUpdated: _Optional[str] = ...) -> None: ...

class GetInventoryItemDefinitionsResponse(_message.Message):
    __slots__ = ["inventoryItemDefinitions", "lastUpdated"]
    INVENTORYITEMDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    inventoryItemDefinitions: _containers.RepeatedCompositeFieldContainer[InventoryItemDefinition]
    lastUpdated: str
    def __init__(self, inventoryItemDefinitions: _Optional[_Iterable[_Union[InventoryItemDefinition, _Mapping]]] = ..., lastUpdated: _Optional[str] = ...) -> None: ...

class GetInventoryItemPropertyDefinitionsRequest(_message.Message):
    __slots__ = ["lastUpdated"]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    lastUpdated: str
    def __init__(self, lastUpdated: _Optional[str] = ...) -> None: ...

class GetInventoryItemPropertyDefinitionsResponse(_message.Message):
    __slots__ = ["inventoryItemPropertyDefinitions", "lastUpdated"]
    INVENTORYITEMPROPERTYDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    inventoryItemPropertyDefinitions: _containers.RepeatedCompositeFieldContainer[InventoryItemPropertyDefinitions]
    lastUpdated: str
    def __init__(self, inventoryItemPropertyDefinitions: _Optional[_Iterable[_Union[InventoryItemPropertyDefinitions, _Mapping]]] = ..., lastUpdated: _Optional[str] = ...) -> None: ...

class GetOtherPlayerItemsRequest(_message.Message):
    __slots__ = ["gpid", "itemDefinitionIds"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONIDS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    itemDefinitionIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gpid: _Optional[str] = ..., itemDefinitionIds: _Optional[_Iterable[int]] = ...) -> None: ...

class GetOtherPlayerItemsResponse(_message.Message):
    __slots__ = ["playerInventoryItems"]
    PLAYERINVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, playerInventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class GetPlayerCouponsRequest(_message.Message):
    __slots__ = ["offset"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: _common_message_pb2.Offset
    def __init__(self, offset: _Optional[_Union[_common_message_pb2.Offset, _Mapping]] = ...) -> None: ...

class GetPlayerCouponsResponse(_message.Message):
    __slots__ = ["coupon"]
    COUPON_FIELD_NUMBER: _ClassVar[int]
    coupon: _containers.RepeatedCompositeFieldContainer[Coupon]
    def __init__(self, coupon: _Optional[_Iterable[_Union[Coupon, _Mapping]]] = ...) -> None: ...

class GetPlayerInventoryByServerRequest(_message.Message):
    __slots__ = ["gpid"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    def __init__(self, gpid: _Optional[str] = ...) -> None: ...

class GetPlayerInventoryByServerResponse(_message.Message):
    __slots__ = ["playerInventory"]
    PLAYERINVENTORY_FIELD_NUMBER: _ClassVar[int]
    playerInventory: PlayerInventory
    def __init__(self, playerInventory: _Optional[_Union[PlayerInventory, _Mapping]] = ...) -> None: ...

class GetPlayerInventoryRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPlayerInventoryResponse(_message.Message):
    __slots__ = ["playerInventory"]
    PLAYERINVENTORY_FIELD_NUMBER: _ClassVar[int]
    playerInventory: PlayerInventory
    def __init__(self, playerInventory: _Optional[_Union[PlayerInventory, _Mapping]] = ...) -> None: ...

class GetRecipeInfoRequest(_message.Message):
    __slots__ = ["recipeCodes"]
    RECIPECODES_FIELD_NUMBER: _ClassVar[int]
    recipeCodes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, recipeCodes: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRecipeInfoResponse(_message.Message):
    __slots__ = ["recipeInfos"]
    RECIPEINFOS_FIELD_NUMBER: _ClassVar[int]
    recipeInfos: _containers.RepeatedCompositeFieldContainer[RecipeInfoResponse]
    def __init__(self, recipeInfos: _Optional[_Iterable[_Union[RecipeInfoResponse, _Mapping]]] = ...) -> None: ...

class GetRecipeStateRequest(_message.Message):
    __slots__ = ["recipeCode"]
    RECIPECODE_FIELD_NUMBER: _ClassVar[int]
    recipeCode: str
    def __init__(self, recipeCode: _Optional[str] = ...) -> None: ...

class GetRecipeStateResponse(_message.Message):
    __slots__ = ["currencies", "currentExecutionCount", "resultSuites"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    CURRENTEXECUTIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESULTSUITES_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    currentExecutionCount: int
    resultSuites: _containers.RepeatedCompositeFieldContainer[ResultSuite]
    def __init__(self, currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., resultSuites: _Optional[_Iterable[_Union[ResultSuite, _Mapping]]] = ..., currentExecutionCount: _Optional[int] = ...) -> None: ...

class GetRecipeStatusRequest(_message.Message):
    __slots__ = ["recipeCode"]
    RECIPECODE_FIELD_NUMBER: _ClassVar[int]
    recipeCode: str
    def __init__(self, recipeCode: _Optional[str] = ...) -> None: ...

class GetRecipeStatusResponse(_message.Message):
    __slots__ = ["executionIntervalOk", "executionTimingOk", "msUntilNextExecution", "timesExecutedTotal"]
    EXECUTIONINTERVALOK_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONTIMINGOK_FIELD_NUMBER: _ClassVar[int]
    MSUNTILNEXTEXECUTION_FIELD_NUMBER: _ClassVar[int]
    TIMESEXECUTEDTOTAL_FIELD_NUMBER: _ClassVar[int]
    executionIntervalOk: bool
    executionTimingOk: bool
    msUntilNextExecution: int
    timesExecutedTotal: int
    def __init__(self, executionIntervalOk: bool = ..., executionTimingOk: bool = ..., timesExecutedTotal: _Optional[int] = ..., msUntilNextExecution: _Optional[int] = ...) -> None: ...

class GiveInventoryByServer(_message.Message):
    __slots__ = ["currencies", "gpids", "items"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    GPIDS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    gpids: _containers.RepeatedScalarFieldContainer[str]
    items: _containers.RepeatedCompositeFieldContainer[RewardInventoryItemAmount]
    def __init__(self, gpids: _Optional[_Iterable[str]] = ..., items: _Optional[_Iterable[_Union[RewardInventoryItemAmount, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...

class GiveInventoryByServerRequest(_message.Message):
    __slots__ = ["requests"]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[GiveInventoryByServer]
    def __init__(self, requests: _Optional[_Iterable[_Union[GiveInventoryByServer, _Mapping]]] = ...) -> None: ...

class GiveInventoryByServerRequestResult(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GiveInventoryByServerResult]
    def __init__(self, results: _Optional[_Iterable[_Union[GiveInventoryByServerResult, _Mapping]]] = ...) -> None: ...

class GiveInventoryByServerResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GiveInventoryByServerRequestResult]
    def __init__(self, results: _Optional[_Iterable[_Union[GiveInventoryByServerRequestResult, _Mapping]]] = ...) -> None: ...

class GiveInventoryByServerResult(_message.Message):
    __slots__ = ["currencies", "gpid", "inventoryItems", "success"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    GPID_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    gpid: str
    inventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    success: bool
    def __init__(self, success: bool = ..., gpid: _Optional[str] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., inventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class GivenReward(_message.Message):
    __slots__ = ["changedItems", "currencies", "items", "stats"]
    CHANGEDITEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    changedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    items: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    stats: _containers.RepeatedCompositeFieldContainer[StatAmount]
    def __init__(self, items: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., changedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., stats: _Optional[_Iterable[_Union[StatAmount, _Mapping]]] = ...) -> None: ...

class GuaranteedResult(_message.Message):
    __slots__ = ["regularResult", "specified"]
    class SpecifiedEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RecipeResult
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RecipeResult, _Mapping]] = ...) -> None: ...
    REGULARRESULT_FIELD_NUMBER: _ClassVar[int]
    SPECIFIED_FIELD_NUMBER: _ClassVar[int]
    regularResult: RegularResult
    specified: _containers.MessageMap[int, RecipeResult]
    def __init__(self, specified: _Optional[_Mapping[int, RecipeResult]] = ..., regularResult: _Optional[_Union[RegularResult, _Mapping]] = ...) -> None: ...

class InventoryItemAmount(_message.Message):
    __slots__ = ["inventoryItemDefinitionId", "value"]
    INVENTORYITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    inventoryItemDefinitionId: int
    value: int
    def __init__(self, inventoryItemDefinitionId: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class InventoryItemDefinition(_message.Message):
    __slots__ = ["buyPrice", "canBeRented", "canBeTraded", "definitions", "displayName", "id", "marketAvailableFromDate", "maxStackSize", "properties", "sellPrice"]
    class DefinitionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InventoryItemPropertyDefinition
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[InventoryItemPropertyDefinition, _Mapping]] = ...) -> None: ...
    class PropertiesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BUYPRICE_FIELD_NUMBER: _ClassVar[int]
    CANBERENTED_FIELD_NUMBER: _ClassVar[int]
    CANBETRADED_FIELD_NUMBER: _ClassVar[int]
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MARKETAVAILABLEFROMDATE_FIELD_NUMBER: _ClassVar[int]
    MAXSTACKSIZE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SELLPRICE_FIELD_NUMBER: _ClassVar[int]
    buyPrice: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    canBeRented: bool
    canBeTraded: bool
    definitions: _containers.MessageMap[str, InventoryItemPropertyDefinition]
    displayName: str
    id: int
    marketAvailableFromDate: int
    maxStackSize: int
    properties: _containers.ScalarMap[str, str]
    sellPrice: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    def __init__(self, id: _Optional[int] = ..., displayName: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ..., buyPrice: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., sellPrice: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., canBeTraded: bool = ..., definitions: _Optional[_Mapping[str, InventoryItemPropertyDefinition]] = ..., maxStackSize: _Optional[int] = ..., canBeRented: bool = ..., marketAvailableFromDate: _Optional[int] = ...) -> None: ...

class InventoryItemPropertyDefinition(_message.Message):
    __slots__ = ["boundExclusive", "name", "originInclusive", "propertyType", "retrievable", "saveInTrade", "setByType"]
    BOUNDEXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGININCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    PROPERTYTYPE_FIELD_NUMBER: _ClassVar[int]
    RETRIEVABLE_FIELD_NUMBER: _ClassVar[int]
    SAVEINTRADE_FIELD_NUMBER: _ClassVar[int]
    SETBYTYPE_FIELD_NUMBER: _ClassVar[int]
    boundExclusive: int
    name: str
    originInclusive: int
    propertyType: _common_message_pb2.PropertyType
    retrievable: RetrievableType
    saveInTrade: bool
    setByType: PropertySetByType
    def __init__(self, name: _Optional[str] = ..., propertyType: _Optional[_Union[_common_message_pb2.PropertyType, str]] = ..., saveInTrade: bool = ..., setByType: _Optional[_Union[PropertySetByType, str]] = ..., retrievable: _Optional[_Union[RetrievableType, str]] = ..., boundExclusive: _Optional[int] = ..., originInclusive: _Optional[int] = ...) -> None: ...

class InventoryItemPropertyDefinitions(_message.Message):
    __slots__ = ["definitions", "itemDefinitionId"]
    class DefinitionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InventoryItemPropertyDefinition
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[InventoryItemPropertyDefinition, _Mapping]] = ...) -> None: ...
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    definitions: _containers.MessageMap[str, InventoryItemPropertyDefinition]
    itemDefinitionId: int
    def __init__(self, itemDefinitionId: _Optional[int] = ..., definitions: _Optional[_Mapping[str, InventoryItemPropertyDefinition]] = ...) -> None: ...

class InventoryItemStackAmount(_message.Message):
    __slots__ = ["inventoryItemStackId", "itemDefinitionId", "value"]
    INVENTORYITEMSTACKID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    inventoryItemStackId: int
    itemDefinitionId: int
    value: int
    def __init__(self, inventoryItemStackId: _Optional[int] = ..., value: _Optional[int] = ..., itemDefinitionId: _Optional[int] = ...) -> None: ...

class ItemFlags(_message.Message):
    __slots__ = ["flags"]
    class FlagsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    flags: _containers.ScalarMap[int, int]
    def __init__(self, flags: _Optional[_Mapping[int, int]] = ...) -> None: ...

class ItemModificationValue(_message.Message):
    __slots__ = ["booleanValue", "floatValue", "intValue", "longValue", "stringValue", "type"]
    BOOLEANVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    booleanValue: bool
    floatValue: float
    intValue: int
    longValue: int
    stringValue: str
    type: _common_message_pb2.PropertyType
    def __init__(self, type: _Optional[_Union[_common_message_pb2.PropertyType, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., stringValue: _Optional[str] = ..., booleanValue: bool = ..., longValue: _Optional[int] = ...) -> None: ...

class ItemModifications(_message.Message):
    __slots__ = ["id", "itemDefinitionId", "modifications"]
    class ModificationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    itemDefinitionId: int
    modifications: _containers.MessageMap[str, ItemModificationValue]
    def __init__(self, id: _Optional[int] = ..., modifications: _Optional[_Mapping[str, ItemModificationValue]] = ..., itemDefinitionId: _Optional[int] = ...) -> None: ...

class MountInventoryItemRequest(_message.Message):
    __slots__ = ["consumedItemId", "modificationName", "modifiedItemId"]
    CONSUMEDITEMID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONNAME_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDITEMID_FIELD_NUMBER: _ClassVar[int]
    consumedItemId: int
    modificationName: str
    modifiedItemId: int
    def __init__(self, consumedItemId: _Optional[int] = ..., modifiedItemId: _Optional[int] = ..., modificationName: _Optional[str] = ...) -> None: ...

class MountInventoryItemResponse(_message.Message):
    __slots__ = ["modifiedItem", "unmountedItem"]
    MODIFIEDITEM_FIELD_NUMBER: _ClassVar[int]
    UNMOUNTEDITEM_FIELD_NUMBER: _ClassVar[int]
    modifiedItem: PlayerInventoryItem
    unmountedItem: PlayerInventoryItem
    def __init__(self, modifiedItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ..., unmountedItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class OnCouponActivatedEvent(_message.Message):
    __slots__ = ["reward"]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    reward: GivenReward
    def __init__(self, reward: _Optional[_Union[GivenReward, _Mapping]] = ...) -> None: ...

class OnInventoryChangedEvent(_message.Message):
    __slots__ = ["addedItems", "changedItems", "currencies"]
    ADDEDITEMS_FIELD_NUMBER: _ClassVar[int]
    CHANGEDITEMS_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    addedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    changedItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    def __init__(self, addedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., changedItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...

class PlayerInventory(_message.Message):
    __slots__ = ["currencies", "inventoryItems"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    inventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., inventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class PlayerInventoryItem(_message.Message):
    __slots__ = ["block", "date", "flags", "id", "isPublic", "itemDefinitionId", "modifications", "newItemsQuantity", "quantity"]
    class ModificationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISPUBLIC_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    NEWITEMSQUANTITY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    block: BlockedAction
    date: int
    flags: int
    id: int
    isPublic: bool
    itemDefinitionId: int
    modifications: _containers.MessageMap[str, ItemModificationValue]
    newItemsQuantity: int
    quantity: int
    def __init__(self, id: _Optional[int] = ..., itemDefinitionId: _Optional[int] = ..., quantity: _Optional[int] = ..., flags: _Optional[int] = ..., date: _Optional[int] = ..., modifications: _Optional[_Mapping[str, ItemModificationValue]] = ..., block: _Optional[_Union[BlockedAction, _Mapping]] = ..., isPublic: bool = ..., newItemsQuantity: _Optional[int] = ...) -> None: ...

class PlayerInventoryItemHistory(_message.Message):
    __slots__ = ["block", "flags", "itemDefinitionId", "modifications", "quantity"]
    class ModificationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    block: BlockedAction
    flags: int
    itemDefinitionId: int
    modifications: _containers.MessageMap[str, ItemModificationValue]
    quantity: int
    def __init__(self, itemDefinitionId: _Optional[int] = ..., quantity: _Optional[int] = ..., flags: _Optional[int] = ..., modifications: _Optional[_Mapping[str, ItemModificationValue]] = ..., block: _Optional[_Union[BlockedAction, _Mapping]] = ...) -> None: ...

class PlayerInventoryItemsByServerRequest(_message.Message):
    __slots__ = ["flagFilter", "gpids"]
    FLAGFILTER_FIELD_NUMBER: _ClassVar[int]
    GPIDS_FIELD_NUMBER: _ClassVar[int]
    flagFilter: FlagFilter
    gpids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, flagFilter: _Optional[_Union[FlagFilter, _Mapping]] = ..., gpids: _Optional[_Iterable[str]] = ...) -> None: ...

class PlayerInventoryItemsByServerResponse(_message.Message):
    __slots__ = ["filteredItems"]
    FILTEREDITEMS_FIELD_NUMBER: _ClassVar[int]
    filteredItems: _containers.RepeatedCompositeFieldContainer[FilteredItems]
    def __init__(self, filteredItems: _Optional[_Iterable[_Union[FilteredItems, _Mapping]]] = ...) -> None: ...

class ProgressGameEventAmount(_message.Message):
    __slots__ = ["eventCode", "points"]
    EVENTCODE_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    eventCode: str
    points: int
    def __init__(self, eventCode: _Optional[str] = ..., points: _Optional[int] = ...) -> None: ...

class PropertyBasedAmount(_message.Message):
    __slots__ = ["amount", "property"]
    class PropertyEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    amount: int
    property: _containers.ScalarMap[str, str]
    def __init__(self, property: _Optional[_Mapping[str, str]] = ..., amount: _Optional[int] = ...) -> None: ...

class RecipeComponents(_message.Message):
    __slots__ = ["currencies", "items", "propertyBasedAmounts"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PROPERTYBASEDAMOUNTS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    items: _containers.RepeatedCompositeFieldContainer[InventoryItemAmount]
    propertyBasedAmounts: _containers.RepeatedCompositeFieldContainer[PropertyBasedAmount]
    def __init__(self, items: _Optional[_Iterable[_Union[InventoryItemAmount, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., propertyBasedAmounts: _Optional[_Iterable[_Union[PropertyBasedAmount, _Mapping]]] = ...) -> None: ...

class RecipeInfoLite(_message.Message):
    __slots__ = ["entities", "expiringRule", "recipe", "results"]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    EXPIRINGRULE_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[ExchangeEntity]
    expiringRule: ExpiringRuleInfo
    recipe: str
    results: _containers.RepeatedCompositeFieldContainer[RecipeResult]
    def __init__(self, recipe: _Optional[str] = ..., entities: _Optional[_Iterable[_Union[ExchangeEntity, _Mapping]]] = ..., expiringRule: _Optional[_Union[ExpiringRuleInfo, _Mapping]] = ..., results: _Optional[_Iterable[_Union[RecipeResult, _Mapping]]] = ...) -> None: ...

class RecipeInfoResponse(_message.Message):
    __slots__ = ["components", "expiringRule", "guaranteedResult", "recipe", "results"]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    EXPIRINGRULE_FIELD_NUMBER: _ClassVar[int]
    GUARANTEEDRESULT_FIELD_NUMBER: _ClassVar[int]
    RECIPE_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    components: RecipeComponents
    expiringRule: ExpiringRuleInfo
    guaranteedResult: GuaranteedResult
    recipe: str
    results: _containers.RepeatedCompositeFieldContainer[RecipeResult]
    def __init__(self, recipe: _Optional[str] = ..., components: _Optional[_Union[RecipeComponents, _Mapping]] = ..., results: _Optional[_Iterable[_Union[RecipeResult, _Mapping]]] = ..., guaranteedResult: _Optional[_Union[GuaranteedResult, _Mapping]] = ..., expiringRule: _Optional[_Union[ExpiringRuleInfo, _Mapping]] = ...) -> None: ...

class RecipeResult(_message.Message):
    __slots__ = ["currencies", "items", "progressGameEventAmounts", "propertyBasedAmounts", "recipes", "statAmounts"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PROGRESSGAMEEVENTAMOUNTS_FIELD_NUMBER: _ClassVar[int]
    PROPERTYBASEDAMOUNTS_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    STATAMOUNTS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    items: _containers.RepeatedCompositeFieldContainer[InventoryItemAmount]
    progressGameEventAmounts: _containers.RepeatedCompositeFieldContainer[ProgressGameEventAmount]
    propertyBasedAmounts: _containers.RepeatedCompositeFieldContainer[ResultPropertyBasedAmount]
    recipes: _containers.RepeatedScalarFieldContainer[str]
    statAmounts: _containers.RepeatedCompositeFieldContainer[StatAmount]
    def __init__(self, items: _Optional[_Iterable[_Union[InventoryItemAmount, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., propertyBasedAmounts: _Optional[_Iterable[_Union[ResultPropertyBasedAmount, _Mapping]]] = ..., progressGameEventAmounts: _Optional[_Iterable[_Union[ProgressGameEventAmount, _Mapping]]] = ..., statAmounts: _Optional[_Iterable[_Union[StatAmount, _Mapping]]] = ..., recipes: _Optional[_Iterable[str]] = ...) -> None: ...

class RegularResult(_message.Message):
    __slots__ = ["result", "step"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    result: RecipeResult
    step: int
    def __init__(self, result: _Optional[_Union[RecipeResult, _Mapping]] = ..., step: _Optional[int] = ...) -> None: ...

class RemoveItemModificationRequest(_message.Message):
    __slots__ = ["itemDefinitionId", "itemId", "propertyName"]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionId: int
    itemId: int
    propertyName: str
    def __init__(self, itemId: _Optional[int] = ..., propertyName: _Optional[str] = ..., itemDefinitionId: _Optional[int] = ...) -> None: ...

class RemoveItemModificationResponse(_message.Message):
    __slots__ = ["playerInventoryItem"]
    PLAYERINVENTORYITEM_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItem: PlayerInventoryItem
    def __init__(self, playerInventoryItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class RemovedInventory(_message.Message):
    __slots__ = ["currencies", "items"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    items: _containers.RepeatedCompositeFieldContainer[InventoryItemStackAmount]
    def __init__(self, items: _Optional[_Iterable[_Union[InventoryItemStackAmount, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...

class ResultPropertyBasedAmount(_message.Message):
    __slots__ = ["computableProperty", "propertyBasedAmount"]
    COMPUTABLEPROPERTY_FIELD_NUMBER: _ClassVar[int]
    PROPERTYBASEDAMOUNT_FIELD_NUMBER: _ClassVar[int]
    computableProperty: _containers.RepeatedScalarFieldContainer[str]
    propertyBasedAmount: PropertyBasedAmount
    def __init__(self, propertyBasedAmount: _Optional[_Union[PropertyBasedAmount, _Mapping]] = ..., computableProperty: _Optional[_Iterable[str]] = ...) -> None: ...

class ResultSuite(_message.Message):
    __slots__ = ["itemDefinitionIds", "probability"]
    ITEMDEFINITIONIDS_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    itemDefinitionIds: _containers.RepeatedScalarFieldContainer[int]
    probability: float
    def __init__(self, probability: _Optional[float] = ..., itemDefinitionIds: _Optional[_Iterable[int]] = ...) -> None: ...

class RewardInfo(_message.Message):
    __slots__ = ["currencies", "expiringRule", "items", "recipes"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    EXPIRINGRULE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    RECIPES_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    expiringRule: ExpiringRuleInfo
    items: _containers.RepeatedCompositeFieldContainer[InventoryItemAmount]
    recipes: _containers.RepeatedCompositeFieldContainer[RecipeInfoLite]
    def __init__(self, items: _Optional[_Iterable[_Union[InventoryItemAmount, _Mapping]]] = ..., currencies: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., recipes: _Optional[_Iterable[_Union[RecipeInfoLite, _Mapping]]] = ..., expiringRule: _Optional[_Union[ExpiringRuleInfo, _Mapping]] = ...) -> None: ...

class RewardInventoryItemAmount(_message.Message):
    __slots__ = ["flags", "itemDefinitionId", "properties", "quantity"]
    class PropertiesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ItemModificationValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ItemModificationValue, _Mapping]] = ...) -> None: ...
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    flags: int
    itemDefinitionId: int
    properties: _containers.MessageMap[str, ItemModificationValue]
    quantity: int
    def __init__(self, itemDefinitionId: _Optional[int] = ..., quantity: _Optional[int] = ..., flags: _Optional[int] = ..., properties: _Optional[_Mapping[str, ItemModificationValue]] = ...) -> None: ...

class SellInventoryItemRequest(_message.Message):
    __slots__ = ["currencyId", "inventoryItemId", "itemDefinitionId", "quantity"]
    CURRENCYID_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    currencyId: int
    inventoryItemId: int
    itemDefinitionId: int
    quantity: int
    def __init__(self, inventoryItemId: _Optional[int] = ..., quantity: _Optional[int] = ..., currencyId: _Optional[int] = ..., itemDefinitionId: _Optional[int] = ...) -> None: ...

class SellInventoryItemResponse(_message.Message):
    __slots__ = ["playerInventoryItem"]
    PLAYERINVENTORYITEM_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItem: PlayerInventoryItem
    def __init__(self, playerInventoryItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class SetInventoryItemFlagsRequest(_message.Message):
    __slots__ = ["itemFlags"]
    ITEMFLAGS_FIELD_NUMBER: _ClassVar[int]
    itemFlags: ItemFlags
    def __init__(self, itemFlags: _Optional[_Union[ItemFlags, _Mapping]] = ...) -> None: ...

class SetInventoryItemFlagsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetInventoryItemPublicityRequest(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ChangePublicityItem]
    def __init__(self, items: _Optional[_Iterable[_Union[ChangePublicityItem, _Mapping]]] = ...) -> None: ...

class SetInventoryItemPublicityResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, items: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class SetItemsModificationsByServerRequest(_message.Message):
    __slots__ = ["requests"]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[SetPlayerItemsModifications]
    def __init__(self, requests: _Optional[_Iterable[_Union[SetPlayerItemsModifications, _Mapping]]] = ...) -> None: ...

class SetItemsModificationsByServerResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SetPlayerItemsModificationsResult]
    def __init__(self, results: _Optional[_Iterable[_Union[SetPlayerItemsModificationsResult, _Mapping]]] = ...) -> None: ...

class SetItemsModificationsRequest(_message.Message):
    __slots__ = ["itemsModifications"]
    ITEMSMODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    itemsModifications: _containers.RepeatedCompositeFieldContainer[ItemModifications]
    def __init__(self, itemsModifications: _Optional[_Iterable[_Union[ItemModifications, _Mapping]]] = ...) -> None: ...

class SetItemsModificationsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetPlayerItemsModifications(_message.Message):
    __slots__ = ["gpid", "items"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    items: _containers.RepeatedCompositeFieldContainer[ItemModifications]
    def __init__(self, gpid: _Optional[str] = ..., items: _Optional[_Iterable[_Union[ItemModifications, _Mapping]]] = ...) -> None: ...

class SetPlayerItemsModificationsResult(_message.Message):
    __slots__ = ["gpid", "success"]
    GPID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    gpid: str
    success: bool
    def __init__(self, gpid: _Optional[str] = ..., success: bool = ...) -> None: ...

class StatAmount(_message.Message):
    __slots__ = ["floatValue", "intValue", "longValue", "propertyType", "statId"]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    PROPERTYTYPE_FIELD_NUMBER: _ClassVar[int]
    STATID_FIELD_NUMBER: _ClassVar[int]
    floatValue: float
    intValue: int
    longValue: int
    propertyType: _common_message_pb2.PropertyType
    statId: str
    def __init__(self, statId: _Optional[str] = ..., propertyType: _Optional[_Union[_common_message_pb2.PropertyType, str]] = ..., intValue: _Optional[int] = ..., floatValue: _Optional[float] = ..., longValue: _Optional[int] = ...) -> None: ...

class TradeInventoryItemsRequest(_message.Message):
    __slots__ = ["localCurrencyAmount", "localItemId", "remoteCurrencyAmount", "remoteGpid", "remoteItemId"]
    LOCALCURRENCYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    LOCALITEMID_FIELD_NUMBER: _ClassVar[int]
    REMOTECURRENCYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    REMOTEGPID_FIELD_NUMBER: _ClassVar[int]
    REMOTEITEMID_FIELD_NUMBER: _ClassVar[int]
    localCurrencyAmount: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    localItemId: _containers.RepeatedScalarFieldContainer[int]
    remoteCurrencyAmount: _containers.RepeatedCompositeFieldContainer[_currency_message_pb2.CurrencyAmount]
    remoteGpid: int
    remoteItemId: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, localItemId: _Optional[_Iterable[int]] = ..., localCurrencyAmount: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ..., remoteGpid: _Optional[int] = ..., remoteItemId: _Optional[_Iterable[int]] = ..., remoteCurrencyAmount: _Optional[_Iterable[_Union[_currency_message_pb2.CurrencyAmount, _Mapping]]] = ...) -> None: ...

class TradeInventoryItemsResponse(_message.Message):
    __slots__ = ["playerInventoryItems"]
    PLAYERINVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, playerInventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class TransferInventoryItemsRequest(_message.Message):
    __slots__ = ["fromItemId", "quantity", "toItemId"]
    FROMITEMID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TOITEMID_FIELD_NUMBER: _ClassVar[int]
    fromItemId: int
    quantity: int
    toItemId: int
    def __init__(self, fromItemId: _Optional[int] = ..., toItemId: _Optional[int] = ..., quantity: _Optional[int] = ...) -> None: ...

class TransferInventoryItemsResponse(_message.Message):
    __slots__ = ["playerInventoryItems"]
    PLAYERINVENTORYITEMS_FIELD_NUMBER: _ClassVar[int]
    playerInventoryItems: _containers.RepeatedCompositeFieldContainer[PlayerInventoryItem]
    def __init__(self, playerInventoryItems: _Optional[_Iterable[_Union[PlayerInventoryItem, _Mapping]]] = ...) -> None: ...

class UnmountInventoryItemRequest(_message.Message):
    __slots__ = ["modificationName", "modifiedItemId"]
    MODIFICATIONNAME_FIELD_NUMBER: _ClassVar[int]
    MODIFIEDITEMID_FIELD_NUMBER: _ClassVar[int]
    modificationName: str
    modifiedItemId: int
    def __init__(self, modifiedItemId: _Optional[int] = ..., modificationName: _Optional[str] = ...) -> None: ...

class UnmountInventoryItemResponse(_message.Message):
    __slots__ = ["unmountedItem"]
    UNMOUNTEDITEM_FIELD_NUMBER: _ClassVar[int]
    unmountedItem: PlayerInventoryItem
    def __init__(self, unmountedItem: _Optional[_Union[PlayerInventoryItem, _Mapping]] = ...) -> None: ...

class PropertySetByType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RetrievableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
