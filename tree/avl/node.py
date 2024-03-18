from typing import Self


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.left: Self | None = None
        self.right: Self | None = None

    @property
    def number_of_children(self) -> int:
        return (self.left is not None) + (self.right is not None)

    @property
    def height(self) -> None:
        return 1 + max(
            self.left.height if self.left else 0, self.right.height if self.right else 0
        )

    @property
    def balance_factor(self) -> int:
        return (self.left.height if self.left else 0) - (
            self.right.height if self.right else 0
        )
    