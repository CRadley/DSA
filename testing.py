from typing import Any, Self


class Item:
    def __init__(self, priority: int, item: Any) -> None:
        self.priority = priority
        self.item = item

    def __gt__(self, other: Self) -> bool:
        return self.priority > other.priority
