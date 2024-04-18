from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DigitalAssistantOCRResponse(_message.Message):
    __slots__ = ("Text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    Text: str
    def __init__(self, Text: _Optional[str] = ...) -> None: ...

class DigitalAssistantOCRRequest(_message.Message):
    __slots__ = ("Image", "PDF")
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PDF_FIELD_NUMBER: _ClassVar[int]
    Image: bytes
    PDF: bytes
    def __init__(self, Image: _Optional[bytes] = ..., PDF: _Optional[bytes] = ...) -> None: ...
