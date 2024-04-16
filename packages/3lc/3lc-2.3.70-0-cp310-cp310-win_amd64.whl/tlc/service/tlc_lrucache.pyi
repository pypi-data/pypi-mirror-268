from _typeshed import Incomplete
from pydantic import BaseModel
from starlite.cache.base import CacheBackendProtocol
from typing import Any, Callable, Dict, NamedTuple

LRU_STATS_KEY: str

class LRUCacheBackendConfig(BaseModel):
    """LRUCache backend configuration."""
    max_entries: int
    max_memory_in_bytes: int
    time_out_in_seconds: float

class LRUCacheBackend(CacheBackendProtocol):
    """In-memory LRU cache backend."""
    def __init__(self, config: LRUCacheBackendConfig) -> None:
        """Initialize ``LRUCacheBackend``"""
    async def get(self, key: str) -> Any: ...
    async def set(self, key: str, value: Any, expiration: int) -> None: ...
    async def delete(self, key: str) -> None: ...
    async def delete_all(self) -> None: ...

def LRUFuncCache(max_entries: int, max_memory_in_bytes: int, time_threshold_in_seconds: float, time_out_in_seconds: float = 0.0) -> Callable:
    """Decorator to add an LRU cache to a function.

    The decorator can control the number of cache slots (max_entries) and how much memory to use for cached element
    (max_memory).

    In addition, the decorator can set how long a function execution must take before the result is cached
    (time_threshold), to avoid caching results that are fast to compute or retrieve, thus only using the cache for
    slower items.

    The time_out parameter can be used to set how long each cached item should remain valid. If set to 0, the items will
    never expire.

    """

class LRUCache:
    """LRU cache where you can control how many slots are available, maximum memory to use for the cache, and a cache
    time out for the items.

    The stats() method will return a dictionary of important statistics about the cache.
    The clear() method will clear the cache and reset all statistics.
    """

    class LRUEntry(NamedTuple):
        timestamp: Incomplete
        value: Incomplete
    cache: Incomplete
    max_entries: Incomplete
    max_memory: Incomplete
    time_out: Incomplete
    def __init__(self, max_entries: int, max_memory: int, time_out: float = 0.0) -> None: ...
    def get(self, key: Any) -> Any: ...
    def set(self, key: Any, value: bytes) -> None: ...
    def delete(self, key: Any) -> None: ...
    def remove_oldest_item(self) -> None: ...
    current_memory_usage: int
    hits: int
    misses: int
    inserts: int
    evictions_slots: int
    evictions_time: int
    evictions_memory: int
    def clear(self) -> None: ...
    def stats(self) -> Dict[str, int]: ...
