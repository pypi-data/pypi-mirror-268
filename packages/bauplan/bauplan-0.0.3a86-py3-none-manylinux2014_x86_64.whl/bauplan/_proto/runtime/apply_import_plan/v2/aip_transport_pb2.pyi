from bauplan._proto.runtime.runtime_shared.v2 import config_pb2 as _config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyImportPlanRequest(_message.Message):
    __slots__ = ('code_intelligence_instructions', 'runner_instructions')
    CODE_INTELLIGENCE_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    RUNNER_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    code_intelligence_instructions: ApplyImportPlanCodeIntelligenceInstructions
    runner_instructions: ApplyImportPlanRunnerInstructions
    def __init__(
        self,
        code_intelligence_instructions: _Optional[
            _Union[ApplyImportPlanCodeIntelligenceInstructions, _Mapping]
        ] = ...,
        runner_instructions: _Optional[_Union[ApplyImportPlanRunnerInstructions, _Mapping]] = ...,
    ) -> None: ...

class ApplyImportPlanResponse(_message.Message):
    __slots__ = ('success_result', 'failure_result')
    SUCCESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_RESULT_FIELD_NUMBER: _ClassVar[int]
    success_result: ApplyImportPlanSuccessResult
    failure_result: ApplyImportPlanFailureResult
    def __init__(
        self,
        success_result: _Optional[_Union[ApplyImportPlanSuccessResult, _Mapping]] = ...,
        failure_result: _Optional[_Union[ApplyImportPlanFailureResult, _Mapping]] = ...,
    ) -> None: ...

class ApplyImportPlanSuccessResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ApplyImportPlanFailureResult(_message.Message):
    __slots__ = ('reason', 'stack_trace')
    REASON_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    reason: str
    stack_trace: str
    def __init__(self, reason: _Optional[str] = ..., stack_trace: _Optional[str] = ...) -> None: ...

class ApplyImportPlanCodeIntelligenceInstructions(_message.Message):
    __slots__ = (
        'import_plan_as_str',
        'data_catalog',
        'base_task_metadata',
        'new_table_name',
        'new_table_branch',
    )
    IMPORT_PLAN_AS_STR_FIELD_NUMBER: _ClassVar[int]
    DATA_CATALOG_FIELD_NUMBER: _ClassVar[int]
    BASE_TASK_METADATA_FIELD_NUMBER: _ClassVar[int]
    NEW_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_TABLE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    import_plan_as_str: str
    data_catalog: _config_pb2.DataCatalog
    base_task_metadata: _config_pb2.BaseTaskMetadata
    new_table_name: str
    new_table_branch: str
    def __init__(
        self,
        import_plan_as_str: _Optional[str] = ...,
        data_catalog: _Optional[_Union[_config_pb2.DataCatalog, _Mapping]] = ...,
        base_task_metadata: _Optional[_Union[_config_pb2.BaseTaskMetadata, _Mapping]] = ...,
        new_table_name: _Optional[str] = ...,
        new_table_branch: _Optional[str] = ...,
    ) -> None: ...

class ApplyImportPlanRunnerInstructions(_message.Message):
    __slots__ = ('base_runner_instructions',)
    BASE_RUNNER_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    base_runner_instructions: _config_pb2.BaseRunnerInstructions
    def __init__(
        self, base_runner_instructions: _Optional[_Union[_config_pb2.BaseRunnerInstructions, _Mapping]] = ...
    ) -> None: ...
