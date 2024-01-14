from typing import Any, Self
from .hash_map import HashMap


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Self | None = None
        self.prev: Self | None = None


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.length = 0
        self.head: Node | None = None
        self.tail: Node | None = None
        self.lookup = HashMap()
        self.reverse_lookup = HashMap()
        self.capacity = capacity

    def update(self, key: Any, value: Any):
        try:
            node: Node = self.lookup.get(key)
            self.detach(node)
            self.prepend(node)
            return
        except KeyError:
            # Key not found in hash_map so it and the node will be created
            # I'm not sure I like the way the control flow is working here...
            # I blame past me on the HashMap implementation
            node = Node(value)
            self.length += 1
            self.prepend(node)
            self.trim_cache()
            self.lookup.set(key, node)
            self.reverse_lookup.set(node, key)

    def get(self, key: Any) -> Any:
        try:
            node: Node = self.lookup.get(key)
            self.detach(node)
            self.prepend(node)
            return node.value
        except KeyError as key_error:
            raise key_error

    def detach(self, node: Node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev
        node.next = None
        node.prev = None

    def prepend(self, node: None):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def trim_cache(self):
        if self.length <= self.capacity:
            return
        tail = self.tail
        self.detach(tail)
        key = self.reverse_lookup.get(tail)
        self.lookup.unset(key)
        self.reverse_lookup.unset(tail)
        self.length -= 1
