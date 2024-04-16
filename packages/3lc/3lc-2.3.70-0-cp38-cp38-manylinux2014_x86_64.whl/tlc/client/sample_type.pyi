import abc
import numpy as np
import torch
import typing
from PIL import Image
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from tlc.client.bulk_data_url_utils import increment_and_get_bulk_data_url as increment_and_get_bulk_data_url
from tlc.core.builtins.constants.column_names import BOUNDING_BOX_LIST as BOUNDING_BOX_LIST, IMAGE_HEIGHT as IMAGE_HEIGHT, IMAGE_WIDTH as IMAGE_WIDTH, LABEL as LABEL, X0 as X0, X1 as X1, Y0 as Y0, Y1 as Y1
from tlc.core.builtins.constants.number_roles import NUMBER_ROLE_BB_MAX_X as NUMBER_ROLE_BB_MAX_X, NUMBER_ROLE_BB_MAX_Y as NUMBER_ROLE_BB_MAX_Y, NUMBER_ROLE_BB_MIN_X as NUMBER_ROLE_BB_MIN_X, NUMBER_ROLE_BB_MIN_Y as NUMBER_ROLE_BB_MIN_Y, NUMBER_ROLE_BB_SIZE_X as NUMBER_ROLE_BB_SIZE_X, NUMBER_ROLE_BB_SIZE_Y as NUMBER_ROLE_BB_SIZE_Y, NUMBER_ROLE_LABEL as NUMBER_ROLE_LABEL
from tlc.core.builtins.constants.units import UNIT_ABSOLUTE as UNIT_ABSOLUTE, UNIT_RELATIVE as UNIT_RELATIVE
from tlc.core.schema import BoolValue as BoolValue, DimensionNumericValue as DimensionNumericValue, Float32Value as Float32Value, Float64Value as Float64Value, ImageUrlStringValue as ImageUrlStringValue, Int16Value as Int16Value, Int32Value as Int32Value, Int64Value as Int64Value, Int8Value as Int8Value, MapElement as MapElement, NumericValue as NumericValue, ScalarValue as ScalarValue, Schema as Schema, SegmentationMaskUrlStringValue as SegmentationMaskUrlStringValue, StringValue as StringValue, Uint16Value as Uint16Value, Uint32Value as Uint32Value, Uint64Value as Uint64Value, Uint8Value as Uint8Value, UrlStringValue as UrlStringValue
from tlc.core.url import Url as Url
from tlc.core.url_adapter_registry import UrlAdapterRegistry as UrlAdapterRegistry
from typing import Generic, Iterator, Literal, Protocol, TypeVar

logger: Incomplete
ST = TypeVar('ST')
RT = TypeVar('RT')

