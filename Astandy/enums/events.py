from enum import Enum

class Event(Enum):
    pass

class BaseEvent(Event):
    UNKNOWN = -1
    CONNECT = 0
    AUTHENTICATED = 1