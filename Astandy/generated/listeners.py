#This file was automatically generated!

from collections.abc import Callable
from functools import lru_cache

from google.protobuf.message import Message

import Astandy
from Astandy.listener import Listener
from Astandy.types.update import Update
from Astandy.enums.events import Event
from .schemes_pb2 import *


class GeneratedUpdate(Update):
    def __init__(self):
        super().__init__()
        self.data: Message = None 

    def __str__(self):
        return f'{self.__class__.__name__}(event={self.event.name},data={self.data})'

class GeneratedEvent(Event):
    MARKETPLACE_REMOTE_EVENT_LISTENER_ON_PLAYER_REQUEST_OPENED = 5
    MARKETPLACE_REMOTE_EVENT_LISTENER_ON_TRADE_UPDATED = 1
    MARKETPLACE_REMOTE_EVENT_LISTENER_ON_TRADE_REQUEST_OPENED = 3
    MARKETPLACE_REMOTE_EVENT_LISTENER_ON_PLAYER_REQUEST_CLOSED = 4
    MARKETPLACE_REMOTE_EVENT_LISTENER_ON_TRADE_REQUEST_CLOSED = 2
    SYSTEM_MESSAGES_REMOTE_EVENT_LISTENER_ON_SYSTEM_MESSAGE_RECEIVED = 126
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_REVOKE_INVITE_TO_LOBBY_EVENT = 72
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_SPECTATOR_INVITED_TO_LOBBY_EVENT = 77
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_PHOTON_GAME_CHANGED_EVENT = 68
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_MAX_MEMBERS_CHANGED_EVENT = 67
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_DATA_CHANGED_EVENT = 61
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_TYPE_CHANGED_EVENT = 70
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_RECEIVED_INVITE_TO_LOBBY_EVENT = 65
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_JOINABLE_CHANGED_EVENT = 62
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_PLAYER_JOINED_LOBBY_EVENT = 66
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_REFUSE_INVITE_TO_LOBBY_EVENT = 75
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_CHAT_MESSAGE_EVENT = 64
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_PLAYER_KICKED_FROM_LOBBY_EVENT = 74
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_PLAYER_TYPE_CHANGED_EVENT = 78
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_RECEIVED_SPECTATOR_INVITE_TO_LOBBY_EVENT = 79
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_OWNER_CHANGED_EVENT = 73
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_PLAYER_INVITED_TO_LOBBY_EVENT = 63
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_GAME_SERVER_CHANGED_EVENT = 80
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_NAME_CHANGED_EVENT = 81
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_PLAYER_LEFT_LOBBY_EVENT = 69
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_SPECTATOR_JOINED_LOBBY_EVENT = 76
    MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_MAX_SPECTATORS_CHANGED_EVENT = 71
    IN_APPS_REMOTE_EVENT_LISTENER_ON_IN_APP_EVENT = 119
    CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_MEMBERS_COUNT_INCREASED = 53
    CLANS_REMOTE_EVENT_LISTENER_ON_READ_CLOSED_INVITE_REQUEST_EVENT = 38
    CLANS_REMOTE_EVENT_LISTENER_ON_JOIN_REQUEST_DECLINED_EVENT = 45
    CLANS_REMOTE_EVENT_LISTENER_ON_KICKED_MEMBER = 42
    CLANS_REMOTE_EVENT_LISTENER_ON_JOIN_REQUEST_CANCELLED_EVENT = 37
    CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_TYPE_CHANGED = 48
    CLANS_REMOTE_EVENT_LISTENER_ON_ASSIGNED_LEADER_ROLE_EVENT = 47
    CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_TAG_AND_NAME_CHANGED = 52
    CLANS_REMOTE_EVENT_LISTENER_ON_LEFT_FROM_CLAN = 46
    CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_MEMBER_DECLINED_REQUEST_EVENT = 41
    CLANS_REMOTE_EVENT_LISTENER_ON_MEMBER_JOINED_TO_CLAN = 35
    CLANS_REMOTE_EVENT_LISTENER_ON_JOIN_REQUEST_TAKEN = 33
    CLANS_REMOTE_EVENT_LISTENER_ON_INVITE_REQUEST_DECLINED_EVENT = 40
    CLANS_REMOTE_EVENT_LISTENER_ON_INVITE_REQUEST_CANCELLED_EVENT = 51
    CLANS_REMOTE_EVENT_LISTENER_ON_ASSIGNED_ROLE_EVENT = 43
    CLANS_REMOTE_EVENT_LISTENER_ON_PLAYER_AVATAR_CHANGED_EVENT = 32
    CLANS_REMOTE_EVENT_LISTENER_ON_ONLINE_STATUS_CHANGED_EVENT = 31
    CLANS_REMOTE_EVENT_LISTENER_ON_PLAYER_NAME_CHANGED_EVENT = 34
    CLANS_REMOTE_EVENT_LISTENER_ON_KICKED_EVENT = 50
    CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_DESCRIPTION_CHANGED_EVENT = 54
    CLANS_REMOTE_EVENT_LISTENER_ON_PLAYER_ATTRIBUTES_CHANGED = 36
    CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_AVATAR_CHANGED_EVENT = 49
    CLANS_REMOTE_EVENT_LISTENER_ON_INVITED_TO_CLAN_EVENT = 44
    CLANS_REMOTE_EVENT_LISTENER_ON_JOINED_TO_CLAN = 39
    INVENTORY_REMOTE_EVENT_LISTENER_ON_INVENTORY_CHANGED = 111
    INVENTORY_REMOTE_EVENT_LISTENER_ON_COUPON_ACTIVATED = 112
    MATCHES_REMOTE_EVENT_LISTENER_ON_MATCH_FINISHED = 95
    FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_NAME_CHANGED_EVENT = 14
    FRIENDS_REMOTE_EVENT_LISTENER_ON_PLAYER_STATUS_CHANGED_EVENT = 11
    FRIENDS_REMOTE_EVENT_LISTENER_ON_PLAYER_ATTRIBUTES_CHANGED = 16
    FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_REMOVED_EVENT = 17
    FRIENDS_REMOTE_EVENT_LISTENER_ON_REVOKE_FRIENDSHIP_REQUEST_EVENT = 18
    FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_ADDED_EVENT = 15
    FRIENDS_REMOTE_EVENT_LISTENER_ON_NEW_FRIENDSHIP_REQUEST_EVENT = 13
    FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_AVATAR_CHANGED_EVENT = 12
    MESSAGES_REMOTE_EVENT_LISTENER_ON_MSG_FROM_FRIEND_EVENT = 121
    CLAN_STATS_REMOTE_EVENT_LISTENER_ON_CLAN_STATS_UPDATED = 59
    GAME_EVENT_REMOTE_EVENT_LISTENER_ON_GAME_PASS_CHANGED = 107
    GAME_EVENT_REMOTE_EVENT_LISTENER_ON_PROGRESS_GAME_EVENT = 106
    GAME_EVENT_REMOTE_EVENT_LISTENER_ON_PROGRESS_CHALLENGE_EVENT = 108
    CLAN_MESSAGES_REMOTE_EVENT_LISTENER_ON_INCOMING_CLAN_CHAT_MESSAGE_EVENT = 58
    ADS_REMOTE_EVENT_LISTENER_ON_AD_REWARD_EVENT = 116
    PLAYER_STATS_REMOTE_EVENT_LISTENER_ON_STATS_UPDATED_EVENT = 101
    MATCHMAKING_REMOTE_LISTENER_ON_MATCHMAKING_PROGRESS = 2
    MATCHMAKING_REMOTE_LISTENER_ON_PLAYERS_CONFIRMED = 3
    MATCHMAKING_REMOTE_LISTENER_ON_MATCHMAKING_DONE = 1
    MATCHMAKING_REMOTE_LISTENER_ON_MATCHMAKING_FAIL = 4

    @staticmethod
    @lru_cache(None)
    def has_value(item):
        return item in [v.value for v in GeneratedEvent.__members__.values()]


