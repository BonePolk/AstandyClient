from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerHandshake(_message.Message):
    __slots__ = ["apiKey", "gameId", "version"]
    APIKEY_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    apiKey: str
    gameId: str
    version: str
    def __init__(self, gameId: _Optional[str] = ..., apiKey: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class ServerHandshakeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ServerLogoutRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ServerLogoutResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
