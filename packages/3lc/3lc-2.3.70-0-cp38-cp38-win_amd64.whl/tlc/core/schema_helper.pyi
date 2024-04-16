import pyarrow as pa
from _typeshed import Incomplete
from tlc.core.builtins.constants.number_roles import NUMBER_ROLE_NN_EMBEDDING as NUMBER_ROLE_NN_EMBEDDING
from tlc.core.builtins.constants.string_roles import STRING_ROLE_TABLE_URL as STRING_ROLE_TABLE_URL
from tlc.core.builtins.constants.values import DEFAULT_LIST_MAX_LENGTH as DEFAULT_LIST_MAX_LENGTH
from tlc.core.object_reference import ObjectReference as ObjectReference
from tlc.core.schema import BoolValue as BoolValue, DatetimeStringValue as DatetimeStringValue, DictValue as DictValue, DimensionNumericValue as DimensionNumericValue, Float32Value as Float32Value, Float64Value as Float64Value, ImageUrlStringValue as ImageUrlStringValue, Int16Value as Int16Value, Int32Value as Int32Value, Int64Value as Int64Value, Int8Value as Int8Value, NumericValue as NumericValue, ScalarValue as ScalarValue, Schema as Schema, SegmentationMaskUrlStringValue as SegmentationMaskUrlStringValue, SegmentationUrlStringValue as SegmentationUrlStringValue, StringValue as StringValue, Uint16Value as Uint16Value, Uint32Value as Uint32Value, Uint64Value as Uint64Value, Uint8Value as Uint8Value, UrlStringValue as UrlStringValue
from tlc.core.url import Url as Url
from typing import Any

class SchemaHelper:
    """A class with helper methods for working with Schema objects"""
    ARROW_TYPE_TO_SCALAR_VALUE_MAPPING: Incomplete
    SCALAR_VALUE_TYPE_TO_ARROW_TYPE_MAPPING: Incomplete
    @staticmethod
    def object_input_urls(obj: Any, schema: Schema) -> list[Url]:
        """
        Returns a list of all URLs referenced by this object, from scalar
        strings or lists of strings

        Note: the result is likely to be relative with respect to the object's URL
        """
    @staticmethod
    def from_pyarrow_datatype(data_type: pa.DataType) -> type[ScalarValue] | None:
        """Converts a DataType to a ScalarValue.

        :param data_type: The pyarrow DataType object to convert.
        :returns: The type of the scalar value that corresponds to the pyarrow DataType.
        """
    @staticmethod
    def to_pyarrow_datatype(schema_or_value: Schema | ScalarValue) -> pa.DataType:
        """Converts a Schema or ScalarValue to a pyarrow DataType.

        Currently supports scalar types, lists of scalar types, structs, and lists of structs.

        :param schema_or_value: The schema or scalar value to convert.
        :returns: The corresponding pyarrow datatype.
        """
    @staticmethod
    def tlc_schema_to_pyarrow_schema(tlc_schema: Schema) -> pa.Schema:
        """Convert a 3LC schema to a PyArrow schema.

        :param tlc_schema: The 3LC schema to convert.
        :returns: The PyArrow schema.
        """
    @staticmethod
    def pyarrow_schema_to_tlc_schema(arrow_schema: pa.Schema, **schema_kwargs: Any) -> Schema:
        """Convert a PyArrow schema to a 3LC schema.

        :param arrow_schema: The PyArrow schema to convert.
        :param schema_kwargs: Additional keyword arguments to pass to the Schema constructor.
        :returns: The 3LC schema.
        """
    @staticmethod
    def cast_scalar(value: Any, value_type: ScalarValue) -> Any:
        """Cast a value which is a ScalarValue into its corresponding python type."""
    @staticmethod
    def cast_value(value: Any, value_schema: Schema) -> Any:
        """Cast any value into its corresponding python type based on the Schema."""
    @staticmethod
    def default_scalar(value_type: ScalarValue) -> Any:
        """Returns the default value for a ScalarValue."""
    @staticmethod
    def default_value(schema: Schema) -> Any:
        """Returns the default value for a schema.

        A schema holds either:
          - a ScalarValue (schema.value) which corresponds to a scalar type (potentially an array of scalars)
          - a dict of sub-Schemas (schema.values) corresponding compound types (potentially an array)

        """
    @staticmethod
    def is_computable(schema: Schema) -> bool:
        """Returns True if the schema is computable."""
    @staticmethod
    def add_schema_to_existing_schema_at_location(added_schema: Schema, existing_schema: Schema, location: list[str]) -> None:
        """Adds the value to the schema at the given location."""
    @staticmethod
    def is_pseudo_scalar(schema: Schema) -> bool:
        """Returns True if the schema is a pseudo-scalar.

        When a schema has a size0 with min=1 and max=1, it is considered a pseudo-scalar. This is a trick we use when
        unrolling/rolling up tables. We want to treat table cells with 1-element lists as scalars.
        """
    @staticmethod
    def get_nested_schema(schema: Schema, path: str) -> Schema | None:
        """Retrieves a nested schema from a schema.

        :param schema: The schema to retrieve the nested schema from.
        :param path: The (dot-separated) path to the nested schema.
        :return: The nested schema, or None if the path doesn't exist.
        """
    @staticmethod
    def create_sparse_schema_from_scalar_value(path: str, scalar_value: ScalarValue) -> Schema:
        """Creates a sparse schema from a path and a schema.

        :param path: The (dot-separated) path to the nested schema.
        :param new_schema: The schema to create the sparse schema from.
        :return: The sparse schema.
        """
    @staticmethod
    def create_sparse_schema_from_schema(path: str, schema: Schema) -> Schema:
        """Creates a sparse schema from a path and a schema.

        :param path: The (dot-separated) path to the nested schema.
        :param new_schema: The schema to create the sparse schema from.
        :return: The sparse schema.
        """
    @staticmethod
    def url_values(schema: Schema) -> list[str]:
        """Return a list of sub-schemas that represent atomic URL values.

        :param schema: The schema to retrieve the URL values from.
        :return: A list of sub-value keys corresponding to URL values.
        """
    @staticmethod
    def is_embedding_value(schema: Schema) -> bool:
        """Returns True if the schema is an atomic schema describing an unreduced embedding value."""