class SampleType(ABC, Generic[ST, RT], metaclass=abc.ABCMeta):
    """The base class for all sample types.

    A `SampleType` defines the type of a single sample. It can be used to create a `Schema` for a `Table`, and
    convert samples between their ML 'sample' representation and their Table 'row' representation. SampleType
    objects are structured like trees, with composite types (e.g. lists, tuples, dicts) as internal nodes and
    atomic types (e.g. ints, floats, strings) as leaves.

    SampleType objects can be created in three main ways:

    1. From a `Schema` object, using `SampleType.from_schema(schema)`.
    2. From a sample, using `SampleType.from_sample(sample)`.
    3. From a 'structure', a simple declarative description of the structure of a single sample,
      using `SampleType.from_structure(structure)`.

    If you have custom types that you want to use in your `Table`, you can create a `SampleType` for them by
    subclassing the appropriate subclass of `SampleType` and registering it with the `register_sample_type` decorator.
    """
    sample_types: dict[str, type[SampleType]]
    sample_type: str
    name: Incomplete
    def __init__(self, name: str) -> None:
        """The basic initializer for all SampleType objects.

        :param name: The name of the SampleType. This will be used as the column name in the Table.
        """
    def rename(self, name: str) -> None:
        """Rename the SampleType.

        :param name: The new name of the SampleType.
        """
    @abstractmethod
    def sample_from_row(self, row: RT) -> ST:
        """Convert a row to a sample using the SampleType.

        :param row: The row to convert.
        :return: The converted sample.
        """
    @abstractmethod
    def row_from_sample(self, sample: ST) -> RT:
        """Convert a sample to a row using the SampleType.

        :param sample: The sample to convert.
        :return: The converted row.
        """
    @property
    @abstractmethod
    def schema(self) -> Schema:
        """A `Schema` object representing the SampleType.

        :return: The `Schema` object.
        """
    @classmethod
    def from_schema(cls, schema: Schema, name: str = 'value') -> SampleType:
        """Create a SampleType from a Schema.

        :param schema: The Schema to create the SampleType from.
        :param name: An optional name for the NoOpSampleType fallback.
        :return: The created SampleType.
        """
    @classmethod
    def from_structure(cls, structure: _SampleTypeStructure, name: str = 'value') -> SampleType:
        '''Create a SampleType from a structure.

        A structure is a simple declarative description of the structure of a single sample. Instead of initializing
        SampleType objects for composite sample types, structures can be represented as nested lists, tuples, or dicts
        containing either SampleType objects, or simply a subclass of SampleType where you don\'t care about
        the names of the columns.

        E.g. `((Int, Int), String)` is equivalent to:
        ```
        HorizontalTuple("value",
            [
                HorizontalTuple("value_0", [Int("value_0_0"), Int("value_0_1")]),
                String("value_1")
            ]
        )
        ```

        :param structure: The structure to create the SampleType from.
        :param name: The name of the SampleType.
        :return: The created SampleType.
        '''
    @classmethod
    def from_sample(cls, sample: ST, name: str = 'value', all_arrays_are_fixed_size: bool = False) -> SampleType:
        """Create a SampleType from a sample.

        This method is used to create a SampleType when creating a Table from a PyTorch Dataset, and the user has not
        specified a SampleType or a structure. Since a SampleType is needed to convert a sample to a row, the first
        sample of the dataset is used as a reference to create the SampleType.

        :param sample: The sample to create the SampleType from.
        :param name: The name of the SampleType.
        :param all_arrays_are_fixed_size: If True, all arrays will be treated as fixed size arrays.
        :return: The created SampleType.
        """
    def __eq__(self, __value: object) -> bool: ...
    def ensure_sample_valid(self, sample: object) -> None:
        """Raises a ValueError if the sample does not match this SampleType. Does nothing otherwise.

        :param sample: The sample to validate.
        :raises ValueError: If the sample does not match this SampleType.
        """
    def ensure_row_valid(self, row: object) -> None:
        """Raises a ValueError if the row does not match this SampleType. Does nothing otherwise.

        :param row: The row to validate.
        :raises ValueError: If the row does not match this SampleType.
        """

def register_sample_type(sample_type: type[_SampleTypeSubclass]) -> type[_SampleTypeSubclass]:
    """A decorator for registering a SampleType.

    Custom sample types must be registered with this decorator in order to be created from a Schema.

    :param sample_type: The SampleType to register.
    :return: The registered SampleType.
    """

class CompositeSampleType(SampleType[ST, typing.Dict[str, object]], Generic[ST], metaclass=abc.ABCMeta):
    """Base class for all composite sample types.

    Composite sample types are sample types that contain other sample types. They are used to represent
    composite data structures like lists, tuples, and dicts. Composite sample types have the `children` attribute,
    which is a list of the sample types that they contain.

    Subclasses of CompositeSampleType only need to implement the `sample_from_row` and `row_from_sample` methods, which
    define how the children should be composed into a single sample or row.
    """
    children: Incomplete
    hidden_children: Incomplete
    def __init__(self, name: str, children: list[SampleType]) -> None: ...
    def rename(self, name: str) -> None: ...
    @abstractmethod
    def sample_from_row(self, row: dict[str, object]) -> ST: ...
    @abstractmethod
    def row_from_sample(self, sample: ST) -> dict[str, object]: ...
    @property
    def schema(self) -> Schema: ...
    def ensure_sample_valid(self, sample: object) -> None: ...
    def ensure_row_valid(self, row: object) -> None: ...

