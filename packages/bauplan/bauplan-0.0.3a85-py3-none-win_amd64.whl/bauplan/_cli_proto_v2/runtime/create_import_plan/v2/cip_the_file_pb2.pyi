from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class IcebergPrimitiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ICEBERG_PRIMITIVE_TYPE_UNSPECIFIED: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_INT: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_LONG: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_FLOAT: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_DOUBLE: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_DECIMAL: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_DATE: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_TIME: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_TIMESTAMP: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_TIMESTAMP_TZ: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_TIMESTAMP_NS: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_TIMESTAMP_TZ_NS: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_STRING: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_UUID: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_FIXED: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_BINARY: _ClassVar[IcebergPrimitiveType]
    ICEBERG_PRIMITIVE_TYPE_BOOLEAN: _ClassVar[IcebergPrimitiveType]

ICEBERG_PRIMITIVE_TYPE_UNSPECIFIED: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_INT: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_LONG: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_FLOAT: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_DOUBLE: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_DECIMAL: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_DATE: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_TIME: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_TIMESTAMP: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_TIMESTAMP_TZ: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_TIMESTAMP_NS: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_TIMESTAMP_TZ_NS: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_STRING: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_UUID: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_FIXED: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_BINARY: IcebergPrimitiveType
ICEBERG_PRIMITIVE_TYPE_BOOLEAN: IcebergPrimitiveType

class ColumnMetadata(_message.Message):
    __slots__ = ('column_name', 'detected_types')
    COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    DETECTED_TYPES_FIELD_NUMBER: _ClassVar[int]
    column_name: str
    detected_types: _containers.RepeatedScalarFieldContainer[IcebergPrimitiveType]
    def __init__(
        self,
        column_name: _Optional[str] = ...,
        detected_types: _Optional[_Iterable[_Union[IcebergPrimitiveType, str]]] = ...,
    ) -> None: ...

class SingleFileSchema(_message.Message):
    __slots__ = ('column_to_type', 'path')
    class ColumnToTypeEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: IcebergPrimitiveType
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[_Union[IcebergPrimitiveType, str]] = ...
        ) -> None: ...

    COLUMN_TO_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    column_to_type: _containers.ScalarMap[str, IcebergPrimitiveType]
    path: str
    def __init__(
        self, column_to_type: _Optional[_Mapping[str, IcebergPrimitiveType]] = ..., path: _Optional[str] = ...
    ) -> None: ...

class ConflictEntry(_message.Message):
    __slots__ = ('column_with_conflict', 'reconcile_step')
    COLUMN_WITH_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    RECONCILE_STEP_FIELD_NUMBER: _ClassVar[int]
    column_with_conflict: str
    reconcile_step: str
    def __init__(
        self, column_with_conflict: _Optional[str] = ..., reconcile_step: _Optional[str] = ...
    ) -> None: ...

class PlanMetadata(_message.Message):
    __slots__ = (
        'proposed_table_name',
        'proposed_branch_name',
        'generation_date',
        'generated_by',
        'max_rows_per_file',
    )
    PROPOSED_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    GENERATION_DATE_FIELD_NUMBER: _ClassVar[int]
    GENERATED_BY_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_PER_FILE_FIELD_NUMBER: _ClassVar[int]
    proposed_table_name: str
    proposed_branch_name: str
    generation_date: str
    generated_by: str
    max_rows_per_file: int
    def __init__(
        self,
        proposed_table_name: _Optional[str] = ...,
        proposed_branch_name: _Optional[str] = ...,
        generation_date: _Optional[str] = ...,
        generated_by: _Optional[str] = ...,
        max_rows_per_file: _Optional[int] = ...,
    ) -> None: ...

class SchemaInfo(_message.Message):
    __slots__ = ('detected_schemas', 'conflicts')
    DETECTED_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    detected_schemas: _containers.RepeatedCompositeFieldContainer[ColumnMetadata]
    conflicts: _containers.RepeatedCompositeFieldContainer[ConflictEntry]
    def __init__(
        self,
        detected_schemas: _Optional[_Iterable[_Union[ColumnMetadata, _Mapping]]] = ...,
        conflicts: _Optional[_Iterable[_Union[ConflictEntry, _Mapping]]] = ...,
    ) -> None: ...

class ImportPlan(_message.Message):
    __slots__ = ('schema_info', 'plan_metadata', 'debugs')
    SCHEMA_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAN_METADATA_FIELD_NUMBER: _ClassVar[int]
    DEBUGS_FIELD_NUMBER: _ClassVar[int]
    schema_info: SchemaInfo
    plan_metadata: PlanMetadata
    debugs: _containers.RepeatedCompositeFieldContainer[SingleFileSchema]
    def __init__(
        self,
        schema_info: _Optional[_Union[SchemaInfo, _Mapping]] = ...,
        plan_metadata: _Optional[_Union[PlanMetadata, _Mapping]] = ...,
        debugs: _Optional[_Iterable[_Union[SingleFileSchema, _Mapping]]] = ...,
    ) -> None: ...
