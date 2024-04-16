from _typeshed import Incomplete
from tlc.core.builtins.constants.number_roles import NUMBER_ROLE_INDEX as NUMBER_ROLE_INDEX
from tlc.core.object import Object as Object
from tlc.core.object_registry import IndexerCallbackEventType as IndexerCallbackEventType, ObjectRegistry as ObjectRegistry
from tlc.core.object_type_registry import MalformedContentError as MalformedContentError, NotRegisteredError as NotRegisteredError, ObjectTypeRegistry as ObjectTypeRegistry
from tlc.core.objects.mutable_object import MutableObject as MutableObject
from tlc.core.objects.table import Table as Table
from tlc.core.objects.tables.system_tables.indexing import TaskCounter as TaskCounter
from tlc.core.schema import DimensionNumericValue as DimensionNumericValue, Float32Value as Float32Value, Int32Value as Int32Value, MapElement as MapElement, ObjectTypeStringValue as ObjectTypeStringValue, Schema as Schema, StringValue as StringValue, UrlStringValue as UrlStringValue
from tlc.core.url import Url as Url
from typing import Any, Sequence

logger: Incomplete

class IndexingTable(Table):
    """The base class for tables which are populated by scanning the contents of a URL.

    The scanning can be limited to a particular object type (e.g. Run).

    :param url: The URL of the table.
    :param created: The creation timestamp of the table.
    :param row_cache_url: The URL of the row cache.
    :param row_cache_populated: Indicates whether the row cache is populated.
    :param scan_urls: The URLs to be scanned.
    :param project_scan_urls: The URLs to be scanned. Folder layout must adhere to 3LC conventions.
    :param constrain_to_type: The type of objects to be included in the table.
    :param scan_wait: The time interval (in seconds) between subsequent scans.
    :param file_extensions: The file extensions to be considered while scanning.
    :param init_parameters: Any additional initialization parameters.

    """
    extra_scan_urls: Incomplete
    project_scan_urls: Incomplete
    constrain_to_type: Incomplete
    scan_wait: Incomplete
    file_extensions: Incomplete
    create_default_dirs: Incomplete
    running: bool
    def __init__(self, url: Url | None = None, created: str | None = None, row_cache_url: Url | None = None, row_cache_populated: bool | None = None, project_scan_urls: Sequence[str | Url] | None = None, extra_scan_urls: Sequence[str | Url] | None = None, constrain_to_type: str | None = None, scan_wait: float | None = None, file_extensions: list[str] | None = None, create_default_dirs: bool | None = None, init_parameters: Any = None) -> None: ...
    def add_extra_scan_urls(self, scan_urls: list[Url | str]) -> None:
        """Add extra scan urls to this indexing table

        If the indexing table is running changes will be propagated to worker threads.
        """
    def add_project_scan_urls(self, project_scan_urls: list[Url | str]) -> None:
        """Add scan urls to this indexing table

        If the indexing table is running changes will be propagated to worker threads.
        """
    def consider_indexing_object(self, obj: Object, url: Url, event_type: IndexerCallbackEventType) -> bool: ...
    def add_indexing_object(self, obj: Object, url: Url) -> bool:
        """Adds a URL to the wait list (if it's considerable)"""
    def should_consider_url(self, url: Url) -> bool:
        """Whether the indexer should consider the given URL for indexing"""
    def should_consider_object(self, obj: Object) -> bool:
        """Only consider registered types that are derived from the constrain_to_type"""
    def start(self) -> None: ...
    rows: Incomplete
    row_count: Incomplete
    def ensure_dependent_properties(self) -> None:
        '''The rows of an IndexingTable are considered dependent properties and this is where the table is populated
        with the objects from the indexed URLs

        IndexingTable deviates from the immutability of the Table class and repeated calls to this function will
        re-populate the table with the latest indexed data.

        A call to this function is a no-op if no new data is available, when the table is queried it will simply return
        the last populated index.

        If new data is available, from indexing or "fast-track", it will re-populate the table with the new data.
        '''
    def append_row(self, row: Any, location_index: int) -> None:
        """Register row in owned row list"""
    def __len__(self) -> int: ...
    def stop(self) -> None: ...
    def wait_for_complete_index(self, timeout: float = 0.0) -> bool:
        """Wait for a complete indexing cycle to finish

        If timeout is 0 waits forever
        :param timeout: timeout in seconds
        :return: True if the next index is available, False if timed out
        """
    @property
    def counter(self) -> int: ...
