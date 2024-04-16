from _typeshed import Incomplete
from torch.utils.data import Sampler
from typing import Iterator, Sequence

class InfiniteWeightedRandomSampler(Sampler):
    """A PyTorch Sampler subclass that provides an infinite stream of sample indices.

    This class is a wrapper around PyTorch's WeightedRandomSampler, and it samples
    with replacement from a given set of weights. Unlike the standard
    WeightedRandomSampler, however, this class can iterate indefinitely over the
    dataset indices.

    When used in a DataLoader, an epoch will see `num_samples` samples, which are
    drawn according to the provided weights. At the end of each epoch, sampling
    continues from the same distribution without interruption, allowing for
    continuous, indefinite sampling.

    :param weights: A sequence of weights, not necessarily summing to 1, associated with each item, i.e.,
    the probability of each item to be sampled.
    :param num_samples: Number of samples to draw in one epoch.

    :yields: An index that has been sampled according to the distribution defined by `weights`.

    :::{warning}
    Be cautious when using this sampler, as the 'infinite' nature of this sampler can cause infinite loops if not
    handled properly. For example, `[x for x in sampler]` will never terminate.
    :::
    """
    sampler: Incomplete
    num_samples: Incomplete
    def __init__(self, weights: Sequence[float], num_samples: int) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...
