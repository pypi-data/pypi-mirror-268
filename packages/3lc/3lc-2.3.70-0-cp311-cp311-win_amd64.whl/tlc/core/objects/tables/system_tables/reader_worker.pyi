import threading
from _typeshed import Incomplete
from tlc.core.objects.tables.system_tables.indexing import TaskCounter as TaskCounter, _UrlContent
from tlc.core.objects.tables.system_tables.indexing_worker import _UrlIndexingWorker
from tlc.core.url import Url as Url
from tlc.core.url_adapter_registry import UrlAdapterRegistry as UrlAdapterRegistry

logger: Incomplete

class _UrlReaderWorker(threading.Thread):
    '''A threaded class that periodically reads files from a _ThreadedDirectoryFileIndexer instance.

    :Example:

    ```python
    scan_urls = ["./path/to/dir", "./another/path"]
    indexer = _UrlIndexingWorker(scan_urls)
    file_reader = _UrlReaderWorker(indexer)
    file_reader.start()
    # Get the file contents
    files = file_reader.get_files()
    ```

    :param indexer: An instance of _UrlIndexingWorker which provides the index scanning.
    '''
    def __init__(self, indexing_worker: _UrlIndexingWorker, tag: str = '') -> None: ...
    def run(self) -> None:
        """Method representing the thread's activity.

        Do not call this method directly. Use the start() method instead, which will in turn call this method.
        """
    def stop(self) -> None:
        """Method to signal the thread to stop its activity.

        This doesn't terminate the thread immediately, but flags it to exit when it finishes its current iteration.
        """
    def update_files(self) -> bool:
        """Scans for new and updated files, reads their content, and stores them."""
    def get_content(self) -> tuple[dict[Url, _UrlContent], TaskCounter, TaskCounter]:
        """Returns a copy of the latest read Url contents.

        :returns: A dictionary of URL to _UrlContent instances representing the latest read contents.
        """
    @property
    def counter(self) -> TaskCounter:
        """Returns the current counter value.

        :returns: An integer representing the current counter value.
        """
    @property
    def index_counter(self) -> TaskCounter:
        """Returns the counter value of the scan that produced the current content.

        :returns: An integer representing the counter value.
        """
    @property
    def running(self) -> bool:
        """Returns the current running state."""
