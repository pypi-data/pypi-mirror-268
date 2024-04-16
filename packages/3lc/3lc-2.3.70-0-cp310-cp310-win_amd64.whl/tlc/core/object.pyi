from _typeshed import Incomplete
from abc import ABC
from tlc.core.builtins.constants.string_roles import STRING_ROLE_DATETIME as STRING_ROLE_DATETIME, STRING_ROLE_VERSION as STRING_ROLE_VERSION
from tlc.core.json_helper import JsonHelper as JsonHelper
from tlc.core.schema import BoolValue as BoolValue, DictValue as DictValue, ObjectTypeStringValue as ObjectTypeStringValue, Schema as Schema, StringValue as StringValue, UrlStringValue as UrlStringValue
from tlc.core.serialization_version_helper import SerializationVersionHelper as SerializationVersionHelper
from tlc.core.transaction_closer import TransactionCloser as TransactionCloser
from tlc.core.url import Scheme as Scheme, Url as Url
from tlc.core.url_adapter import IfExistsOption as IfExistsOption
from tlc.core.url_adapter_registry import UrlAdapterRegistry as UrlAdapterRegistry
from tlcsaas.transaction import Transaction as Transaction
from typing import Any, Literal

logger: Incomplete

class Object(ABC):
    '''The base class for all 3LC objects.

    Contains these basic properties:

    \'type\':    Which class this object is (used by factory method to instantiate
               the correct class during JSON deserialization)

    \'url\':     The URL which this object instance was deserialized FROM, or
               should be serialized TO.

               Note that this value is NOT written to JSON, since the JSON representation
               could potentially be moved around (as in e.g. a file being moved
               to another folder).

    \'created\': The time when this object was first created.

    \'schema\':  A property describing the layout of this object. Note that this
               value should NOT be written to JSON, except for objects where
               recreating the schema would be a "heavy" operation.

               This means, in practice, that the \'schema\' is only ever written
               to JSON for Table objects, and only after they have determined the
               immutable schema for their \'rows\' property.

               For this last reason, there\'s an assert that schemas are never written
               unless there\'s a non-empty \'schema.rows.values\' list.

    \'serialization_version\': The serialization version of the object.
    '''
    serialization_version: Incomplete
    type: Incomplete
    created: Incomplete
    url: Incomplete
    is_url_writable: Incomplete
    schema: Incomplete
    transaction_id: Incomplete
    def __init__(self, url: Url | None = None, created: str | None = None, init_parameters: Any = None) -> None: ...
    def initial_value(self, property_name: str, new_value: Any, default_value: Any = None) -> Any:
        """Returns self[property_name] if it exists, or the provided new value if not None else the default_value

        This pattern allows all creation of new objects to be done via the constructor
        """
    def ensure_minimal_schema(self) -> None: ...
    def ensure_complete_schema(self) -> None: ...
    def ensure_dependent_properties(self) -> None:
        """Make sure dependent properties are populated

        This method must set all properties required to achieve the 'fully defined' state of an object.

        For example: `Table.row_count` is initially set to `UNKNOWN_ROW_COUNT` (-1) to indicate that it is not (yet)
        known, after a call to prepare_data_production it will be set to the correct value.

        Override in subclasses to ensure the required dependent properties are populated
        """
    def ensure_fully_defined(self) -> None:
        """Makes sure the internal state of the object is fully defined.

        For most objects, this simply amounts to populating the 'schema' property
        according to the properties which are directly present within the class.

        However, for Table objects it also means:

        - Making sure the 'schema.rows' sub-schema defines the layout of table
          rows if and when they will be produced

        To ensure that data is ready and dependent properties are populated, call ensure_dependent_properties.
        """
    def write_to_url(self, force: bool = False) -> Url: ...
    @staticmethod
    def add_object_url_property_to_schema(schema: Schema, url_string_icon: str = '') -> None:
        """
        Adds the 'url' property to this schema
        """
    @staticmethod
    def add_is_url_writable_property_to_schema(schema: Schema) -> None:
        """
        Adds the 'is_url_writable' property to this schema
        """
    def should_include_schema_in_json(self, _schema: Schema) -> bool:
        """
        Indicates whether the schema property of this object should be included when
        serializing to JSON
        """
    def to_json(self, init_level: int = 1) -> str:
        """
        Returns a JSON representation of this object. This will be sufficient to recreate
        a fully functioning clone of the object at a later time.

        Note that for brevity, properties with default values are not written to the string.
        """
    def copy(self, *, destination_url: Url | None = None, if_exists: Literal['raise', 'rename', 'overwrite'] = 'raise') -> Object:
        """Returns a copy of this object, with the specified URL.

        :param destination_url: The url to write the copy to. If not provided, a new url will be generated based on the
            objects own url.
        :param if_exists: How to handle the case where the destination URL already exists.

        :returns: A copy of this table.
        """
    def delete(self) -> None:
        """Deletes this object from its URL."""
    def is_stale(self, timestamp: str | None, epsilon: float = 0.0) -> bool:
        """
        Indicates whether this object is stale compared to a given timestamp.

        The base implementation never considers an object stale.
        :param timestamp: The timestamp against which to check staleness. Can be None.
        :param epsilon: The tolerance in seconds for staleness. If the difference between
                        the object's timestamp and the provided timestamp exceeds this value,
                        the object is considered stale. Defaults to 0.0s.
        :returns: True if the object is stale, False otherwise.

        :raises ValueError: if the timestamp is invalid.
        """
    def absolute_url_from_relative(self, input_url: Url) -> Url:
        """
        Converts a relative URL to be absolute, given the URL of this object
        """
    def relative_url_from_absolute(self, input_url: Url) -> Url:
        """
        Converts an absolute URL to be relative, given the URL of this object
        """
    @classmethod
    def type_name(cls) -> str:
        """The type name of the class, used to resolve factory methods"""
    @classmethod
    def from_url(cls, url: Url | str) -> Object:
        """Creates an Object from a URL.

        :param url: The URL of the object.

        :return: The object.
        """
