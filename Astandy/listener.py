from collections.abc import Callable
from Astandy.types.update import Update
from Astandy.enums.events import BaseEvent

class Listener:
    event: BaseEvent = BaseEvent.UNKNOWN

    def __init__(self, callback: Callable):
        self._callback = callback

    async def call(self, client, update: Update):
        await self._callback(client, update)