class MarketplaceRemoteEventListenerOnPlayerRequestOpenedUpdate(GeneratedUpdate):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_PLAYER_REQUEST_OPENED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnPlayerRequestOpenedEvent()
        self.data.ParseFromString(payload)
class MarketplaceRemoteEventListenerOnPlayerRequestOpenedListener(Listener):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_PLAYER_REQUEST_OPENED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MarketplaceRemoteEventListenerOnPlayerRequestOpenedUpdate):
        await self._callback(client, update)
class MarketplaceRemoteEventListenerOnPlayerRequestOpened:
    def MarketplaceRemoteEventListenerOnPlayerRequestOpened(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MarketplaceRemoteEventListenerOnPlayerRequestOpenedListener(func))
            return func
        return decorator

class MarketplaceRemoteEventListenerOnTradeUpdatedUpdate(GeneratedUpdate):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_TRADE_UPDATED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnTradeUpdatedEvent()
        self.data.ParseFromString(payload)
class MarketplaceRemoteEventListenerOnTradeUpdatedListener(Listener):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_TRADE_UPDATED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MarketplaceRemoteEventListenerOnTradeUpdatedUpdate):
        await self._callback(client, update)
class MarketplaceRemoteEventListenerOnTradeUpdated:
    def MarketplaceRemoteEventListenerOnTradeUpdated(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MarketplaceRemoteEventListenerOnTradeUpdatedListener(func))
            return func
        return decorator

class MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate(GeneratedUpdate):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_TRADE_REQUEST_OPENED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnTradeRequestOpenedEvent()
        self.data.ParseFromString(payload)
class MarketplaceRemoteEventListenerOnTradeRequestOpenedListener(Listener):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_TRADE_REQUEST_OPENED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate):
        await self._callback(client, update)
class MarketplaceRemoteEventListenerOnTradeRequestOpened:
    def MarketplaceRemoteEventListenerOnTradeRequestOpened(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MarketplaceRemoteEventListenerOnTradeRequestOpenedListener(func))
            return func
        return decorator

class MarketplaceRemoteEventListenerOnPlayerRequestClosedUpdate(GeneratedUpdate):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_PLAYER_REQUEST_CLOSED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnPlayerRequestClosedEvent()
        self.data.ParseFromString(payload)
class MarketplaceRemoteEventListenerOnPlayerRequestClosedListener(Listener):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_PLAYER_REQUEST_CLOSED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MarketplaceRemoteEventListenerOnPlayerRequestClosedUpdate):
        await self._callback(client, update)
class MarketplaceRemoteEventListenerOnPlayerRequestClosed:
    def MarketplaceRemoteEventListenerOnPlayerRequestClosed(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MarketplaceRemoteEventListenerOnPlayerRequestClosedListener(func))
            return func
        return decorator

class MarketplaceRemoteEventListenerOnTradeRequestClosedUpdate(GeneratedUpdate):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_TRADE_REQUEST_CLOSED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnTradeRequestClosedEvent()
        self.data.ParseFromString(payload)
class MarketplaceRemoteEventListenerOnTradeRequestClosedListener(Listener):
    event = GeneratedEvent.MARKETPLACE_REMOTE_EVENT_LISTENER_ON_TRADE_REQUEST_CLOSED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MarketplaceRemoteEventListenerOnTradeRequestClosedUpdate):
        await self._callback(client, update)
class MarketplaceRemoteEventListenerOnTradeRequestClosed:
    def MarketplaceRemoteEventListenerOnTradeRequestClosed(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MarketplaceRemoteEventListenerOnTradeRequestClosedListener(func))
            return func
        return decorator

class SystemMessagesRemoteEventListenerOnSystemMessageReceivedUpdate(GeneratedUpdate):
    event = GeneratedEvent.SYSTEM_MESSAGES_REMOTE_EVENT_LISTENER_ON_SYSTEM_MESSAGE_RECEIVED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnSystemMessageReceivedEvent()
        self.data.ParseFromString(payload)
class SystemMessagesRemoteEventListenerOnSystemMessageReceivedListener(Listener):
    event = GeneratedEvent.SYSTEM_MESSAGES_REMOTE_EVENT_LISTENER_ON_SYSTEM_MESSAGE_RECEIVED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: SystemMessagesRemoteEventListenerOnSystemMessageReceivedUpdate):
        await self._callback(client, update)
