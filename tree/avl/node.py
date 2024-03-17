from typing import Self


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.left: Self | None = None
        self.right: Self | None = None
        self.height: int = 1

    @property
    def number_of_children(self) -> int:
        return (self.left is not None) + (self.right is not None)
