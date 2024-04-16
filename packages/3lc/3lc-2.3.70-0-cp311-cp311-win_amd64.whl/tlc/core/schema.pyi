from _typeshed import Incomplete
from tlc.client.sample_type import SampleType as SampleType, _SampleTypeStructure
from tlc.core.builtins.constants.column_names import SAMPLE_WEIGHT as SAMPLE_WEIGHT
from tlc.core.builtins.constants.string_roles import STRING_ROLE_DATETIME as STRING_ROLE_DATETIME, STRING_ROLE_FOLDER_URL as STRING_ROLE_FOLDER_URL, STRING_ROLE_IMAGE_URL as STRING_ROLE_IMAGE_URL, STRING_ROLE_OBJECT_TYPE as STRING_ROLE_OBJECT_TYPE, STRING_ROLE_SEGMENTATION_MASK_URL as STRING_ROLE_SEGMENTATION_MASK_URL, STRING_ROLE_URL as STRING_ROLE_URL
from typing import Any, Mapping

class MapElement(dict):
    """Defines a single item in a value map."""
    def __init__(self, internal_name: str = '', display_name: str = '', description: str = '', display_color: str = '', url: str = '') -> None: ...
    @property
    def internal_name(self) -> str: ...
    @internal_name.setter
    def internal_name(self, value: str) -> None: ...
    @property
    def display_name(self) -> str: ...
    @display_name.setter
    def display_name(self, value: str) -> None: ...
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str) -> None: ...
    @property
    def display_color(self) -> str: ...
    @display_color.setter
    def display_color(self, value: str) -> None: ...
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: str) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def to_minimal_dict(self, include_all: bool) -> dict[str, Any]:
        """
        Add a minimal representation of this object to a dictionary for subsequent serialization to JSON
        """
    @staticmethod
    def from_any(any_map_element: Any) -> MapElement:
        """
        Creates a MapElement object and populates it from an anonymous, possibly sparse object
        """

class ScalarValue:
    """Describes a scalar value in a schema"""
    type: Incomplete
    def __init__(self, value_type: str = ..., default_value: Any = None) -> None: ...
    def to_minimal_dict(self, include_all: bool) -> dict[str, Any]:
        """
        Add a minimal representation of this object to a dictionary for subsequent serialization to JSON
        """
    @staticmethod
    def from_any(any_value: Any) -> ScalarValue:
        """
        Create and populate a ScalarValue (or one of the derived classes) given
        an anonymous, potentially sparse object
        """
    @staticmethod
    def from_value(value: Any) -> ScalarValue:
        """
        Create a scalar value from a Python value.

        :param value: The value to create a ScalarValue from
        :return: A ScalarValue (or one it the derived classes) representing the value
        """
    def __eq__(self, other: Any) -> bool: ...
    @property
    def default_value(self) -> Any: ...

class BoolValue(ScalarValue):
    """
    Describes a scalar boolean value
    """
    def __init__(self, default_value: bool | None = None) -> None: ...
    @staticmethod
    def from_any(any_value: Any) -> BoolValue:
        """
        Create and populate a BoolValue object given an anonymous, potentially sparse object
        """

class NumericValue(ScalarValue):
    """
    Describes a scalar numeric value
    """
    min: Incomplete
    max: Incomplete
    enforce_min: Incomplete
    enforce_max: Incomplete
    step: Incomplete
    number_role: Incomplete
    unit: Incomplete
    map: Incomplete
    def __init__(self, value_type: str = ..., value_min: float | int | None = None, value_max: float | int | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: int | float | None = None) -> None: ...
    def to_minimal_dict(self, include_all: bool) -> dict[str, Any]:
        """
        Add a minimal representation of this object to a dictionary for subsequent serialization to JSON
        """
    @staticmethod
    def from_any(any_value: Any) -> NumericValue:
        """
        Create and populate a NumericValue object given an anonymous, potentially sparse object
        """
    @staticmethod
    def from_value(value: Any) -> NumericValue:
        """Create a numeric value from a Python value.

        :param value: The value to create a NumericValue from
        :return: A NumericValue (or one it the derived classes) representing the value
        """
    def __eq__(self, other: Any) -> bool: ...

