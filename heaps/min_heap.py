from typing import List
from .utils import determine_child_indices, determine_parent_index


class MinHeap:
    def __init__(self):
        self.length = 0
        self._heap: List[int] = []

    def push(self, value: int):
        self.length += 1
        self._heap.append(value)
        if self.length == 1:
            return
        index = self.length - 1
        self._heapify_up(index)

    def _heapify_up(self, index: int):
        if not index:
            return
        parent_index = determine_parent_index(index)
        if self._heap[index] < self._heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index: int):
        left_index, right_index = determine_child_indices(index)
        if self.length <= left_index:
            return
        if self.length > right_index:
            min_child = min(self._heap[left_index], self._heap[right_index])
            min_child_index = (
                left_index if min_child == self._heap[left_index] else right_index
            )
        else:
            min_child = self._heap[left_index]
            min_child_index = left_index
        if min_child < self._heap[index]:
            self._swap(index, min_child_index)
            self._heapify_down(min_child_index)

    def pop(self) -> int | None:
        if not self.length:
            return None
        self.length -= 1
        self._swap(0, self.length)
        value = self._heap.pop()
        self._heapify_down(0)
        return value

    def peek(self) -> int | None:
        if not self.length:
            return None
        return self._heap[0]

    def _swap(self, a: int, b: int):
        self._heap[a], self._heap[b] = self._heap[b], self._heap[a]