class SystemMessagesRemoteEventListenerOnSystemMessageReceived:
    def SystemMessagesRemoteEventListenerOnSystemMessageReceived(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(SystemMessagesRemoteEventListenerOnSystemMessageReceivedListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_REVOKE_INVITE_TO_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnRevokeInviteToLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_REVOKE_INVITE_TO_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEvent:
    def MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_SPECTATOR_INVITED_TO_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnNewSpectatorInvitedToLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_SPECTATOR_INVITED_TO_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEvent:
    def MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_PHOTON_GAME_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyPhotonGameChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_PHOTON_GAME_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_MAX_MEMBERS_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyMaxMembersChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_MAX_MEMBERS_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyDataChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_DATA_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyDataChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyDataChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_DATA_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyDataChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyDataChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyDataChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyDataChangedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyTypeChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_TYPE_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyTypeChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyTypeChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_TYPE_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyTypeChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyTypeChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyTypeChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyTypeChangedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_RECEIVED_INVITE_TO_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnReceivedInviteToLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_RECEIVED_INVITE_TO_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEvent:
    def MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyJoinableChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_JOINABLE_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyJoinableChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyJoinableChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_JOINABLE_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyJoinableChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyJoinableChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyJoinableChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyJoinableChangedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_PLAYER_JOINED_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnNewPlayerJoinedLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_PLAYER_JOINED_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEvent:
    def MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_REFUSE_INVITE_TO_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnRefuseInviteToLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_REFUSE_INVITE_TO_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEvent:
    def MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyChatMessageEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_CHAT_MESSAGE_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyChatMessageEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyChatMessageEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_CHAT_MESSAGE_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyChatMessageEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyChatMessageEvent:
    def MatchmakingRemoteEventListenerOnLobbyChatMessageEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyChatMessageEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_PLAYER_KICKED_FROM_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnPlayerKickedFromLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_PLAYER_KICKED_FROM_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEvent:
    def MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_PLAYER_TYPE_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyPlayerTypeChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_PLAYER_TYPE_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_RECEIVED_SPECTATOR_INVITE_TO_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnReceivedSpectatorInviteToLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_RECEIVED_SPECTATOR_INVITE_TO_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEvent:
    def MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyOwnerChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_OWNER_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyOwnerChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyOwnerChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_OWNER_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyOwnerChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyOwnerChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyOwnerChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyOwnerChangedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_PLAYER_INVITED_TO_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnNewPlayerInvitedToLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_PLAYER_INVITED_TO_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEvent:
    def MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyGameServerChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_GAME_SERVER_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyGameServerChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyGameServerChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_GAME_SERVER_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyGameServerChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyGameServerChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyGameServerChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyGameServerChangedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyNameChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_NAME_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyNameChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyNameChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_NAME_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyNameChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyNameChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyNameChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyNameChangedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnPlayerLeftLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_PLAYER_LEFT_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnPlayerLeftLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnPlayerLeftLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_PLAYER_LEFT_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnPlayerLeftLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnPlayerLeftLobbyEvent:
    def MatchmakingRemoteEventListenerOnPlayerLeftLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnPlayerLeftLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_SPECTATOR_JOINED_LOBBY_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnNewSpectatorJoinedLobbyEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_NEW_SPECTATOR_JOINED_LOBBY_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEvent:
    def MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEventListener(func))
            return func
        return decorator

class MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_MAX_SPECTATORS_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLobbyMaxSpectatorsChangedEvent()
        self.data.ParseFromString(payload)
class MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEventListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_EVENT_LISTENER_ON_LOBBY_MAX_SPECTATORS_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEventUpdate):
        await self._callback(client, update)
class MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEvent:
    def MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEventListener(func))
            return func
        return decorator

class InAppsRemoteEventListenerOnInAppEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.IN_APPS_REMOTE_EVENT_LISTENER_ON_IN_APP_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnInAppEvent()
        self.data.ParseFromString(payload)
class InAppsRemoteEventListenerOnInAppEventListener(Listener):
    event = GeneratedEvent.IN_APPS_REMOTE_EVENT_LISTENER_ON_IN_APP_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: InAppsRemoteEventListenerOnInAppEventUpdate):
        await self._callback(client, update)
