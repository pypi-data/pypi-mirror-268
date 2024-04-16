from tlc.client.sample_type import SampleType as SampleType
from tlc.core.object_type_registry import ObjectTypeRegistry as ObjectTypeRegistry
from tlc.core.objects.table import TableRow as TableRow
from tlc.core.objects.tables.in_memory_rows_table import _InMemoryRowsTable
from tlc.core.schema import Schema as Schema
from tlc.core.url import Url as Url
from typing import Any, Mapping

class TableFromPydict(_InMemoryRowsTable):
    """A table populated from a Python dictionary

    The TableFromPydict will live in memory until persisted. When saved to Url it will write it's rows to a row cache
    file so that it can be loaded back into memory at a later time.

    :Example:
    ```
    python from tlc import TableFromPydict

    data = {
        'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']
    }
    table = TableFromPydict(data=data)
    ```
    """
    def __init__(self, url: Url | None = None, created: str | None = None, row_cache_url: Url | None = None, row_cache_populated: bool | None = None, override_table_rows_schema: Any = None, init_parameters: Any = None, data: Mapping[str, object] | None = None) -> None: ...
