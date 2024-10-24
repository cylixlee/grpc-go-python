from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("name", "greet")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GREET_FIELD_NUMBER: _ClassVar[int]
    name: str
    greet: str
    def __init__(self, name: _Optional[str] = ..., greet: _Optional[str] = ...) -> None: ...