class StringKeyDict(CompositeSampleType[typing.Dict[str, object]]):
    """A dict with string keys."""
    sample_type: str
    def rename(self, name: str) -> None: ...
    def sample_from_row(self, row: dict[str, object]) -> dict[str, object]: ...
    def row_from_sample(self, sample: dict[str, object]) -> dict[str, object]: ...
    def ensure_sample_valid(self, sample: object) -> None: ...

class HorizontalList(CompositeSampleType[list]):
    """A list of fixed length and structure."""
    sample_type: str
    def sample_from_row(self, row: dict[str, object]) -> list: ...
    def row_from_sample(self, sample: list) -> dict[str, object]: ...

class Box(CompositeSampleType[object]):
    """A helper SampleType for making a dict with a single value appear as just the value itself,
    when provided as a sample."""
    sample_type: str
    def __init__(self, child: _SampleTypeStructure, hidden_children: list[_SampleTypeStructure] | None = None) -> None: ...
    def sample_from_row(self, row: dict[str, object]) -> object: ...
    def row_from_sample(self, sample: object) -> dict[str, object]: ...
    def ensure_sample_valid(self, sample: object) -> None: ...

class HorizontalTuple(CompositeSampleType[tuple]):
    """A tuple of fixed length and structure."""
    sample_type: str
    def sample_from_row(self, row: dict[str, object]) -> tuple: ...
    def row_from_sample(self, sample: tuple) -> dict[str, object]: ...

class AtomicSampleType(SampleType[ST, RT], metaclass=abc.ABCMeta):
    """Base class for all atomic sample types.

    Atomic sample types are sample types that contain a single value. They are used to represent
    atomic data structures like ints, floats, strings, and images. Atomic sample types have the `value` attribute,
    which is a `ScalarValue` required to create a `Schema` for the SampleType.

    Subclasses of AtomicSampleType only need to implement the `sample_from_row` and `row_from_sample` methods, which
    define how the value should be converted to and from a row, as well as the `value` property.
    """
    @abstractmethod
    def sample_from_row(self, row: RT) -> ST: ...
    @abstractmethod
    def row_from_sample(self, sample: ST) -> RT: ...
    @property
    def schema(self) -> Schema: ...
    @property
    @abstractmethod
    def value(self) -> ScalarValue:
        """A `ScalarValue` representing the SampleType.

        :return: The `ScalarValue` object.
        """

class PILImage(AtomicSampleType[Image.Image, str]):
    """A PIL Image."""
    sample_type: str
    def __init__(self, name: str) -> None: ...
    @property
    def value(self) -> StringValue: ...
    def sample_from_row(self, row: str) -> Image.Image: ...
    def row_from_sample(self, sample: Image.Image) -> str: ...

class SegmentationPILImage(PILImage):
    """A single-channel PIL-image containing a segmentation mask."""
    sample_type: str
    def __init__(self, name: str, classes: list[str] | dict[int, str] | dict[float, str] | dict[float, MapElement]) -> None: ...
    @property
    def value(self) -> SegmentationMaskUrlStringValue: ...

class Hidden(SampleType[None, object]):
    """A value which should not be present in the sample."""
    sample_type: str
    def __init__(self, name: str, schema: Schema) -> None: ...
    @property
    def schema(self) -> Schema: ...
    def sample_from_row(self, row: object) -> None: ...
    def row_from_sample(self, sample: object) -> object: ...
    def ensure_sample_valid(self, sample: object) -> None:
        """Hidden values will not be present in the 'sample view', but this function never raises in order to allow
        users to write values with a hidden schema to a Table using TableWriter.
        """

class Path(AtomicSampleType[str, str]):
    """A string representing a path."""
    sample_type: str
    @property
    def value(self) -> StringValue: ...
    def sample_from_row(self, row: str) -> str: ...
    def row_from_sample(self, sample: str) -> str: ...

class ImagePath(Path):
    """A path to an image file."""
    sample_type: str
    @property
    def value(self) -> StringValue: ...

class TrivialAtomicSampleType(AtomicSampleType[ST, ST], metaclass=abc.ABCMeta):
    """A base class for atomic sample types whose row representation is the same as their sample representation.

    Subclasses of TrivialAtomicSampleType only need to implement the `value` property.
    """
    def sample_from_row(self, row: ST) -> ST: ...
    def row_from_sample(self, sample: ST) -> ST: ...

