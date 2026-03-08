import asyncio
from collections import defaultdict

from .types.update import Update 
from .listener import Listener
from .enums.events import BaseEvent

class Dispatcher():
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.listeners: dict[int, Listener] = defaultdict(list[Listener])

    def add_listener(self, listener: Listener):
        self.listeners[listener.event].append(listener)

    async def call_listeners(self, update: Update):
        for listener in self.listeners[update.event]:
            asyncio.create_task(listener.call(self._client, update))