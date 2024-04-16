import torch
import transformers
from _typeshed import Incomplete
from tlc.client.helpers import active_run as active_run
from tlc.client.session import Session as Session
from tlc.core.builtins.types import MetricData as MetricData
from tlc.core.exceptions import TLCException as TLCException
from tlc.core.objects.table import Table as Table
from tlc.core.writers import MetricsTableWriter as MetricsTableWriter
from typing import Any, Callable

class TLCTrainer(transformers.Trainer):
    """A drop-in replacement for the 🤗 transformers Trainer.

    Adds per-sample metrics collection on both the train and eval datasets every time .evaluate() is called.

    To specify what metrics to collect, pass in a function to the compute_tlc_metrics argument that takes in a batch
    of data and returns a dictionary of per-sample metrics for the batch.

    :param compute_tlc_metrics: A function that takes in a batch of data and returns a dictionary of metrics.
    :param collect_tlc_metrics_before_training: Whether to collect metrics before training starts.
    """
    collect_tlc_metrics_before_training: Incomplete
    def __init__(self, *args: Any, compute_tlc_metrics: Callable[..., dict[str, MetricData]] | None = None, collect_tlc_metrics_before_training: bool = False, **kwargs: Any) -> None: ...
    def train(self, *args: Any, **kwargs: Any) -> Any: ...
    def prediction_step(self, *args: Any, **kwargs: Any) -> tuple[torch.Tensor | None, torch.Tensor | None, torch.Tensor | None]: ...
    def evaluate(self, eval_dataset: torch.utils.data.Dataset | None = None, ignore_keys: list[str] | None = None, metric_key_prefix: str = 'eval') -> dict[str, float]: ...
