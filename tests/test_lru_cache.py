from structures.lru_cache import LRUCache
import pytest


def test_lru_cache():
    lru = LRUCache(3)
    with pytest.raises(KeyError):
        lru.get("foo")
    lru.update("foo", 70)
    assert lru.get("foo") == 70
    lru.update("bar", 500)
    assert lru.get("bar") == 500
    lru.update("baz", 1000)
    assert lru.get("baz") == 1000

    lru.update("ball", 1111)
    assert lru.get("ball") == 1111
    with pytest.raises(KeyError):
        lru.get("foo")
