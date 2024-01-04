from tree.binary_node import BinaryNode
from typing import List


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
