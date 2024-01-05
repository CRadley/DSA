from structures.trie import TrieSoftDelete, TrieHardDelete


def test_trie_soft_delete():
    trie = TrieSoftDelete()
    assert not len(trie)
    trie.insert("foo")
    trie.insert("fool")
    trie.insert("foolish")
    trie.insert("bar")
    assert len(trie) == 10
    assert trie.find("fo") == [
        "foo",
        "fool",
        "foolish",
    ]
    assert trie.find("b") == ["bar"]
    trie.delete("foolish")
    assert trie.find("fo") == [
        "foo",
        "fool",
    ]
    assert len(trie) == 10
    assert trie.find("b") == ["bar"]
    trie.insert("foolish")
    assert trie.find("fo") == [
        "foo",
        "fool",
        "foolish",
    ]


def test_trie_hard_delete():
    trie = TrieHardDelete()
    assert not len(trie)
    trie.insert("foo")
    trie.insert("fool")
    trie.insert("foolish")
    trie.insert("bar")
    assert len(trie) == 10
    assert trie.find("fo") == [
        "foo",
        "fool",
        "foolish",
    ]
    assert trie.find("b") == ["bar"]
    trie.delete("foolish")
    assert trie.find("fo") == [
        "foo",
        "fool",
    ]
    assert len(trie) == 7
    assert trie.find("b") == ["bar"]
    trie.insert("foolish")
    assert trie.find("fo") == [
        "foo",
        "fool",
        "foolish",
    ]