class InAppsRemoteEventListenerOnInAppEvent:
    def InAppsRemoteEventListenerOnInAppEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(InAppsRemoteEventListenerOnInAppEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnClanMembersCountIncreasedUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_MEMBERS_COUNT_INCREASED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnClanMaxMembersCountIncreased()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnClanMembersCountIncreasedListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_MEMBERS_COUNT_INCREASED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnClanMembersCountIncreasedUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnClanMembersCountIncreased:
    def ClansRemoteEventListenerOnClanMembersCountIncreased(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnClanMembersCountIncreasedListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnReadClosedInviteRequestEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_READ_CLOSED_INVITE_REQUEST_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnReadClosedInviteRequestEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnReadClosedInviteRequestEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_READ_CLOSED_INVITE_REQUEST_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnReadClosedInviteRequestEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnReadClosedInviteRequestEvent:
    def ClansRemoteEventListenerOnReadClosedInviteRequestEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnReadClosedInviteRequestEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnJoinRequestDeclinedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_JOIN_REQUEST_DECLINED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnJoinRequestDeclinedEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnJoinRequestDeclinedEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_JOIN_REQUEST_DECLINED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnJoinRequestDeclinedEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnJoinRequestDeclinedEvent:
    def ClansRemoteEventListenerOnJoinRequestDeclinedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnJoinRequestDeclinedEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnKickedMemberUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_KICKED_MEMBER
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnKickedMemberEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnKickedMemberListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_KICKED_MEMBER
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnKickedMemberUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnKickedMember:
    def ClansRemoteEventListenerOnKickedMember(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnKickedMemberListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnJoinRequestCancelledEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_JOIN_REQUEST_CANCELLED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnJoinRequestCancelledEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnJoinRequestCancelledEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_JOIN_REQUEST_CANCELLED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnJoinRequestCancelledEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnJoinRequestCancelledEvent:
    def ClansRemoteEventListenerOnJoinRequestCancelledEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnJoinRequestCancelledEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnClanTypeChangedUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_TYPE_CHANGED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnClanTypeChanged()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnClanTypeChangedListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_TYPE_CHANGED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnClanTypeChangedUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnClanTypeChanged:
    def ClansRemoteEventListenerOnClanTypeChanged(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnClanTypeChangedListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnAssignedLeaderRoleEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_ASSIGNED_LEADER_ROLE_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnAssignedLeaderRoleEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnAssignedLeaderRoleEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_ASSIGNED_LEADER_ROLE_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnAssignedLeaderRoleEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnAssignedLeaderRoleEvent:
    def ClansRemoteEventListenerOnAssignedLeaderRoleEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnAssignedLeaderRoleEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnClanTagAndNameChangedUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_TAG_AND_NAME_CHANGED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnClanTagAndNameChanged()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnClanTagAndNameChangedListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_TAG_AND_NAME_CHANGED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnClanTagAndNameChangedUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnClanTagAndNameChanged:
    def ClansRemoteEventListenerOnClanTagAndNameChanged(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnClanTagAndNameChangedListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnLeftFromClanUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_LEFT_FROM_CLAN
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnLeftFromClan()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnLeftFromClanListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_LEFT_FROM_CLAN
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnLeftFromClanUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnLeftFromClan:
    def ClansRemoteEventListenerOnLeftFromClan(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnLeftFromClanListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnClanMemberDeclinedRequestEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_MEMBER_DECLINED_REQUEST_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnClanMemberDeclinedRequestEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnClanMemberDeclinedRequestEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_MEMBER_DECLINED_REQUEST_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnClanMemberDeclinedRequestEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnClanMemberDeclinedRequestEvent:
    def ClansRemoteEventListenerOnClanMemberDeclinedRequestEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnClanMemberDeclinedRequestEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnMemberJoinedToClanUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_MEMBER_JOINED_TO_CLAN
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnMemberJoinedToClanEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnMemberJoinedToClanListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_MEMBER_JOINED_TO_CLAN
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnMemberJoinedToClanUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnMemberJoinedToClan:
    def ClansRemoteEventListenerOnMemberJoinedToClan(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnMemberJoinedToClanListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnJoinRequestTakenUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_JOIN_REQUEST_TAKEN
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnJoinRequestTakenEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnJoinRequestTakenListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_JOIN_REQUEST_TAKEN
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnJoinRequestTakenUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnJoinRequestTaken:
    def ClansRemoteEventListenerOnJoinRequestTaken(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnJoinRequestTakenListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnInviteRequestDeclinedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_INVITE_REQUEST_DECLINED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnInviteRequestDeclinedEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnInviteRequestDeclinedEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_INVITE_REQUEST_DECLINED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnInviteRequestDeclinedEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnInviteRequestDeclinedEvent:
    def ClansRemoteEventListenerOnInviteRequestDeclinedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnInviteRequestDeclinedEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnInviteRequestCancelledEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_INVITE_REQUEST_CANCELLED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnInviteRequestCancelledEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnInviteRequestCancelledEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_INVITE_REQUEST_CANCELLED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnInviteRequestCancelledEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnInviteRequestCancelledEvent:
    def ClansRemoteEventListenerOnInviteRequestCancelledEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnInviteRequestCancelledEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnAssignedRoleEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_ASSIGNED_ROLE_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnAssignedRoleEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnAssignedRoleEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_ASSIGNED_ROLE_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnAssignedRoleEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnAssignedRoleEvent:
    def ClansRemoteEventListenerOnAssignedRoleEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnAssignedRoleEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnPlayerAvatarChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_PLAYER_AVATAR_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnPlayerAvatarChangedEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnPlayerAvatarChangedEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_PLAYER_AVATAR_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnPlayerAvatarChangedEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnPlayerAvatarChangedEvent:
    def ClansRemoteEventListenerOnPlayerAvatarChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnPlayerAvatarChangedEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnOnlineStatusChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_ONLINE_STATUS_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnOnlineStatusChangedEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnOnlineStatusChangedEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_ONLINE_STATUS_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnOnlineStatusChangedEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnOnlineStatusChangedEvent:
    def ClansRemoteEventListenerOnOnlineStatusChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnOnlineStatusChangedEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnPlayerNameChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_PLAYER_NAME_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnPlayerNameChangedEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnPlayerNameChangedEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_PLAYER_NAME_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnPlayerNameChangedEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnPlayerNameChangedEvent:
    def ClansRemoteEventListenerOnPlayerNameChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnPlayerNameChangedEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnKickedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_KICKED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnKickedEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnKickedEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_KICKED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnKickedEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnKickedEvent:
    def ClansRemoteEventListenerOnKickedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnKickedEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnClanDescriptionChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_DESCRIPTION_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnClanDescriptionChangedEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnClanDescriptionChangedEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_DESCRIPTION_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnClanDescriptionChangedEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnClanDescriptionChangedEvent:
    def ClansRemoteEventListenerOnClanDescriptionChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnClanDescriptionChangedEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnPlayerAttributesChangedUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_PLAYER_ATTRIBUTES_CHANGED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnPlayerAttributesChanged()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnPlayerAttributesChangedListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_PLAYER_ATTRIBUTES_CHANGED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnPlayerAttributesChangedUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnPlayerAttributesChanged:
    def ClansRemoteEventListenerOnPlayerAttributesChanged(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnPlayerAttributesChangedListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnClanAvatarChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_AVATAR_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnClanAvatarChangedEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnClanAvatarChangedEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_CLAN_AVATAR_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnClanAvatarChangedEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnClanAvatarChangedEvent:
    def ClansRemoteEventListenerOnClanAvatarChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnClanAvatarChangedEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnInvitedToClanEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_INVITED_TO_CLAN_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnInvitedToClanEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnInvitedToClanEventListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_INVITED_TO_CLAN_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnInvitedToClanEventUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnInvitedToClanEvent:
    def ClansRemoteEventListenerOnInvitedToClanEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnInvitedToClanEventListener(func))
            return func
        return decorator

class ClansRemoteEventListenerOnJoinedToClanUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_JOINED_TO_CLAN
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnJoinedToClanEvent()
        self.data.ParseFromString(payload)
class ClansRemoteEventListenerOnJoinedToClanListener(Listener):
    event = GeneratedEvent.CLANS_REMOTE_EVENT_LISTENER_ON_JOINED_TO_CLAN
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClansRemoteEventListenerOnJoinedToClanUpdate):
        await self._callback(client, update)
class ClansRemoteEventListenerOnJoinedToClan:
    def ClansRemoteEventListenerOnJoinedToClan(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClansRemoteEventListenerOnJoinedToClanListener(func))
            return func
        return decorator

class InventoryRemoteEventListenerOnInventoryChangedUpdate(GeneratedUpdate):
    event = GeneratedEvent.INVENTORY_REMOTE_EVENT_LISTENER_ON_INVENTORY_CHANGED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnInventoryChangedEvent()
        self.data.ParseFromString(payload)
class InventoryRemoteEventListenerOnInventoryChangedListener(Listener):
    event = GeneratedEvent.INVENTORY_REMOTE_EVENT_LISTENER_ON_INVENTORY_CHANGED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: InventoryRemoteEventListenerOnInventoryChangedUpdate):
        await self._callback(client, update)
class InventoryRemoteEventListenerOnInventoryChanged:
    def InventoryRemoteEventListenerOnInventoryChanged(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(InventoryRemoteEventListenerOnInventoryChangedListener(func))
            return func
        return decorator

class InventoryRemoteEventListenerOnCouponActivatedUpdate(GeneratedUpdate):
    event = GeneratedEvent.INVENTORY_REMOTE_EVENT_LISTENER_ON_COUPON_ACTIVATED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnCouponActivatedEvent()
        self.data.ParseFromString(payload)
class InventoryRemoteEventListenerOnCouponActivatedListener(Listener):
    event = GeneratedEvent.INVENTORY_REMOTE_EVENT_LISTENER_ON_COUPON_ACTIVATED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: InventoryRemoteEventListenerOnCouponActivatedUpdate):
        await self._callback(client, update)
class InventoryRemoteEventListenerOnCouponActivated:
    def InventoryRemoteEventListenerOnCouponActivated(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(InventoryRemoteEventListenerOnCouponActivatedListener(func))
            return func
        return decorator

class MatchesRemoteEventListenerOnMatchFinishedUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHES_REMOTE_EVENT_LISTENER_ON_MATCH_FINISHED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnMatchFinishedEvent()
        self.data.ParseFromString(payload)
class MatchesRemoteEventListenerOnMatchFinishedListener(Listener):
    event = GeneratedEvent.MATCHES_REMOTE_EVENT_LISTENER_ON_MATCH_FINISHED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchesRemoteEventListenerOnMatchFinishedUpdate):
        await self._callback(client, update)
class MatchesRemoteEventListenerOnMatchFinished:
    def MatchesRemoteEventListenerOnMatchFinished(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchesRemoteEventListenerOnMatchFinishedListener(func))
            return func
        return decorator

class FriendsRemoteEventListenerOnFriendNameChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_NAME_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnFriendNameChangedEvent()
        self.data.ParseFromString(payload)
class FriendsRemoteEventListenerOnFriendNameChangedEventListener(Listener):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_NAME_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: FriendsRemoteEventListenerOnFriendNameChangedEventUpdate):
        await self._callback(client, update)
class FriendsRemoteEventListenerOnFriendNameChangedEvent:
    def FriendsRemoteEventListenerOnFriendNameChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(FriendsRemoteEventListenerOnFriendNameChangedEventListener(func))
            return func
        return decorator

class FriendsRemoteEventListenerOnPlayerStatusChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_PLAYER_STATUS_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnPlayerStatusChangedEvent()
        self.data.ParseFromString(payload)
class FriendsRemoteEventListenerOnPlayerStatusChangedEventListener(Listener):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_PLAYER_STATUS_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: FriendsRemoteEventListenerOnPlayerStatusChangedEventUpdate):
        await self._callback(client, update)
class FriendsRemoteEventListenerOnPlayerStatusChangedEvent:
    def FriendsRemoteEventListenerOnPlayerStatusChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(FriendsRemoteEventListenerOnPlayerStatusChangedEventListener(func))
            return func
        return decorator

class FriendsRemoteEventListenerOnPlayerAttributesChangedUpdate(GeneratedUpdate):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_PLAYER_ATTRIBUTES_CHANGED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnPlayerAttributesChanged()
        self.data.ParseFromString(payload)
class FriendsRemoteEventListenerOnPlayerAttributesChangedListener(Listener):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_PLAYER_ATTRIBUTES_CHANGED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: FriendsRemoteEventListenerOnPlayerAttributesChangedUpdate):
        await self._callback(client, update)
class FriendsRemoteEventListenerOnPlayerAttributesChanged:
    def FriendsRemoteEventListenerOnPlayerAttributesChanged(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(FriendsRemoteEventListenerOnPlayerAttributesChangedListener(func))
            return func
        return decorator

class FriendsRemoteEventListenerOnFriendRemovedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_REMOVED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnFriendRemovedEvent()
        self.data.ParseFromString(payload)
class FriendsRemoteEventListenerOnFriendRemovedEventListener(Listener):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_REMOVED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: FriendsRemoteEventListenerOnFriendRemovedEventUpdate):
        await self._callback(client, update)
class FriendsRemoteEventListenerOnFriendRemovedEvent:
    def FriendsRemoteEventListenerOnFriendRemovedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(FriendsRemoteEventListenerOnFriendRemovedEventListener(func))
            return func
        return decorator

class FriendsRemoteEventListenerOnRevokeFriendshipRequestEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_REVOKE_FRIENDSHIP_REQUEST_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnRevokeFriendshipRequestEvent()
        self.data.ParseFromString(payload)
class FriendsRemoteEventListenerOnRevokeFriendshipRequestEventListener(Listener):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_REVOKE_FRIENDSHIP_REQUEST_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: FriendsRemoteEventListenerOnRevokeFriendshipRequestEventUpdate):
        await self._callback(client, update)
class FriendsRemoteEventListenerOnRevokeFriendshipRequestEvent:
    def FriendsRemoteEventListenerOnRevokeFriendshipRequestEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(FriendsRemoteEventListenerOnRevokeFriendshipRequestEventListener(func))
            return func
        return decorator

class FriendsRemoteEventListenerOnFriendAddedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_ADDED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnFriendAddedEvent()
        self.data.ParseFromString(payload)
class FriendsRemoteEventListenerOnFriendAddedEventListener(Listener):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_ADDED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: FriendsRemoteEventListenerOnFriendAddedEventUpdate):
        await self._callback(client, update)
class FriendsRemoteEventListenerOnFriendAddedEvent:
    def FriendsRemoteEventListenerOnFriendAddedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(FriendsRemoteEventListenerOnFriendAddedEventListener(func))
            return func
        return decorator

class FriendsRemoteEventListenerOnNewFriendshipRequestEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_NEW_FRIENDSHIP_REQUEST_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnNewFriendshipRequestEvent()
        self.data.ParseFromString(payload)
class FriendsRemoteEventListenerOnNewFriendshipRequestEventListener(Listener):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_NEW_FRIENDSHIP_REQUEST_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: FriendsRemoteEventListenerOnNewFriendshipRequestEventUpdate):
        await self._callback(client, update)
