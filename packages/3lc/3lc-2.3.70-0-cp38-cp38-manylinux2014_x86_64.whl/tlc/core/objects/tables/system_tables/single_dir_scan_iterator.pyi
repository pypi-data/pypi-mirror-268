from _typeshed import Incomplete
from tlc.core.objects.tables.system_tables.indexing import _BlacklistExceptionHandler, _ScanIterator, _UrlIndex
from tlc.core.url import Url as Url
from tlc.core.url_adapter_registry import UrlAdapterRegistry as UrlAdapterRegistry
from typing import Generator

logger: Incomplete

class _SingleDirScanIterator(_ScanIterator):
    """Private class for indexing Urls in a single directory.

    :param dir_url: The URL of the directory to iterate over.
    """
    def __init__(self, scan_urls: list[Url], extensions: list[str], tag: str, create_default_dirs: bool | None, blacklist_config: list[_BlacklistExceptionHandler] | None) -> None: ...
    @staticmethod
    def single_dir_readme() -> str: ...
    def scan(self) -> Generator[_UrlIndex, None, None]: ...
    def scan_url(self, dir_url: Url) -> Generator[_UrlIndex, None, None]: ...
    def scan_package_url(self, dir_url: Url) -> Generator[_UrlIndex, None, None]: ...
