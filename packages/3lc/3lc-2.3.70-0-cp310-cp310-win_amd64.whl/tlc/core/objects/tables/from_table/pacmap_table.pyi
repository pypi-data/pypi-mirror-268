from _typeshed import Incomplete
from tlc.core.builtins.constants.number_roles import NUMBER_ROLE_XYZ_COMPONENT as NUMBER_ROLE_XYZ_COMPONENT, NUMBER_ROLE_XY_COMPONENT as NUMBER_ROLE_XY_COMPONENT
from tlc.core.builtins.constants.string_roles import STRING_ROLE_URL as STRING_ROLE_URL
from tlc.core.object_reference import ObjectReference as ObjectReference
from tlc.core.object_type_registry import ObjectTypeRegistry as ObjectTypeRegistry
from tlc.core.objects.table import ImmutableDict as ImmutableDict, Table as Table, TableRow as TableRow
from tlc.core.objects.tables.from_table.schema_helper import input_table_schema as input_table_schema
from tlc.core.objects.tables.in_memory_rows_table import _InMemoryRowsTable
from tlc.core.schema import BoolValue as BoolValue, DimensionNumericValue as DimensionNumericValue, Float32Value as Float32Value, Int32Value as Int32Value, Schema as Schema, StringValue as StringValue
from tlc.core.url import Scheme as Scheme, Url as Url
from typing import Any

pacmap: Incomplete
logger: Incomplete

class PaCMAPTable(_InMemoryRowsTable):
    """
    A procedural table where a column in the input table column has been has dimensionally reduced by the PaCMAP
    algorithm.
    """
    input_table_url: Incomplete
    source_embedding_column: Incomplete
    target_embedding_column: Incomplete
    retain_source_embedding_column: Incomplete
    n_components: Incomplete
    n_neighbors: Incomplete
    MN_ratio: Incomplete
    FP_ratio: Incomplete
    distance: Incomplete
    lr: Incomplete
    num_iters: Incomplete
    verbose: Incomplete
    apply_pca: Incomplete
    random_state: Incomplete
    fit_table_url: Incomplete
    model_url: Incomplete
    def __init__(self, url: Url | None = None, created: str | None = None, row_cache_url: Url | None = None, row_cache_populated: bool | None = None, input_table_url: Url | Table | None = None, source_embedding_column: str | None = None, target_embedding_column: str | None = None, retain_source_embedding_column: bool | None = None, fit_table_url: Table | Url | None = None, model_url: Url | None = None, n_components: int | None = None, n_neighbors: int | None = None, MN_ratio: float | None = None, FP_ratio: float | None = None, distance: str | None = None, lr: float | None = None, num_iters: int | None = None, verbose: bool | None = None, apply_pca: bool | None = None, random_state: int | None = None, init_parameters: Any = None) -> None: ...
