from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
FLOAT: StatDefType
INT: StatDefType
LONG: StatDefType

class StatDefType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
