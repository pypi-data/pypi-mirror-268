import torch
from _typeshed import Incomplete
from tlc.client.torch.metrics.metrics_collectors.metrics_collector_base import MetricsCollector as MetricsCollector
from tlc.client.torch.metrics.predictor import PredictorOutput as PredictorOutput
from tlc.core.builtins.constants.number_roles import NUMBER_ROLE_NN_EMBEDDING as NUMBER_ROLE_NN_EMBEDDING
from tlc.core.builtins.types import MetricData as MetricData, SampleData as SampleData
from tlc.core.schema import DimensionNumericValue as DimensionNumericValue, Float32Value as Float32Value, Schema as Schema
from typing import Callable

logger: Incomplete

class EmbeddingsMetricsCollector(MetricsCollector):
    '''Metrics collector that prepares hidden layer activations for storage.

    Assumes that the provided `predictor_output` contains a dictionary of hidden layers, where the keys are the layer
    indices and the values are the activations of the layer.

    Returns metrics batches with a column named "embeddings_{layer}" for each layer provided.

    The activations of intermediate modules can have arbitrary shape, and in order to write them to a Table, they must
    be reshaped to 1D arrays (flattened).

    Will ensure all layers are flattened according to `reshape_strategy[layer]`.
    '''
    def __init__(self, layers: list[int] | None = None, reshape_strategy: dict[int, str] | dict[int, Callable[[torch.Tensor], torch.Tensor]] | None = None) -> None:
        '''Create a new embeddings metrics collector.

        :param layers: The layers to collect embeddings from. If not provided, all layers provided by the model will be
            collected.
        :param reshape_strategy: The reshaping strategy to use for each layer. Can be either "mean", which takes the
            mean across all non-first dimensions (excluding batch dimension), or "flatten", which flattens all
            dimensions after the batch dimension. Could also be a callable which performs the flattening.
        '''
    def compute_metrics(self, _1: SampleData, predictor_output: PredictorOutput) -> dict[str, MetricData]:
        """Collect and flatten hidden layer activations from model outputs.

        :param predictor_output: The outputs from a {class}`Predictor<tlc.client.torch.metrics.Predictor>`.
        :returns: A dictionary of column names to batch of flattened embeddings.
        """
    @property
    def column_schemas(self) -> dict[str, Schema]: ...
