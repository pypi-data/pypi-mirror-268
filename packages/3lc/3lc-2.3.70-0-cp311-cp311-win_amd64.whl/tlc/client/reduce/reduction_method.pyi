import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from tlc.core.builtins.constants.number_roles import NUMBER_ROLE_NN_EMBEDDING as NUMBER_ROLE_NN_EMBEDDING
from tlc.core.objects.table import Table as Table
from tlc.core.schema import NumericValue as NumericValue, Schema as Schema
from tlc.core.url import Url as Url
from tlc.core.url_adapter_registry import UrlAdapterRegistry as UrlAdapterRegistry
from typing import Generic, TypedDict

class ReducerArgs(TypedDict, total=False):
    """Arguments specific to the reduction method."""

class ReductionMethod(ABC, Generic[_ReducerArgsType], metaclass=abc.ABCMeta):
    """Perform dimensionality reduction on columns of tables.

    Dimensionality reduction is accomplished by creating derived tables of the appropriate
    type (e.g., UMAPTable) which apply the reduction method to the input tables.

    :params reducer_args: A dictionary of arguments which are specific to the reduction method.
    """
    reducer_args: Incomplete
    def __init__(self, reducer_args: _ReducerArgsType | None = None) -> None: ...
    @abstractmethod
    def default_args(self) -> _ReducerArgsType: ...
    @abstractmethod
    def fit_and_apply_reduction(self, producer: Table, consumers: list[Table]) -> dict[Url, Url]: ...
    @abstractmethod
    def fit_reduction_method(self, table: Table, column: str) -> Url: ...
    @abstractmethod
    def apply_reduction_method(self, table: Table, fit_table_url: Url, column: str) -> Url | None: ...
