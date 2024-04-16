from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DigitalAssistantEntryPointResponse(_message.Message):
    __slots__ = ("Text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    Text: str
    def __init__(self, Text: _Optional[str] = ...) -> None: ...

class DigitalAssistantEntryPointRequest(_message.Message):
    __slots__ = ("Text", "OuterContext", "Image", "PDF")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    OUTERCONTEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PDF_FIELD_NUMBER: _ClassVar[int]
    Text: str
    OuterContext: OuterContextItem
    Image: bytes
    PDF: bytes
    def __init__(self, Text: _Optional[str] = ..., OuterContext: _Optional[_Union[OuterContextItem, _Mapping]] = ..., Image: _Optional[bytes] = ..., PDF: _Optional[bytes] = ...) -> None: ...

class OuterContextItem(_message.Message):
    __slots__ = ("Sex", "Age", "UserId", "SessionId")
    SEX_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    Sex: bool
    Age: int
    UserId: int
    SessionId: int
    def __init__(self, Sex: bool = ..., Age: _Optional[int] = ..., UserId: _Optional[int] = ..., SessionId: _Optional[int] = ...) -> None: ...