class Float32Value(NumericValue):
    """
    A numeric value with type 'float32'
    """
    def __init__(self, value_min: float | None = None, value_max: float | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: float | None = None) -> None: ...

class Float64Value(NumericValue):
    """
    A numeric value with type 'float64'
    """
    def __init__(self, value_min: float | None = None, value_max: float | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: float | None = None) -> None: ...

class Uint8Value(NumericValue):
    """
    A numeric value with type 'uint8'
    """
    def __init__(self, value_min: float | None = None, value_max: float | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: int | None = None) -> None: ...

class Int8Value(NumericValue):
    """
    A numeric value with type 'int8'
    """
    def __init__(self, value_min: float | None = None, value_max: float | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: int | None = None) -> None: ...

class Uint16Value(NumericValue):
    """
    A numeric value with type 'uint16'
    """
    def __init__(self, value_min: float | None = None, value_max: float | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: int | None = None) -> None: ...

class Int16Value(NumericValue):
    """
    A numeric value with type 'int16'
    """
    def __init__(self, value_min: float | None = None, value_max: float | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: int | None = None) -> None: ...

class Uint32Value(NumericValue):
    """
    A numeric value with type 'uint32'
    """
    def __init__(self, value_min: float | None = None, value_max: float | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: int | None = None) -> None: ...

class Int32Value(NumericValue):
    """
    A numeric value with type 'int32'
    """
    min: Incomplete
    max: Incomplete
    def __init__(self, value_min: int | None = None, value_max: int | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: int | None = None) -> None: ...

class Uint64Value(NumericValue):
    """
    A numeric value with type 'uint64'
    """
    def __init__(self, value_min: float | None = None, value_max: float | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: int | None = None) -> None: ...

class Int64Value(NumericValue):
    """
    A numeric value with type 'int64'
    """
    def __init__(self, value_min: float | None = None, value_max: float | None = None, enforce_min: bool = False, enforce_max: bool = False, value_step: float = 0, number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, default_value: int | None = None) -> None: ...

