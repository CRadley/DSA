from typing import Self


class BinaryNode:
    def __init__(self, value: int, left: Self | None, right: Self | None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.value}"

    @property
    def number_of_children(self) -> int:
        return bool(self.left) + bool(self.right)
