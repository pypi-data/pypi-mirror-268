from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateImportPlanRequest(_message.Message):
    __slots__ = ('search_string', 'max_rows')
    SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_FIELD_NUMBER: _ClassVar[int]
    search_string: str
    max_rows: int
    def __init__(self, search_string: _Optional[str] = ..., max_rows: _Optional[int] = ...) -> None: ...

class CreateImportPlanResponse(_message.Message):
    __slots__ = ('job_id',)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class ApplyImportPlanRequest(_message.Message):
    __slots__ = ('plan_yaml', 'branch', 'table')
    PLAN_YAML_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    plan_yaml: str
    branch: str
    table: str
    def __init__(
        self, plan_yaml: _Optional[str] = ..., branch: _Optional[str] = ..., table: _Optional[str] = ...
    ) -> None: ...

class ApplyImportPlanResponse(_message.Message):
    __slots__ = ('status', 'msg')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    status: str
    msg: str
    def __init__(self, status: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...
