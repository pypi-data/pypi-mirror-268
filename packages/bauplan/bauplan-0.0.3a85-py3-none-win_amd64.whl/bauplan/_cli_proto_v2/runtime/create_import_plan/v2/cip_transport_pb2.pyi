from bauplan._proto.runtime.runtime_shared.v2 import config_pb2 as _config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateImportPlanRequest(_message.Message):
    __slots__ = ('code_intelligence_instructions', 'runner_instructions')
    CODE_INTELLIGENCE_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    RUNNER_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    code_intelligence_instructions: CreateImportPlanCodeIntelligenceInstructions
    runner_instructions: CreateImportPlanRunnerInstructions
    def __init__(
        self,
        code_intelligence_instructions: _Optional[
            _Union[CreateImportPlanCodeIntelligenceInstructions, _Mapping]
        ] = ...,
        runner_instructions: _Optional[_Union[CreateImportPlanRunnerInstructions, _Mapping]] = ...,
    ) -> None: ...

class CreateImportPlanResponse(_message.Message):
    __slots__ = ('success_result', 'failure_result')
    SUCCESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_RESULT_FIELD_NUMBER: _ClassVar[int]
    success_result: CreateImportPlanSuccessResult
    failure_result: CreateImportPlanFailureResult
    def __init__(
        self,
        success_result: _Optional[_Union[CreateImportPlanSuccessResult, _Mapping]] = ...,
        failure_result: _Optional[_Union[CreateImportPlanFailureResult, _Mapping]] = ...,
    ) -> None: ...

class CreateImportPlanSuccessResult(_message.Message):
    __slots__ = ('import_plan_as_yaml',)
    IMPORT_PLAN_AS_YAML_FIELD_NUMBER: _ClassVar[int]
    import_plan_as_yaml: str
    def __init__(self, import_plan_as_yaml: _Optional[str] = ...) -> None: ...

class CreateImportPlanFailureResult(_message.Message):
    __slots__ = ('reason', 'stack_trace')
    REASON_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    reason: str
    stack_trace: str
    def __init__(self, reason: _Optional[str] = ..., stack_trace: _Optional[str] = ...) -> None: ...

class CreateImportPlanCodeIntelligenceInstructions(_message.Message):
    __slots__ = ('search_string', 'base_task_metadata', 'max_rows_per_file')
    SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    BASE_TASK_METADATA_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_PER_FILE_FIELD_NUMBER: _ClassVar[int]
    search_string: str
    base_task_metadata: _config_pb2.BaseTaskMetadata
    max_rows_per_file: int
    def __init__(
        self,
        search_string: _Optional[str] = ...,
        base_task_metadata: _Optional[_Union[_config_pb2.BaseTaskMetadata, _Mapping]] = ...,
        max_rows_per_file: _Optional[int] = ...,
    ) -> None: ...

class CreateImportPlanRunnerInstructions(_message.Message):
    __slots__ = ('base_runner_instructions',)
    BASE_RUNNER_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    base_runner_instructions: _config_pb2.BaseRunnerInstructions
    def __init__(
        self, base_runner_instructions: _Optional[_Union[_config_pb2.BaseRunnerInstructions, _Mapping]] = ...
    ) -> None: ...
