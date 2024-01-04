from tree.binary_node import BinaryNode
from tree.binary_traversal import pre_order, in_order, post_order

TREE = BinaryNode(
    7,
    BinaryNode(23, BinaryNode(5, None, None), BinaryNode(4, None, None)),
    BinaryNode(3, BinaryNode(18, None, None), BinaryNode(21, None, None)),
)


def test_pre_order_traversal():
    assert pre_order(TREE) == [7, 23, 5, 4, 3, 18, 21]


def test_in_order_traversal():
    assert in_order(TREE) == [5, 23, 4, 7, 18, 3, 21]


def test_post_order_traversal():
    assert post_order(TREE) == [5, 4, 23, 18, 21, 3, 7]
