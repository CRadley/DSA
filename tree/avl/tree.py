from .node import Node
from typing import List


class AVLTree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, key: int, value: int):
        if self.root is None:
            self.root = Node(key, value)
            return
        current = self.root
        stack = []
        while current:
            stack.insert(0, current)
            if key < current.key:
                if current.left is None:
                    current.left = Node(key, value)
                    break
                else:
                    current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key, value)
                    break
                else:
                    current = current.right
            else:
                current.value = value
                break
        self.rotate(stack)

    def rotate(self, stack: List[Node]):
        for node in stack:
            balance_factor = node.balance_factor
            if balance_factor == 2:
                if node.left.balance_factor == -1:
                    self._left_rotate(node.left)
                self._right_rotate(node)
            elif balance_factor == -2:
                if node.right.balance_factor == 1:
                    self._right_rotate(node.right)
                self._left_rotate(node)

    def _left_rotate(self, node: Node):
        node.left = Node(node.key, node.value)
        node.value = node.right.value
        node.key = node.right.key
        node.right = node.right.right

    def _right_rotate(self, node: Node):
        node.right = Node(node.key, node.value)
        node.value = node.left.value
        node.key = node.left.key
        node.left = node.left.left

    def pre_order_traversal(self) -> List[int]:
        keys = []
        self._pre_order_traveral(self.root, keys)
        return keys

    def _pre_order_traveral(self, node: Node, keys: List[int]):
        if node is None:
            return
        keys.append(node.key)
        self._pre_order_traveral(node.left, keys)
        self._pre_order_traveral(node.right, keys)

    def delete(self, key: int):
        if self.root is None:
            return
        self._delete(self.root, key)

    def _delete(self, node: Node, key: int) -> bool:
        if node.key == key:
            return True
        elif key < node.key and node.left is not None:
            if self._delete(node.left, key):
                match node.left.number_of_children:
                    case 0:
                        node.left = None
                    case 1:
                        if node.left.left is None:
                            node.left = node.left.left
                        else:
                            node.left = node.right.left
                    case 2:
                        s = self.find_smallest_value(node.left.right)
                        node.left.value = s
                        self._delete(node.left.right, s)
        elif key > node.key and node.right is not None:
            if self._delete(node.right, key):
                match node.right.number_of_children:
                    case 0:
                        node.right = None
                    case 1:
                        if node.right.left is None:
                            node.right = node.right.left
                        else:
                            node.right = node.right.right
                    case 2:
                        s = self.find_smallest_value(node.right.right)
                        node.right.value = s
                        self._delete(node.right.right, s)
        self.rotate([node])

    def find_smallest_value(self, node: Node) -> int:
        current = node
        while current.left is not None:
            current = current.left
        return current.value
