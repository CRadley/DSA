from typing import Generic, TypeVar, get_args

K = TypeVar("K")
V = TypeVar("V")


class HashMap(Generic[K, V]):
    def __init__(self, *, size: int = 10000):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def set(self, key: K, value: V):
        if not self._validate_key_type(key):
            raise TypeError
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

    def _validate_key_type(self, key: K):
        key_type = get_args(self.__orig_bases__[0])[0]
        return isinstance(key_type, TypeVar) or isinstance(key, key_type)

    def _validate_value_type(self, value: V):
        value_type = get_args(self.__orig_bases__[0])[1]
        return isinstance(value_type, TypeVar) or isinstance(value, value_type)


class DerivedHashMap(HashMap[str, int]):
    """
    This inherited class is required to have runtime type checking
    for K and V
    """
