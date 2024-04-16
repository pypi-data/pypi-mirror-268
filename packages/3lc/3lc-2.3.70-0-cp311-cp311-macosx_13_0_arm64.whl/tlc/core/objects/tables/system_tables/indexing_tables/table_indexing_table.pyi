from _typeshed import Incomplete
from tlc.core.object import Object as Object
from tlc.core.object_type_registry import ObjectTypeRegistry as ObjectTypeRegistry
from tlc.core.objects.mutable_objects.configuration import Configuration as Configuration
from tlc.core.objects.table import Table as Table
from tlc.core.objects.tables.system_tables.indexing_table import IndexingTable as IndexingTable
from tlc.core.objects.tables.system_tables.indexing_tables.table_info import TableInfo as TableInfo
from tlc.core.schema import Schema as Schema
from tlc.core.url import Url as Url
from tlc.core.url_adapters import ApiUrlAdapter as ApiUrlAdapter
from typing import Any

logger: Incomplete

class TableIndexingTable(IndexingTable):
    """A table populated from the Table index"""
    table_indexing_table_instance: TableIndexingTable | None
    def __init__(self, url: Url | None = None, project_scan_urls: list[Url | str] | None = None, extra_scan_urls: list[Url | str] | None = None, scan_wait: float | None = None, create_default_dirs: bool | None = None, init_parameters: Any = None) -> None: ...
    @staticmethod
    def instance() -> TableIndexingTable:
        """
        Returns the singleton TableIndexingTable object
        """
    def append_row(self, row: Any, location_index: int) -> None: ...
    def should_consider_object(self, obj: Object) -> bool:
        """Only consider Tables"""