class FriendsRemoteEventListenerOnNewFriendshipRequestEvent:
    def FriendsRemoteEventListenerOnNewFriendshipRequestEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(FriendsRemoteEventListenerOnNewFriendshipRequestEventListener(func))
            return func
        return decorator

class FriendsRemoteEventListenerOnFriendAvatarChangedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_AVATAR_CHANGED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnFriendAvatarChangedEvent()
        self.data.ParseFromString(payload)
class FriendsRemoteEventListenerOnFriendAvatarChangedEventListener(Listener):
    event = GeneratedEvent.FRIENDS_REMOTE_EVENT_LISTENER_ON_FRIEND_AVATAR_CHANGED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: FriendsRemoteEventListenerOnFriendAvatarChangedEventUpdate):
        await self._callback(client, update)
class FriendsRemoteEventListenerOnFriendAvatarChangedEvent:
    def FriendsRemoteEventListenerOnFriendAvatarChangedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(FriendsRemoteEventListenerOnFriendAvatarChangedEventListener(func))
            return func
        return decorator

class MessagesRemoteEventListenerOnMsgFromFriendEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.MESSAGES_REMOTE_EVENT_LISTENER_ON_MSG_FROM_FRIEND_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnMsgFromFriendEvent()
        self.data.ParseFromString(payload)
