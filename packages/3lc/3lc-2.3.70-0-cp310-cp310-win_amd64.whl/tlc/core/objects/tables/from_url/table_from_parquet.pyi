from _typeshed import Incomplete
from pandas import DataFrame as DataFrame
from tlc.core.object_type_registry import ObjectTypeRegistry as ObjectTypeRegistry
from tlc.core.objects.table import TableRow as TableRow
from tlc.core.objects.tables.in_memory_rows_table import _InMemoryRowsTable
from tlc.core.schema import Schema as Schema, StringValue as StringValue
from tlc.core.schema_helper import SchemaHelper as SchemaHelper
from tlc.core.url import Url as Url
from tlc.core.url_adapter_registry import UrlAdapterRegistry as UrlAdapterRegistry
from typing import Any

logger: Incomplete

class TableFromParquet(_InMemoryRowsTable):
    """A table populated from a Parquet file loaded from a URL"""
    input_url: Incomplete
    row_cache_url: Incomplete
    row_cache_populated: bool
    absolute_input_url: Incomplete
    def __init__(self, url: Url | None = None, created: str | None = None, row_cache_url: Url | None = None, row_cache_populated: bool | None = None, override_table_rows_schema: Any = None, init_parameters: Any = None, input_url: Url | None = None) -> None: ...
    def is_all_parquet(self) -> bool:
        """
        This table is all Parquet.
        """
