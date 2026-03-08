from Astandy.listener import Listener
from Astandy.enums.events import BaseEvent


class OnConnect(Listener):
    event = BaseEvent.CONNECT