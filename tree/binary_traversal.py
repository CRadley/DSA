from tree.binary_node import BinaryNode
from typing import List
from structures.queue import Queue


def pre_order(node: BinaryNode | None) -> List[int]:
    if node is None:
        return []
    elements = []
    elements.append(node.value)
    elements.extend(pre_order(node.left))
    elements.extend(pre_order(node.right))
    return elements


def in_order(node: BinaryNode | None) -> List[int]:
    if node is None:
        return []
    elements = []
    elements.extend(in_order(node.left))
    elements.append(node.value)
    elements.extend(in_order(node.right))
    return elements


def post_order(node: BinaryNode | None) -> List[int]:
    if node is None:
        return []
    elements = []
    elements.extend(post_order(node.left))
    elements.extend(post_order(node.right))
    elements.append(node.value)
    return elements


def tree_level_order(node: BinaryNode | None) -> List[int]:
    """
    Breadth First Search
    """
    queue = Queue()
    queue.enqueue(node)
    values = []
    while queue:
        current = queue.deque()
        if current is None:
            continue
        values.append(current.value)
        queue.enqueue(current.left)
        queue.enqueue(current.right)
    return values


def breadth_first_search(node: BinaryNode | None, value: int) -> List[int]:
    """
    Breadth First Search
    """
    queue = Queue()
    queue.enqueue(node)
    while queue:
        current = queue.deque()
        if current is None:
            continue
        if current.value == value:
            return True
        queue.enqueue(current.left)
        queue.enqueue(current.right)
    return False


def compare_binary_trees(a: BinaryNode | None, b: BinaryNode | None) -> bool:
    """
    Compare two binary trees in terms of shape and structure.
    A DFS is search is used as this is shape preserving
    """
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False
    elif a.value != b.value:
        return False
    return compare_binary_trees(a.left, b.left) and compare_binary_trees(
        a.right, b.right
    )


def bst_insert(node: BinaryNode, value: int):
    if value > node.value:
        if node.right is None:
            node.right = BinaryNode(value, None, None)
        else:
            bst_insert(node.right, value)
    else:
        if node.left is None:
            node.left = BinaryNode(value, None, None)
        else:
            bst_insert(node.left, value)


def bst_delete(node: BinaryNode, value: int):
    """
    Case 0) 0 children - remove
    Case 1) 1 child - Set parent node to child
    Case 2) Find smallest on large side, Find largest on small side. This will then simplify to either Case 0 or 1
    """


def dfs_on_bst(node: BinaryNode | None, value: int) -> bool:
    if node is None:
        return False
    elif node.value == value:
        return True
    if node.value < value:
        return dfs_on_bst(node.right, value)
    return dfs_on_bst(node.left, value)
