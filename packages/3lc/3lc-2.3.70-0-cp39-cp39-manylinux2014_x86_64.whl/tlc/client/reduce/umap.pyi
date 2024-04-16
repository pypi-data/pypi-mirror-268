from _typeshed import Incomplete
from tlc.client.reduce.reduction_method import ReducerArgs as ReducerArgs, ReductionMethod as ReductionMethod
from tlc.core.objects.table import Table as Table
from tlc.core.objects.tables.from_table.umap_table import UMAPTable as UMAPTable
from tlc.core.schema_helper import SchemaHelper as SchemaHelper
from tlc.core.url import Url as Url

logger: Incomplete

class UMapTableArgs(ReducerArgs, total=False):
    """Arguments specific to the UMAP reduction method.

    See {class}`UMAPTable<tlc.core.objects.tables.from_table.umap_table.UMAPTable>` for more information.
    """
    n_components: int
    standard_scaler_normalize: bool
    n_neighbors: int
    metric: str
    min_dist: float
    source_embedding_column: str | None
    target_embedding_column: str | None
    retain_source_embedding_column: bool
    n_jobs: int

class UMapReduction(ReductionMethod[UMapTableArgs]):
    """Perform dimensionality reduction on columns of tables using the UMAP algorithm.

    :params reducer_args: A dictionary of arguments which are specific to the reduction method.
    """
    def default_args(self) -> UMapTableArgs:
        """Returns the default arguments for the UMAP reduction method."""
    def fit_and_apply_reduction(self, producer: Table, consumers: list[Table]) -> dict[Url, Url]: ...
    def fit_reduction_method(self, table: Table, column: str) -> Url:
        """Fits a UMAPTable and returns the model URL"""
    def apply_reduction_method(self, table: Table, fit_table_url: Url, column: str) -> Url | None: ...