class MessagesRemoteEventListenerOnMsgFromFriendEventListener(Listener):
    event = GeneratedEvent.MESSAGES_REMOTE_EVENT_LISTENER_ON_MSG_FROM_FRIEND_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MessagesRemoteEventListenerOnMsgFromFriendEventUpdate):
        await self._callback(client, update)
class MessagesRemoteEventListenerOnMsgFromFriendEvent:
    def MessagesRemoteEventListenerOnMsgFromFriendEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MessagesRemoteEventListenerOnMsgFromFriendEventListener(func))
            return func
        return decorator

class ClanStatsRemoteEventListenerOnClanStatsUpdatedUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLAN_STATS_REMOTE_EVENT_LISTENER_ON_CLAN_STATS_UPDATED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnClanStatsUpdatedEvent()
        self.data.ParseFromString(payload)
class ClanStatsRemoteEventListenerOnClanStatsUpdatedListener(Listener):
    event = GeneratedEvent.CLAN_STATS_REMOTE_EVENT_LISTENER_ON_CLAN_STATS_UPDATED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClanStatsRemoteEventListenerOnClanStatsUpdatedUpdate):
        await self._callback(client, update)
class ClanStatsRemoteEventListenerOnClanStatsUpdated:
    def ClanStatsRemoteEventListenerOnClanStatsUpdated(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClanStatsRemoteEventListenerOnClanStatsUpdatedListener(func))
            return func
        return decorator

class GameEventRemoteEventListenerOnGamePassChangedUpdate(GeneratedUpdate):
    event = GeneratedEvent.GAME_EVENT_REMOTE_EVENT_LISTENER_ON_GAME_PASS_CHANGED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnGamePassChangedEvent()
        self.data.ParseFromString(payload)
class GameEventRemoteEventListenerOnGamePassChangedListener(Listener):
    event = GeneratedEvent.GAME_EVENT_REMOTE_EVENT_LISTENER_ON_GAME_PASS_CHANGED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: GameEventRemoteEventListenerOnGamePassChangedUpdate):
        await self._callback(client, update)
class GameEventRemoteEventListenerOnGamePassChanged:
    def GameEventRemoteEventListenerOnGamePassChanged(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(GameEventRemoteEventListenerOnGamePassChangedListener(func))
            return func
        return decorator

class GameEventRemoteEventListenerOnProgressGameEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.GAME_EVENT_REMOTE_EVENT_LISTENER_ON_PROGRESS_GAME_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnProgressGameEvent()
        self.data.ParseFromString(payload)
class GameEventRemoteEventListenerOnProgressGameEventListener(Listener):
    event = GeneratedEvent.GAME_EVENT_REMOTE_EVENT_LISTENER_ON_PROGRESS_GAME_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: GameEventRemoteEventListenerOnProgressGameEventUpdate):
        await self._callback(client, update)
class GameEventRemoteEventListenerOnProgressGameEvent:
    def GameEventRemoteEventListenerOnProgressGameEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(GameEventRemoteEventListenerOnProgressGameEventListener(func))
            return func
        return decorator

class GameEventRemoteEventListenerOnProgressChallengeEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.GAME_EVENT_REMOTE_EVENT_LISTENER_ON_PROGRESS_CHALLENGE_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnProgressChallengeEvent()
        self.data.ParseFromString(payload)
class GameEventRemoteEventListenerOnProgressChallengeEventListener(Listener):
    event = GeneratedEvent.GAME_EVENT_REMOTE_EVENT_LISTENER_ON_PROGRESS_CHALLENGE_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: GameEventRemoteEventListenerOnProgressChallengeEventUpdate):
        await self._callback(client, update)
class GameEventRemoteEventListenerOnProgressChallengeEvent:
    def GameEventRemoteEventListenerOnProgressChallengeEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(GameEventRemoteEventListenerOnProgressChallengeEventListener(func))
            return func
        return decorator

class ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.CLAN_MESSAGES_REMOTE_EVENT_LISTENER_ON_INCOMING_CLAN_CHAT_MESSAGE_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnIncomingClanChatMessageEvent()
        self.data.ParseFromString(payload)
class ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEventListener(Listener):
    event = GeneratedEvent.CLAN_MESSAGES_REMOTE_EVENT_LISTENER_ON_INCOMING_CLAN_CHAT_MESSAGE_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEventUpdate):
        await self._callback(client, update)
class ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEvent:
    def ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEventListener(func))
            return func
        return decorator

class AdsRemoteEventListenerOnAdRewardEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.ADS_REMOTE_EVENT_LISTENER_ON_AD_REWARD_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnAdRewardEvent()
        self.data.ParseFromString(payload)
class AdsRemoteEventListenerOnAdRewardEventListener(Listener):
    event = GeneratedEvent.ADS_REMOTE_EVENT_LISTENER_ON_AD_REWARD_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: AdsRemoteEventListenerOnAdRewardEventUpdate):
        await self._callback(client, update)
class AdsRemoteEventListenerOnAdRewardEvent:
    def AdsRemoteEventListenerOnAdRewardEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(AdsRemoteEventListenerOnAdRewardEventListener(func))
            return func
        return decorator

class PlayerStatsRemoteEventListenerOnStatsUpdatedEventUpdate(GeneratedUpdate):
    event = GeneratedEvent.PLAYER_STATS_REMOTE_EVENT_LISTENER_ON_STATS_UPDATED_EVENT
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = OnStatsUpdatedEvent()
        self.data.ParseFromString(payload)
class PlayerStatsRemoteEventListenerOnStatsUpdatedEventListener(Listener):
    event = GeneratedEvent.PLAYER_STATS_REMOTE_EVENT_LISTENER_ON_STATS_UPDATED_EVENT
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: PlayerStatsRemoteEventListenerOnStatsUpdatedEventUpdate):
        await self._callback(client, update)
class PlayerStatsRemoteEventListenerOnStatsUpdatedEvent:
    def PlayerStatsRemoteEventListenerOnStatsUpdatedEvent(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(PlayerStatsRemoteEventListenerOnStatsUpdatedEventListener(func))
            return func
        return decorator

class MatchmakingRemoteListenerOnMatchmakingProgressUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_LISTENER_ON_MATCHMAKING_PROGRESS
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = EEBEGEFGBEBEGEH()
        self.data.ParseFromString(payload)
class MatchmakingRemoteListenerOnMatchmakingProgressListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_LISTENER_ON_MATCHMAKING_PROGRESS
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteListenerOnMatchmakingProgressUpdate):
        await self._callback(client, update)