class DimensionNumericValue(Int32Value):
    """
    Describes a scalar numeric value which is a dimension size within a property
    """
    display_name: Incomplete
    description: Incomplete
    sample_type: Incomplete
    min: Incomplete
    def __init__(self, value_min: int = 0, value_max: int | None = None, enforce_min: bool = True, enforce_max: bool = False, display_name: str = '', description: str = '', number_role: str = '', unit: str = '', value_map: dict[float, MapElement] | None = None, sample_type: str = '', default_value: int | None = None) -> None: ...
    def to_minimal_dict(self, include_all: bool) -> dict[str, Any]:
        """
        Add a minimal representation of this object to a dictionary for
        subsequent serialization to JSON
        """
    @staticmethod
    def dimension_numeric_value_from_any(this_property: Any) -> DimensionNumericValue | None:
        """
        Creates a DimensionNumericValue object and populates it from an anonymous, possibly sparse object
        """
    def is_fixed_size(self) -> bool: ...
    def is_scalar(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...

class StringValue(ScalarValue):
    """
    Describes a string value
    """
    string_role: Incomplete
    url_string_icon: str
    def __init__(self, string_role: str = '', default_value: str | None = None) -> None: ...
    def to_minimal_dict(self, include_all: bool) -> dict[str, Any]:
        """
        Add a minimal representation of this object to a dictionary for subsequent serialization to JSON
        """
    @staticmethod
    def from_any(any_value: Any) -> StringValue:
        """
        Create and populate a StringValue object given an anonymous, potentially sparse object
        """
    def __eq__(self, other: Any) -> bool: ...

class UrlStringValue(StringValue):
    """
    Describes a generic URL string value
    """
    string_role: Incomplete
    url_string_icon: Incomplete
    def __init__(self, url_string_icon: str = '', default_value: str | None = None) -> None: ...

class ImageUrlStringValue(UrlStringValue):
    """
    Describes a Image URL string value
    """
    string_role: Incomplete
    def __init__(self, default_value: str | None = None) -> None: ...

class SegmentationUrlStringValue(UrlStringValue):
    """
    Describes a Segmentation URL string value
    """
    segmentation_value_map: Incomplete
    string_role: Incomplete
    def __init__(self, default_value: str | None = None, segmentation_value_map: dict[float, MapElement] | None = None) -> None: ...
    def to_minimal_dict(self, include_all: bool) -> dict[str, Any]: ...
    @staticmethod
    def from_any(any_value: Any) -> SegmentationUrlStringValue:
        """
        Create and populate a SegmentationUrlStringValue object given an anonymous, potentially sparse object
        """

class SegmentationMaskUrlStringValue(SegmentationUrlStringValue):
    """
    Describes a Segmentation Mask URL string value
    """
    string_role: Incomplete
    def __init__(self, default_value: str | None = None, segmentation_value_map: dict[float, MapElement] | None = None) -> None: ...
    @staticmethod
    def from_any(any_value: Any) -> SegmentationMaskUrlStringValue:
        """
        Create and populate a SegmentationMaskUrlStringValue object given an anonymous, potentially sparse object
        """

class DatetimeStringValue(StringValue):
    """
    Describes a date-time string value
    """
    string_role: Incomplete
    def __init__(self, default_value: str | None = None) -> None: ...

class ObjectTypeStringValue(StringValue):
    """
    A string containing an object type
    """
    string_role: Incomplete
    def __init__(self, default_value: str | None = None) -> None: ...

class FolderUrlStringValue(StringValue):
    """
    Describes a generic URL string value
    """
    string_role: Incomplete
    def __init__(self, default_value: str | None = None) -> None: ...

class DictValue(ScalarValue):
    """
    Describes a value which consists of an anonymous, free-form dictionary
    """
    def __init__(self, default_value: dict = {}) -> None: ...
    @staticmethod
    def from_any(_: Any) -> DictValue: ...
    @property
    def default_value(self) -> dict: ...

class Schema:
    '''
    A schema is a recursive structure which defines the layout of an object. It defines what elements the
    object consists of, which must be either

    - Atomic type (with optional metadata, e.g. value range, unit, etc.)
       OR
    - Composite contents (a list of schemas describing the sub-object)

    In addition, it defines HOW MANY of these scalar or composite elements exist, in the form of
    up to six-dimensions which can each be described separately and be of fixed or variable lengths. The
    default size of dimensions is 1, describing a scalar value.

    Schemas are used for

    - Defining the layout of Objects (as reported by e.g. "MyObject.schema")
    - In the case of Tables: defining the common layout of all table rows
      (as reported by e.g "MyTableObject.schema.values["rows"])

    In the case where a schema defines a "top-level" object, it will always have a
    \'values\' attribute (since it is always a composite object, and does not comprise only a single atomic value).
    '''
    display_name: Incomplete
    description: Incomplete
    writable: Incomplete
    display_importance: Incomplete
    composite_role: Incomplete
    display_color: Incomplete
    swap_group: Incomplete
    computable: Incomplete
    sample_type: Incomplete
    transient: Incomplete
    default_visible: Incomplete
    size0: Incomplete
    size1: Incomplete
    size2: Incomplete
    size3: Incomplete
    size4: Incomplete
    size5: Incomplete
    value: Incomplete
    values: Incomplete
    def __init__(self, display_name: str = '', description: str = '', writable: bool = True, display_importance: float = 0, value: ScalarValue | None = None, values: dict[str, Schema] | None = None, composite_role: str = '', display_color: str = '', swap_group: str = '', computable: bool = True, sample_type: str = '', transient: bool = False, default_visible: bool = True, size0: DimensionNumericValue | None = None, size1: DimensionNumericValue | None = None, size2: DimensionNumericValue | None = None, size3: DimensionNumericValue | None = None, size4: DimensionNumericValue | None = None, size5: DimensionNumericValue | None = None) -> None: ...
    def is_empty(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def to_minimal_dict(self, include_all: bool) -> dict[str, Any]:
        """
        Add a minimal representation of this object to a dictionary for subsequent serialization to JSON
        """
    def add_sub_schema(self, name: str, schema: Schema) -> None:
        """
        Adds a Schema as a sub-property within this Schema (i.e. into the 'values' collection)
        """
    def add_sub_value(self, name: str, value: ScalarValue, writable: bool = True, computable: bool = True) -> None:
        """
        Adds a scalar value as a sub-property within this Schema (i.e. into the 'values' collection)
        """
    def to_json(self) -> str:
        """
        Writes the contents of this schema to a JSON string. Note that

        - Defaults values are omitted for brevity
        - Schemas might be recursive
        """
    @staticmethod
    def from_any(any_object: Any) -> Schema:
        """
        Returns a Schema object which has been populated from a serialized (possibly sparse) object
        """
    @staticmethod
    def from_json(json_string: str) -> Schema:
        """
        Returns a Schema object which has been populated from a JSON string
        """
    def consider_override_from(self, override_schema: Schema | Mapping[str, object] | None) -> Schema:
        """
        Selectively overwrites columns within this Schema according to the columns defined in another Schema.
        """
    def does_object_match(self, _object: Any) -> bool:
        """Checks whether a schema matches an example object.

        This requires exact 1:1 mapping between attributes in the object
        and the schema (including recursively). This means no attributes
        can be missing, nor can there be any additional attributes only
        present in the object.
        """
    def is_fixed_size(self) -> bool: ...
    def is_scalar(self) -> bool: ...
    def is_atomic(self) -> bool:
        """Return whether the schema is atomic, i.e. has a single value.

        The opposite of `is_composite`.
        :return: Whether the schema is atomic
        """
    def is_composite(self) -> bool:
        """Return whether the schema is composite, i.e. has multiple values.

        The opposite of `is_atomic`.
        :return: Whether the schema is composite
        """
    @property
    def sample_type_object(self) -> SampleType: ...
    def row_from_sample(self, sample: Any) -> dict[str, Any]: ...
    def sample_from_row(self, row: Mapping[str, object]) -> Any: ...
    @classmethod
    def from_structure(cls, structure: _SampleTypeStructure) -> Schema:
        """Creates a schema from a structure.

        :param structure: The structure to create a schema from
        :return: The schema
        """
    @classmethod
    def from_sample(cls, sample: Any) -> Schema:
        """Creates a schema describing the provided sample.

        :param sample: The sample to create a schema from
        :return: The schema
        """
    def push_dim(self, dim: DimensionNumericValue | None = None) -> DimensionNumericValue | None:
        """Inserts dim as size0 and shifts all other dimensions right. (size1 becomes size0, size2 becomes size1).

        :param dim: The dimension to insert as size0
        :return: The old size5
        """
    def pop_dim(self) -> DimensionNumericValue | None:
        """Sets size5 to None and shifts all other dimensions left. (size5 becomes size4, size4 becomes size3, etc.).

        :return: The old size0
        """
    def add_sample_weight(self, hidden: bool = True) -> None:
        """Adds a sample weight column to the schema.

        :param hidden: Whether the column should be hidden
        """

class NoneSchema(Schema):
    '''A schema that encodes a None value

    It is not a valid Schema as it has neither value nor values. It is used to encode override schemas that remove
    sub schemas.

    :Example:
    ```python
    override_schema = { "values": { "column_to_remove": None }}
    # or equivalently
    override_schema = { "values": { "column_to_remove": NoneSchema()}}
    ```
    '''
    def __init__(self) -> None: ...
    def to_json(self) -> str: ...
