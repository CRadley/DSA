from typing import Self


class _Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Self | None = None
        self.prev: Self | None = None
