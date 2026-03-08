from .hello import HelloRemoteService
from .bolt import BoltRemoteService
from .handshake import HandshakeRemoteService
from .player import PlayerRemoteService


class Services(
    HelloRemoteService,
    BoltRemoteService,
    HandshakeRemoteService,
    PlayerRemoteService
): 
    def __init__(self):
        super().__init__()

__all__ = [
    "Services"
]