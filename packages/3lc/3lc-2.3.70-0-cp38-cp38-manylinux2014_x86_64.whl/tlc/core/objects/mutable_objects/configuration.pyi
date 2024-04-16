from _typeshed import Incomplete
from tlc.core.object_type_registry import ObjectTypeRegistry as ObjectTypeRegistry
from tlc.core.objects.mutable_object import MutableObject as MutableObject
from tlc.core.schema import DictValue as DictValue, Schema as Schema, StringValue as StringValue
from tlc.core.url import Url as Url, UrlAliasRegistry as UrlAliasRegistry
from tlc.core.url_adapters import ApiUrlAdapter as ApiUrlAdapter
from tlc.core.utils.telemetry import Telemetry as Telemetry
from typing import Any

logger: Incomplete

class Configuration(MutableObject):
    """
    3LC runtime configuration.

    This singleton object contains all runtime configuration settings for this
    instance of 3LC, including

    - Current-user information
    - Network access tokens
    - Cache settings
    - Other settings
    - ...
    """
    configuration_instance: Configuration | None
    project_root_url: Incomplete
    project_scan_urls: Incomplete
    extra_table_scan_urls: Incomplete
    extra_run_scan_urls: Incomplete
    aliases: Incomplete
    sentry_dashboard_config: Incomplete
    def __init__(self, url: Url | None = None, created: str | None = None, last_modified: str | None = None, init_parameters: Any = None) -> None: ...
    @staticmethod
    def instance() -> Configuration:
        """
        Returns the singleton Configuration object
        """
