from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class HashMap(Generic[K, V]):
    def __init__(self, *, size: int = 10000):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def set(self, key: K, value: V):
        hash_index = self._determine_hash_index(key)
        self.buckets[hash_index].append((key, value))

    def get(self, key: K) -> V:
        hash_index = self._determine_hash_index(key)
        try:
            return next(v for k, v in self.buckets[hash_index] if key == k)
        except StopIteration:
            raise KeyError(f"{key} not found in HashMap") from None

    def unset(self, key: K) -> V:
        hash_index = self._determine_hash_index(key)
        try:
            index = next(
                i for i, (k, _) in enumerate(self.buckets[hash_index]) if key == k
            )
            return self.buckets[hash_index].pop(index)
        except StopIteration:
            raise KeyError(f"{key} not found in HashMap") from None

    def _determine_hash_index(self, key: K) -> int:
        return hash(key) % self.size