class MatchmakingRemoteListenerOnMatchmakingProgress:
    def MatchmakingRemoteListenerOnMatchmakingProgress(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteListenerOnMatchmakingProgressListener(func))
            return func
        return decorator

class MatchmakingRemoteListenerOnPlayersConfirmedUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_LISTENER_ON_PLAYERS_CONFIRMED
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = BEBFABBECGCAFCH()
        self.data.ParseFromString(payload)
class MatchmakingRemoteListenerOnPlayersConfirmedListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_LISTENER_ON_PLAYERS_CONFIRMED
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteListenerOnPlayersConfirmedUpdate):
        await self._callback(client, update)
class MatchmakingRemoteListenerOnPlayersConfirmed:
    def MatchmakingRemoteListenerOnPlayersConfirmed(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteListenerOnPlayersConfirmedListener(func))
            return func
        return decorator

class MatchmakingRemoteListenerOnMatchmakingDoneUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_LISTENER_ON_MATCHMAKING_DONE
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = AGCBFBCDCGGECGA()
        self.data.ParseFromString(payload)
class MatchmakingRemoteListenerOnMatchmakingDoneListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_LISTENER_ON_MATCHMAKING_DONE
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteListenerOnMatchmakingDoneUpdate):
        await self._callback(client, update)
class MatchmakingRemoteListenerOnMatchmakingDone:
    def MatchmakingRemoteListenerOnMatchmakingDone(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteListenerOnMatchmakingDoneListener(func))
            return func
        return decorator

class MatchmakingRemoteListenerOnMatchmakingFailUpdate(GeneratedUpdate):
    event = GeneratedEvent.MATCHMAKING_REMOTE_LISTENER_ON_MATCHMAKING_FAIL
    def __init__(self, payload: bytes):
        super().__init__()
        self.data = CFCGDGEAEHDEABF()
        self.data.ParseFromString(payload)
class MatchmakingRemoteListenerOnMatchmakingFailListener(Listener):
    event = GeneratedEvent.MATCHMAKING_REMOTE_LISTENER_ON_MATCHMAKING_FAIL
    def __init__(self, callback):
        super().__init__(callback)
    async def call(self, client, update: MatchmakingRemoteListenerOnMatchmakingFailUpdate):
        await self._callback(client, update)
class MatchmakingRemoteListenerOnMatchmakingFail:
    def MatchmakingRemoteListenerOnMatchmakingFail(self) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._dp.add_listener(MatchmakingRemoteListenerOnMatchmakingFailListener(func))
            return func
        return decorator

class GeneratedEvents(MarketplaceRemoteEventListenerOnPlayerRequestOpened,MarketplaceRemoteEventListenerOnTradeUpdated,MarketplaceRemoteEventListenerOnTradeRequestOpened,MarketplaceRemoteEventListenerOnPlayerRequestClosed,MarketplaceRemoteEventListenerOnTradeRequestClosed,SystemMessagesRemoteEventListenerOnSystemMessageReceived,MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEvent,MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEvent,MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEvent,MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEvent,MatchmakingRemoteEventListenerOnLobbyDataChangedEvent,MatchmakingRemoteEventListenerOnLobbyTypeChangedEvent,MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEvent,MatchmakingRemoteEventListenerOnLobbyJoinableChangedEvent,MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEvent,MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEvent,MatchmakingRemoteEventListenerOnLobbyChatMessageEvent,MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEvent,MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEvent,MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEvent,MatchmakingRemoteEventListenerOnLobbyOwnerChangedEvent,MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEvent,MatchmakingRemoteEventListenerOnLobbyGameServerChangedEvent,MatchmakingRemoteEventListenerOnLobbyNameChangedEvent,MatchmakingRemoteEventListenerOnPlayerLeftLobbyEvent,MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEvent,MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEvent,InAppsRemoteEventListenerOnInAppEvent,ClansRemoteEventListenerOnClanMembersCountIncreased,ClansRemoteEventListenerOnReadClosedInviteRequestEvent,ClansRemoteEventListenerOnJoinRequestDeclinedEvent,ClansRemoteEventListenerOnKickedMember,ClansRemoteEventListenerOnJoinRequestCancelledEvent,ClansRemoteEventListenerOnClanTypeChanged,ClansRemoteEventListenerOnAssignedLeaderRoleEvent,ClansRemoteEventListenerOnClanTagAndNameChanged,ClansRemoteEventListenerOnLeftFromClan,ClansRemoteEventListenerOnClanMemberDeclinedRequestEvent,ClansRemoteEventListenerOnMemberJoinedToClan,ClansRemoteEventListenerOnJoinRequestTaken,ClansRemoteEventListenerOnInviteRequestDeclinedEvent,ClansRemoteEventListenerOnInviteRequestCancelledEvent,ClansRemoteEventListenerOnAssignedRoleEvent,ClansRemoteEventListenerOnPlayerAvatarChangedEvent,ClansRemoteEventListenerOnOnlineStatusChangedEvent,ClansRemoteEventListenerOnPlayerNameChangedEvent,ClansRemoteEventListenerOnKickedEvent,ClansRemoteEventListenerOnClanDescriptionChangedEvent,ClansRemoteEventListenerOnPlayerAttributesChanged,ClansRemoteEventListenerOnClanAvatarChangedEvent,ClansRemoteEventListenerOnInvitedToClanEvent,ClansRemoteEventListenerOnJoinedToClan,InventoryRemoteEventListenerOnInventoryChanged,InventoryRemoteEventListenerOnCouponActivated,MatchesRemoteEventListenerOnMatchFinished,FriendsRemoteEventListenerOnFriendNameChangedEvent,FriendsRemoteEventListenerOnPlayerStatusChangedEvent,FriendsRemoteEventListenerOnPlayerAttributesChanged,FriendsRemoteEventListenerOnFriendRemovedEvent,FriendsRemoteEventListenerOnRevokeFriendshipRequestEvent,FriendsRemoteEventListenerOnFriendAddedEvent,FriendsRemoteEventListenerOnNewFriendshipRequestEvent,FriendsRemoteEventListenerOnFriendAvatarChangedEvent,MessagesRemoteEventListenerOnMsgFromFriendEvent,ClanStatsRemoteEventListenerOnClanStatsUpdated,GameEventRemoteEventListenerOnGamePassChanged,GameEventRemoteEventListenerOnProgressGameEvent,GameEventRemoteEventListenerOnProgressChallengeEvent,ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEvent,AdsRemoteEventListenerOnAdRewardEvent,PlayerStatsRemoteEventListenerOnStatsUpdatedEvent,MatchmakingRemoteListenerOnMatchmakingProgress,MatchmakingRemoteListenerOnPlayersConfirmed,MatchmakingRemoteListenerOnMatchmakingDone,MatchmakingRemoteListenerOnMatchmakingFail,): pass