class Number(TrivialAtomicSampleType[ST], metaclass=abc.ABCMeta):
    """Base class for numeric types"""
    number_role: Incomplete
    def __init__(self, name: str, number_role: str = '') -> None: ...

class _Int(Number[ST]):
    """Base class for integer types"""
    precision: Incomplete
    signed: Incomplete
    def __init__(self, name: str, precision: Literal[8, 16, 32, 64] = 32, signed: bool = True, number_role: str = '') -> None:
        """:param precision: The precision of the integer, in bits. Must be one of [8, 16, 32, 64].
        :param signed: Whether the value of the integer can be negative.
        :param number_role: The number role of the integer. This determines how the integer will be displayed in the
            Dashboard.
        """
    @property
    def value(self) -> _IntegerValue: ...

class Int(_Int[int]):
    """A python int."""
    sample_type: str

class NumPyInt(_Int[np.integer]):
    """A numpy int."""
    sample_type: str
    def __init__(self, name: str, precision: Literal[8, 16, 32, 64] = 64, signed: bool = True, number_role: str = '') -> None: ...
    def ensure_sample_valid(self, sample: object) -> None: ...

class _Float(Number[ST]):
    """Base class for float types"""
    precision: Incomplete
    normalized: Incomplete
    def __init__(self, name: str, precision: Literal[32, 64] = 64, normalized: bool = False, number_role: str = '') -> None:
        """:param precision: The precision of the float, in bits. Must be one of [32, 64].
        :param normalized: Whether the value of the float is normalized between 0 and 1.
        :param number_role: The number role of the float. This determines how the float will be displayed in the
            Dashboard.
        """
    @property
    def value(self) -> Float32Value | Float64Value: ...

class Float(_Float[float]):
    """A python float."""
    sample_type: str

class NumPyFloat(_Float[np.floating]):
    """A numpy float."""
    sample_type: str
    def __init__(self, name: str, precision: Literal[32, 64] = 64, normalized: bool = False, number_role: str = '') -> None: ...
    def ensure_sample_valid(self, sample: object) -> None: ...

class Bool(TrivialAtomicSampleType[bool]):
    """A python bool."""
    sample_type: str
    @property
    def value(self) -> BoolValue: ...

class CategoricalLabel(TrivialAtomicSampleType[int]):
    """A categorical label.

    Categorical labels are represented as ints, with the mapping from ints to class names defined by the `classes`
    attribute, a list of strings.
    """
    sample_type: str
    value_map: Incomplete
    def __init__(self, name: str, classes: list[str] | dict[int, str] | dict[float, str] | dict[float, MapElement]) -> None:
        """Create a CategoricalLabel.

        :param name: The name of the CategoricalLabel.
        :param classes: The classes of the CategoricalLabel.
        """
    @property
    def value(self) -> Int32Value: ...

class String(TrivialAtomicSampleType[str]):
    """A python string."""
    sample_type: str
    string_role: Incomplete
    def __init__(self, name: str, string_role: str = '') -> None:
        """:param string_role: The string role of the string. This determines how the string will be displayed in the
        Dashboard.
        """
    @property
    def value(self) -> StringValue: ...

class NoOpSampleType(TrivialAtomicSampleType[object]):
    """The fallback SampleType for atomic schemas."""
    sample_type: str
    def __init__(self, name: str, value: ScalarValue) -> None: ...
    @property
    def value(self) -> ScalarValue: ...

class _Container(Protocol):
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...

