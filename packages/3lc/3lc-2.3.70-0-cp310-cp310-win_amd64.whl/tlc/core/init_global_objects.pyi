from tlc.core.objects.mutable_objects.configuration import Configuration as Configuration
from tlc.core.objects.tables.system_tables import LogTable as LogTable, RunIndexingTable as RunIndexingTable, TableIndexingTable as TableIndexingTable
from tlc.core.url import UrlAliasRegistry as UrlAliasRegistry
from tlc.core.utils.telemetry import Telemetry as Telemetry

def init_global_objects() -> None:
    """Initialize all global singleton objects"""
