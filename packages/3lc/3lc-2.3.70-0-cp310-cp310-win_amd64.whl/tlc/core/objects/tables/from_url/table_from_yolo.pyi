from _typeshed import Incomplete
from tlc.core.builtins.constants.column_names import BOUNDING_BOXES as BOUNDING_BOXES, BOUNDING_BOX_LIST as BOUNDING_BOX_LIST, HEIGHT as HEIGHT, IMAGE as IMAGE, IMAGE_HEIGHT as IMAGE_HEIGHT, IMAGE_WIDTH as IMAGE_WIDTH, LABEL as LABEL, WIDTH as WIDTH, X0 as X0, X1 as X1, Y0 as Y0, Y1 as Y1
from tlc.core.builtins.constants.number_roles import NUMBER_ROLE_BB_CENTER_X as NUMBER_ROLE_BB_CENTER_X, NUMBER_ROLE_BB_CENTER_Y as NUMBER_ROLE_BB_CENTER_Y, NUMBER_ROLE_BB_SIZE_X as NUMBER_ROLE_BB_SIZE_X, NUMBER_ROLE_BB_SIZE_Y as NUMBER_ROLE_BB_SIZE_Y
from tlc.core.builtins.constants.string_roles import STRING_ROLE_URL as STRING_ROLE_URL
from tlc.core.builtins.constants.units import UNIT_RELATIVE as UNIT_RELATIVE
from tlc.core.builtins.schemas import BoundingBoxListSchema as BoundingBoxListSchema
from tlc.core.object_type_registry import ObjectTypeRegistry as ObjectTypeRegistry
from tlc.core.objects.table import TableRow as TableRow
from tlc.core.objects.tables.in_memory_rows_table import SkipRow as SkipRow, _InMemoryRowsTable
from tlc.core.schema import ImageUrlStringValue as ImageUrlStringValue, Int32Value as Int32Value, MapElement as MapElement, Schema as Schema, StringValue as StringValue
from tlc.core.url import Url as Url
from typing import Any

logger: Incomplete

class TableFromYolo(_InMemoryRowsTable):
    '''A table populated from a YOLO dataset, defined by a YAML file, a split and optionally a root path.

    The `TableFromYolo` class is an interface between 3LC and the YOLO data format. The YAML file must contain the
    keys `path`, `names` and the provided `split`. If the path in the YAML file is relative, a set of alternatives are
    tried: The directory with the YAML file, the parent of this directory and the
    current working directory.

    :Example:
    ```python
    table = TableFromYolo(
        input_url="path/to/yaml/file.yaml",
        split="train",
    )
    print(table.table_rows[0])
    ```

    :param input_url: The path to the YAML file.
    :param split: The split to use.
    '''
    input_url: Incomplete
    split: Incomplete
    def __init__(self, url: Url | None = None, created: str | None = None, row_cache_url: Url | None = None, row_cache_populated: bool | None = None, override_table_rows_schema: Any = None, input_url: str | Url | None = None, split: str | None = None, init_parameters: Any = None) -> None: ...
