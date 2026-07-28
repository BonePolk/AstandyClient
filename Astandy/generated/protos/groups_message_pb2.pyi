import player_message_pb2 as _player_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateGroupRequest(_message.Message):
    __slots__ = ["friendIds"]
    FRIENDIDS_FIELD_NUMBER: _ClassVar[int]
    friendIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, friendIds: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateGroupResponse(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: Group
    def __init__(self, group: _Optional[_Union[Group, _Mapping]] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ["avatarId", "id", "name", "players"]
    AVATARID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    avatarId: str
    id: str
    name: str
    players: _containers.RepeatedCompositeFieldContainer[_player_message_pb2.Player]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., avatarId: _Optional[str] = ..., players: _Optional[_Iterable[_Union[_player_message_pb2.Player, _Mapping]]] = ...) -> None: ...

class JoinGroupRequest(_message.Message):
    __slots__ = ["groupId"]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    groupId: str
    def __init__(self, groupId: _Optional[str] = ...) -> None: ...

class JoinGroupResponse(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: Group
    def __init__(self, group: _Optional[_Union[Group, _Mapping]] = ...) -> None: ...

class LeaveGroupRequest(_message.Message):
    __slots__ = ["groupId"]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    groupId: str
    def __init__(self, groupId: _Optional[str] = ...) -> None: ...

class LeaveGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
