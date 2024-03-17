from tree.binary.binary_node import BinaryNode
from tree.binary.binary_traversal import (
    pre_order,
    in_order,
    post_order,
    tree_level_order,
    breadth_first_search,
    compare_binary_trees,
    bst_insert,
    dfs_on_bst,
    binary_search_tree,
    bst_delete,
)
import pytest


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


def test_tree_level_order():
    """
    AKA BFS Order...
    """
    assert tree_level_order(TREE) == [7, 23, 3, 5, 4, 18, 21]


def test_breadth_first_search_in_tree():
    assert breadth_first_search(TREE, 7)


def test_breadth_first_search_not_in_tree():
    assert not breadth_first_search(TREE, 6)


@pytest.mark.parametrize(
    "node_a,node_b,expected",
    [
        (
            BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, None)),
            BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, None)),
            True,
        ),
        (
            BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, None)),
            BinaryNode(1, BinaryNode(2, BinaryNode(3, None, None), None), None),
            False,
        ),
    ],
)
def test_compare_binary_trees(node_a, node_b, expected):
    assert compare_binary_trees(node_a, node_b) == expected


def test_bst_insert_left():
    tree = BinaryNode(5, None, None)
    bst_insert(tree, 4)
    assert tree.left.value == 4


def test_bst_insert_left_right():
    tree = BinaryNode(5, None, None)
    bst_insert(tree, 3)
    bst_insert(tree, 4)
    assert tree.left.value == 3
    assert tree.left.right.value == 4


def test_bst_insert_right():
    tree = BinaryNode(5, None, None)
    bst_insert(tree, 7)
    assert tree.right.value == 7


def test_bst_insert_right_left():
    tree = BinaryNode(5, None, None)
    bst_insert(tree, 7)
    bst_insert(tree, 6)
    assert tree.right.value == 7
    assert tree.right.left.value == 6
    assert in_order(tree) == [5, 6, 7]


def test_dfs_on_bst():
    tree = BinaryNode(2, BinaryNode(1, None, None), BinaryNode(3, None, None))
    assert dfs_on_bst(tree, 1)
    assert dfs_on_bst(tree, 2)
    assert dfs_on_bst(tree, 3)
    assert not dfs_on_bst(tree, 4)


def test_binary_search_tree():
    tree = BinaryNode(2, BinaryNode(1, None, None), BinaryNode(3, None, None))
    assert binary_search_tree(tree, 1)
    assert binary_search_tree(tree, 2)
    assert binary_search_tree(tree, 3)
    assert not binary_search_tree(tree, 4)


def test_delete_binary_tree_case_0():
    """
    Node being deleted has no children
    """
    root = BinaryNode(
        7,
        BinaryNode(3, BinaryNode(2, None, None), BinaryNode(4, None, None)),
        BinaryNode(
            23,
            BinaryNode(18, BinaryNode(17, None, None), None),
            BinaryNode(26, BinaryNode(24, None, None), BinaryNode(29, None, None)),
        ),
    )
    expected = [2, 3, 7, 17, 18, 23, 24, 26, 29]
    bst_delete(root, 4)
    assert in_order(root) == expected


def test_delete_binary_tree_case_1():
    """
    Node being deleted has 1 child
    """
    root = BinaryNode(
        7,
        BinaryNode(3, BinaryNode(2, None, None), BinaryNode(4, None, None)),
        BinaryNode(
            23,
            BinaryNode(18, BinaryNode(17, None, None), None),
            BinaryNode(26, BinaryNode(24, None, None), BinaryNode(29, None, None)),
        ),
    )
    expected = [2, 3, 4, 7, 17, 23, 24, 26, 29]
    bst_delete(root, 18)
    assert in_order(root) == expected


def test_delete_binary_tree_case_2():
    """
    Node being deleted has 2 children
    """
    root = BinaryNode(
        7,
        BinaryNode(3, BinaryNode(2, None, None), BinaryNode(4, None, None)),
        BinaryNode(
            23,
            BinaryNode(18, BinaryNode(17, None, None), None),
            BinaryNode(26, BinaryNode(24, None, None), BinaryNode(29, None, None)),
        ),
    )
    expected = [2, 3, 4, 7, 17, 18, 24, 26, 29]
    bst_delete(root, 23)
    assert in_order(root) == expected
