from structures.hash_map import HashMap
import pytest


def test_hash_map():
    hash_map = HashMap(size=10)
    hash_map.set("foo", "bar")
    hash_map.set("bar", "baz")
    assert hash_map.get("foo") == "bar"
    assert hash_map.get("bar") == "baz"
    with pytest.raises(KeyError):
        hash_map.get("baz")
    hash_map.unset("bar")
    with pytest.raises(KeyError):
        hash_map.get("bar")
    with pytest.raises(KeyError):
        hash_map.unset("bar")
