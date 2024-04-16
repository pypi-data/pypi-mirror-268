from _typeshed import Incomplete
from tlc.client.sample_type import SampleType as SampleType, _SampleTypeStructure
from tlc.core.builtins.types import MetricData as MetricData, MetricTableInfo as MetricTableInfo
from tlc.core.objects.table import Table as Table
from tlc.core.objects.tables.from_url import TableFromParquet as TableFromParquet
from tlc.core.schema import Schema as Schema
from tlc.core.schema_helper import SchemaHelper as SchemaHelper
from tlc.core.url import Url as Url
from tlc.core.url_adapter import IfExistsOption as IfExistsOption
from tlc.core.url_adapter_registry import UrlAdapterRegistry as UrlAdapterRegistry
from typing import Literal, Mapping, MutableMapping

logger: Incomplete
COLUMN_NAME_REGEX: Incomplete

class TableWriter:
    '''A class for writing batches of rows to persistent storage.

    This class is primarily used for writing data in a structured format to parquet files. It supports
    batching of data and managing the schema of the columns.

    :Example:

    ```python
    table_writer = TableWriter(
        project_name="My Project",
        dataset_name="My Dataset",
        table_name="My Table"
    )
    table_writer.add_batch({"column1": [1, 2, 3], "column2": ["a", "b", "c"]})
    table_writer.add_row({"column1": 4, "column2": "d"})
    table = table_writer.finalize()
    ```
    '''
    write_option: Incomplete
    buffer: Incomplete
    max_length: Incomplete
    override_column_schemas: Incomplete
    url: Incomplete
    def __init__(self, table_name: str = ..., dataset_name: str = ..., project_name: str = ..., column_schemas: Mapping[str, _SampleTypeStructure] | None = None, if_exists: Literal['overwrite', 'rename', 'raise'] = 'rename', *, table_url: Url | str | None = None) -> None:
        '''Initialize a TableWriter.

        :param table_name: The name of the table, defaults to "table".
        :param dataset_name: The name of the dataset, defaults to "default-dataset".
        :param project_name: The name of the project, defaults to "default-project".
        :param column_schemas: Optional schemas to override the default inferred column schemas.
        :param table_url: An optional url to manually specify the Url of the written table. Mutually exclusive with
            table_name, dataset_name, and project_name.
        '''
    def add_row(self, table_row: MutableMapping[str, MetricData]) -> None:
        """Add a single row to the table being written.

        :param table_row: A dictionary mapping column names to values.
        """
    def add_batch(self, table_batch: MutableMapping[str, MetricData]) -> None:
        """Add a batch of rows to the buffer for writing.

        This method validates the consistency of the batch and appends it to the buffer. When the buffer reaches
        its maximum size, it is automatically flushed to disk.

        :param table_batch: A dictionary mapping column names to lists of values.
        :raises ValueError: If the columns in the batch have unequal lengths or mismatch with existing columns.
        """
    def clear(self) -> None:
        """Clear the buffer and reset the internal state."""
    def finalize(self) -> Table:
        """Write all added batches to disk and return the written table."""
