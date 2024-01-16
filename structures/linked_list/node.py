from typing import Generic, TypeVar, Self

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None
        self.prev: Node[T] | None = None
