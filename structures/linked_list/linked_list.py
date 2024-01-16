from typing import Generic, TypeVar
from .node import Node

T = TypeVar("T")


class LinkedList(Generic[T]):
    def __init__(self):
        self.length = 0
        self.head: Node[T] | None = None

    def append(self, value: T):
        """
        Add a node at the end of the linked list
        """
        node = Node[T](value)
        self.length += 1
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def prepend(self, value: int):
        """
        Add a node at the start of the linked list
        """
        node = Node[T](value)
        self.length += 1
        if self.head:
            node.next = self.head
        self.head = node

    def get(self, index: int) -> T | None:
        if index >= self.length:
            return None
        current = self.head
        counter = 0
        while current:
            if index == counter:
                return current.value
            counter += 1
            current = current.next
        return None

    def remove_at(self, index: int) -> T | None:
        if index >= self.length:
            return None
        self.length -= 1
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            return value
        current = self.head
        counter = 0
        while current:
            if index - 1 == counter:
                break
            counter += 1
            current = current.next
        value = current.next.value
        if self.length == index:
            current.next = None
        else:
            current.next = current.next.next
        return value

    def remove(self, value: int) -> T | None:
        current = self.head
        prev = None
        counter = 0
        while current:
            if current.value == value:
                break
            counter += 1
            prev = current
            current = current.next
        if current is None:
            return None
        self.length -= 1
        value = current.value
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        return value
