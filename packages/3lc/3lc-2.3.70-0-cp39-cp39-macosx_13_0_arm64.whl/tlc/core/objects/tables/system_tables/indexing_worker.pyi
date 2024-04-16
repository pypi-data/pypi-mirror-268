import threading
from _typeshed import Incomplete
from tlc.core.objects.tables.system_tables.indexing import TaskCounter as TaskCounter, _ScanIterator, _UrlIndex
from tlc.core.url import Url as Url

logger: Incomplete

class _UrlIndexingWorker(threading.Thread):
    '''A threaded class that periodically indexes files in specified directories.

    This class extends the Python threading.Thread class to allow the indexing operation to run
    in its own thread.

    :Example:

    ```python
    scan_urls = ["./path/to/dir", "./another/path"]
    indexer = _UrlIndexingWorker(scan_urls, file_extensions=[".json", ".csv"], interval=120)
    indexer.start()
    # The thread runs in the background. Call get_index() to get the latest result.
    current_index = indexer.get_index()
    ```

    :param scan_urls: A list of URLs of directories to scan.
    :param file_extensions: A list of file extensions to consider while scanning. Default is [".json"].
    :param interval: Time interval (in seconds) between subsequent scans.
    '''
    def __init__(self, index_iterator: _ScanIterator, interval_wait: float = 1.0, tag: str = '') -> None: ...
    def set_scan_urls(self, scan_urls: list[Url], sub_indexer: int) -> None: ...
    def run(self) -> None:
        """Method representing the thread's activity.

        Do not call this method directly. Use the start() method instead, which will in turn call this method.
        """
    def stop(self) -> None:
        """Method to signal the thread to stop its activity.

        This doesn't terminate the thread immediately, but flags it to exit when it finishes its current iteration.
        """
    def handle_scan(self, new_scan: list[_UrlIndex]) -> dict[Url, _UrlIndex] | None:
        """Checks a newly scanned index for changes and returns an optionally updated index"""
    def get_index(self) -> tuple[dict[Url, _UrlIndex], TaskCounter]:
        """Returns the latest Url index result from the scan.

        :returns: A list of _UrlIndex instances representing the latest scan results.
        """
    @property
    def counter(self) -> TaskCounter:
        """Returns the current counter value."""
    def running(self) -> bool:
        """Returns the current running state."""
