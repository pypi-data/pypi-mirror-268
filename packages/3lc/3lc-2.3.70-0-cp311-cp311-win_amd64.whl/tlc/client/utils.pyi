from _typeshed import Incomplete
from collections.abc import Iterable, Iterator
from torch.utils.data import Dataset as Dataset
from torch.utils.data.sampler import Sampler
from typing import Any, Callable, Generator

def bytes2str(obj: bytes) -> str: ...
def str2bytes(s: str) -> bytes: ...
def take(iterator: Iterator, batch_size: int) -> list: ...
def batched_iterator(iterator: Iterable, batch_size: int) -> Iterator[list]: ...

class SubsetSequentialSampler(Sampler[int]):
    """Samples elements sequentially from a given list of indices."""
    indices: Incomplete
    def __init__(self, indices: list[int]) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...

class RangeSampler(Sampler[int]):
    """Samples elements sequentially from a range"""
    end: Incomplete
    start: Incomplete
    step: Incomplete
    def __init__(self, end: int, start: int = 0, step: int = 1) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...

def without_transforms(dataset: Dataset) -> Generator[Callable | None, None, None]:
    """Ensures that, if the dataset is a Torchvision dataset, its transforms are temporarily removed.

    :param dataset: The dataset to temporarily remove transforms from.
    """
def standardized_transforms(transforms: Callable[..., Any]) -> Callable[[Any], Any]:
    """Create a new transforms function which takes the whole sample as its only argument,
    rather than destructuring it.

    :param transforms: The transforms function to standardize.
    :return: The standardized transforms function.
    """
