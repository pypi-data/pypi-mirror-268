from com.terraquantum.javalibs.logging.v1 import logging_extensions_pb2 as _logging_extensions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetInvitationRequest(_message.Message):
    __slots__ = ("id", "invitation_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    INVITATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    invitation_token: str
    def __init__(self, id: _Optional[str] = ..., invitation_token: _Optional[str] = ...) -> None: ...
