from tlc.core.url import Url as Url
from typing import Iterator

def set_bulk_data_url_prefix(prefix: Url) -> None:
    """Set the global variable for the bulk data URL prefix."""
def increment_and_get_bulk_data_url(column_name: str, suffix: str) -> Url:
    """Get the next bulk data url.

    Increment the bulk data Url index and return a Url corresponding to the given column_name and suffix, and the
    current values of the global bulk data Url prefix and index.

    :param column: The name of the part of the sample to generate the Url for.
    :param suffix: The suffix to be used for the bulk data Url.
    :return: The generated Url.
    """
def reset_bulk_data_url() -> None:
    """Reset the global bulk data Url prefix and index."""
def bulk_data_url_context(prefix: Url) -> Iterator[None]:
    """
    Context manager for bulk data Urls.

    Sets the global bulk data Url prefix to the given prefix, and resets it after the context
    manager exits.

    :param prefix: The prefix to set the global bulk data Url prefix to.
    """
