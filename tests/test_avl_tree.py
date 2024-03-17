from tree.avl import AVLTree


# def test_left_rotate_after_insert():
#     tree = AVLTree()
#     tree.insert(2, 2)
#     tree.insert(3, 3)
#     tree.insert(4, 4)
#     assert tree.pre_order_traversal() == [3, 2, 4], "Pre Order"
#     assert tree.in_order_traversal() == [2, 3, 4], "In Order"
#     assert tree.post_order_traversal() == [2, 4, 3], "Post Order"


def test_right_rotate():
    tree = AVLTree()
    tree.insert(4, 4)
    tree.insert(3, 3)
    tree.insert(2, 2)
    assert tree.pre_order_traversal() == [3, 2, 4]


def test_left_rotate():
    tree = AVLTree()
    tree.insert(2, 2)
    tree.insert(3, 3)
    tree.insert(4, 4)
    assert tree.pre_order_traversal() == [3, 2, 4]


def test_left_right_rotate():
    tree = AVLTree()
    tree.insert(4, 4)
    tree.insert(2, 2)
    tree.insert(3, 3)
    assert tree.pre_order_traversal() == [3, 2, 4]


def test_right_left_rotate():
    tree = AVLTree()
    tree.insert(4, 4)
    tree.insert(6, 6)
    tree.insert(5, 5)
    assert tree.pre_order_traversal() == [5, 4, 6]


def test_larger_tree():
    tree = AVLTree()
    tree.insert(5, 5)
    tree.insert(10, 10)
    tree.insert(4, 4)
    tree.insert(3, 3)
    tree.insert(2, 2)
    tree.insert(11, 11)
    tree.insert(12, 12)
    assert tree.pre_order_traversal() == [5, 3, 2, 4, 11, 10, 12]


def test_delete():
    tree = AVLTree()
    tree.insert(5, 5)
    tree.insert(2, 2)
    tree.insert(6, 6)
    tree.insert(7, 7)
    assert tree.pre_order_traversal() == [5, 2, 6, 7]
    tree.delete(2)
    assert tree.pre_order_traversal() == [6, 5, 7]