GENERATED_UPDATES = {5: [MarketplaceRemoteEventListenerOnPlayerRequestOpenedUpdate],1: [MarketplaceRemoteEventListenerOnTradeUpdatedUpdate,MatchmakingRemoteListenerOnMatchmakingDoneUpdate],3: [MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate,MatchmakingRemoteListenerOnPlayersConfirmedUpdate],4: [MarketplaceRemoteEventListenerOnPlayerRequestClosedUpdate,MatchmakingRemoteListenerOnMatchmakingFailUpdate],2: [MarketplaceRemoteEventListenerOnTradeRequestClosedUpdate,MatchmakingRemoteListenerOnMatchmakingProgressUpdate],126: [SystemMessagesRemoteEventListenerOnSystemMessageReceivedUpdate],72: [MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEventUpdate],77: [MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEventUpdate],68: [MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEventUpdate],67: [MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEventUpdate],61: [MatchmakingRemoteEventListenerOnLobbyDataChangedEventUpdate],70: [MatchmakingRemoteEventListenerOnLobbyTypeChangedEventUpdate],65: [MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEventUpdate],62: [MatchmakingRemoteEventListenerOnLobbyJoinableChangedEventUpdate],66: [MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEventUpdate],75: [MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEventUpdate],64: [MatchmakingRemoteEventListenerOnLobbyChatMessageEventUpdate],74: [MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEventUpdate],78: [MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEventUpdate],79: [MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEventUpdate],73: [MatchmakingRemoteEventListenerOnLobbyOwnerChangedEventUpdate],63: [MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEventUpdate],80: [MatchmakingRemoteEventListenerOnLobbyGameServerChangedEventUpdate],81: [MatchmakingRemoteEventListenerOnLobbyNameChangedEventUpdate],69: [MatchmakingRemoteEventListenerOnPlayerLeftLobbyEventUpdate],76: [MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEventUpdate],71: [MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEventUpdate],119: [InAppsRemoteEventListenerOnInAppEventUpdate],53: [ClansRemoteEventListenerOnClanMembersCountIncreasedUpdate],38: [ClansRemoteEventListenerOnReadClosedInviteRequestEventUpdate],45: [ClansRemoteEventListenerOnJoinRequestDeclinedEventUpdate],42: [ClansRemoteEventListenerOnKickedMemberUpdate],37: [ClansRemoteEventListenerOnJoinRequestCancelledEventUpdate],48: [ClansRemoteEventListenerOnClanTypeChangedUpdate],47: [ClansRemoteEventListenerOnAssignedLeaderRoleEventUpdate],52: [ClansRemoteEventListenerOnClanTagAndNameChangedUpdate],46: [ClansRemoteEventListenerOnLeftFromClanUpdate],41: [ClansRemoteEventListenerOnClanMemberDeclinedRequestEventUpdate],35: [ClansRemoteEventListenerOnMemberJoinedToClanUpdate],33: [ClansRemoteEventListenerOnJoinRequestTakenUpdate],40: [ClansRemoteEventListenerOnInviteRequestDeclinedEventUpdate],51: [ClansRemoteEventListenerOnInviteRequestCancelledEventUpdate],43: [ClansRemoteEventListenerOnAssignedRoleEventUpdate],32: [ClansRemoteEventListenerOnPlayerAvatarChangedEventUpdate],31: [ClansRemoteEventListenerOnOnlineStatusChangedEventUpdate],34: [ClansRemoteEventListenerOnPlayerNameChangedEventUpdate],50: [ClansRemoteEventListenerOnKickedEventUpdate],54: [ClansRemoteEventListenerOnClanDescriptionChangedEventUpdate],36: [ClansRemoteEventListenerOnPlayerAttributesChangedUpdate],49: [ClansRemoteEventListenerOnClanAvatarChangedEventUpdate],44: [ClansRemoteEventListenerOnInvitedToClanEventUpdate],39: [ClansRemoteEventListenerOnJoinedToClanUpdate],111: [InventoryRemoteEventListenerOnInventoryChangedUpdate],112: [InventoryRemoteEventListenerOnCouponActivatedUpdate],95: [MatchesRemoteEventListenerOnMatchFinishedUpdate],14: [FriendsRemoteEventListenerOnFriendNameChangedEventUpdate],11: [FriendsRemoteEventListenerOnPlayerStatusChangedEventUpdate],16: [FriendsRemoteEventListenerOnPlayerAttributesChangedUpdate],17: [FriendsRemoteEventListenerOnFriendRemovedEventUpdate],18: [FriendsRemoteEventListenerOnRevokeFriendshipRequestEventUpdate],15: [FriendsRemoteEventListenerOnFriendAddedEventUpdate],13: [FriendsRemoteEventListenerOnNewFriendshipRequestEventUpdate],12: [FriendsRemoteEventListenerOnFriendAvatarChangedEventUpdate],121: [MessagesRemoteEventListenerOnMsgFromFriendEventUpdate],59: [ClanStatsRemoteEventListenerOnClanStatsUpdatedUpdate],107: [GameEventRemoteEventListenerOnGamePassChangedUpdate],106: [GameEventRemoteEventListenerOnProgressGameEventUpdate],108: [GameEventRemoteEventListenerOnProgressChallengeEventUpdate],58: [ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEventUpdate],116: [AdsRemoteEventListenerOnAdRewardEventUpdate],101: [PlayerStatsRemoteEventListenerOnStatsUpdatedEventUpdate],}
UPDATE_INDEX = {5: 0, 1: 0, 3: 0, 4: 0, 2: 0, 126: 0, 72: 0, 77: 0, 68: 0, 67: 0, 61: 0, 70: 0, 65: 0, 62: 0, 66: 0, 75: 0, 64: 0, 74: 0, 78: 0, 79: 0, 73: 0, 63: 0, 80: 0, 81: 0, 69: 0, 76: 0, 71: 0, 119: 0, 53: 0, 38: 0, 45: 0, 42: 0, 37: 0, 48: 0, 47: 0, 52: 0, 46: 0, 41: 0, 35: 0, 33: 0, 40: 0, 51: 0, 43: 0, 32: 0, 31: 0, 34: 0, 50: 0, 54: 0, 36: 0, 49: 0, 44: 0, 39: 0, 111: 0, 112: 0, 95: 0, 14: 0, 11: 0, 16: 0, 17: 0, 18: 0, 15: 0, 13: 0, 12: 0, 121: 0, 59: 0, 107: 0, 106: 0, 108: 0, 58: 0, 116: 0, 101: 0, }