class DimensionalSampleType(SampleType[ST, RT], metaclass=abc.ABCMeta):
    """Base class for all dimensional sample types.

    Dimensional sample types describe how a sample can be extended along a dimension. They are used to represent
    composite data structures whose size might vary between samples in a dataset. Dimensional sample types have the
    `content` attribute, which is a sample type that describes the structure of the samples along the dimension.

    Subclasses of DimensionalSampleType only need to implement the `sample_from_row` and `row_from_sample` methods,
    which define how the content should be composed into a single sample or row.
    """
    content: Incomplete
    def __init__(self, content: _SampleTypeStructure) -> None:
        """The basic initializer for all DimensionalSampleType objects.

        :param content: The sample type that describes the structure of the samples along the dimension.
        """
    def rename(self, name: str) -> None: ...
    @abstractmethod
    def sample_from_row(self, row: RT) -> ST: ...
    @abstractmethod
    def row_from_sample(self, sample: ST) -> RT: ...
    def ensure_sample_valid(self, sample: object) -> None: ...
    def ensure_row_valid(self, row: object) -> None: ...

class PythonContainer(DimensionalSampleType[_ContainerST, list], metaclass=abc.ABCMeta):
    """Dimensional sample types whose row representation is a list."""
    min_size: Incomplete
    max_size: Incomplete
    def __init__(self, content: _SampleTypeStructure, min_size: int = 0, max_size: int | None = None) -> None:
        """
        :param content: The sample type that describes the structure of the samples along the dimension.
        :param min_size: The minimum size of the container.
        :param max_size: The maximum size of the container.
        """
    def row_from_sample(self, sample: _ContainerST) -> list: ...
    @property
    def schema(self) -> Schema: ...
    def ensure_sample_valid(self, sample: object) -> None: ...
    def ensure_row_valid(self, row: object) -> None: ...

class List(PythonContainer[list]):
    """A list of variable length."""
    sample_type: str
    def sample_from_row(self, row: list) -> list: ...

class Tuple(PythonContainer[tuple]):
    """A tuple of variable length."""
    sample_type: str
    def sample_from_row(self, row: list) -> tuple: ...

class NumpyArray(DimensionalSampleType[np.ndarray, list]):
    """A numpy array of variable length."""
    sample_type: str
    shape: Incomplete
    dtype: Incomplete
    def __init__(self, shape: tuple[int, ...], content: _SampleTypeStructure) -> None:
        """The basic initializer for all NumpyArray objects.

        :param shape: The shape of the array.
        :param content: The sample type that describes the structure of the samples along the dimension.
        """
    @property
    def schema(self) -> Schema: ...
    def sample_from_row(self, row: list) -> np.ndarray: ...
    def row_from_sample(self, sample: np.ndarray) -> list: ...
    def ensure_sample_valid(self, sample: object) -> None: ...
    @staticmethod
    def compute_row_shape(row: list) -> tuple[int, ...]:
        """Compute the shape of a row in a NumpyArray from the row itself.

        :param row: The row to compute the shape from.
        :return: The shape of the row.
        """
    def ensure_row_valid(self, row: object) -> None: ...

class Singleton(DimensionalSampleType[object, object]):
    """A sample type for handling the concept of a pseudo-scalar; a scalar which has a size0 with min=max=1.

    This value should appear in both its sample and row representations as the scalar itself, rather than a list
    containing the scalar.
    """
    sample_type: str
    @property
    def schema(self) -> Schema: ...
    def sample_from_row(self, row: object) -> object: ...
    def row_from_sample(self, sample: object) -> object: ...
    def ensure_sample_valid(self, sample: object) -> None: ...
    def ensure_row_valid(self, row: object) -> None: ...

class BoundingBoxList(StringKeyDict):
    """A COCO-like list of bounding boxes."""
    def __init__(self, name: str, format: Literal['xywh', 'xyxy'] = 'xyxy', normalized: bool = False, classes: list[str] | dict[int, str] | dict[float, str] | dict[float, MapElement] = []) -> None: ...

class SegmentationMask(AtomicSampleType[torch.Tensor, str]):
    """A torch tensor representing a segmentation mask.

    The tensor is expected to have shape (H, W) and contain integer values representing the class of each pixel.
    """
    sample_type: str
    segmentation_value_map: Incomplete
    def __init__(self, name: str, classes: list[str] | dict[int, str] | dict[float, str] | dict[float, MapElement] = []) -> None: ...
    def row_from_sample(self, sample: torch.Tensor) -> str: ...
    def sample_from_row(self, row: str) -> torch.Tensor: ...
    @property
    def value(self) -> StringValue: ...
