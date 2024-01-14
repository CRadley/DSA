from typing import List


class MaxHeap:
    def __init__(self, arr: List[int] | None = None):
        self.heap: List[int] = [] if arr is None else arr
        self.build_max_heap()

    def _heapify_down(self, index: int):
        left_index = self.determine_left_index(index)
        right_index = self.determine_right_index(index)
        if (
            left_index <= len(self.heap) - 1
            and self.heap[left_index] > self.heap[index]
        ):
            largest_index = left_index
        else:
            largest_index = index
        if (
            right_index <= len(self.heap) - 1
            and self.heap[right_index] > self.heap[largest_index]
        ):
            largest_index = right_index
        if largest_index != index:
            self._swap(index, largest_index)
            self._heapify_down(largest_index)

    def _heapify_up(self, index: int):
        if not index:
            return
        parent_index = self.determine_parent_index(index)
        if self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def build_max_heap(self):
        indices = list(range(0, len(self.heap) // 2, 1))
        for index in indices[::-1]:
            self._heapify_down(index)

    def update_index(self, index: int, value: int):
        current = self.heap[index]
        self.heap[index] = value
        if value > current:
            self._heapify_up(index)
        elif value < current:
            self._heapify_down(index)

    @staticmethod
    def determine_parent_index(index: int) -> int:
        """
        Given an index, determine the parent index
        """
        return (index - 1) // 2

    @staticmethod
    def determine_left_index(index: int) -> int:
        """
        Given an index, determine the left hand child
        """
        return 2 * index + 1

    @staticmethod
    def determine_right_index(index: int) -> int:
        """
        Given an index, determine the right hand child
        """
        return 2 * index + 2

    def _swap(self, a: int, b: int):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def push(self, value: int):
        self.heap.append(value)
        if len(self) == 1:
            return
        self._heapify_up(len(self) - 1)

    def __len__(self) -> int:
        return len(self.heap)

    def peek(self) -> int | None:
        if len(self):
            return self.heap[0]
        return None

    def pop(self, index: int = 0) -> int | None:
        if len(self) == 0:
            return None
        if index >= len(self):
            return None
        self._swap(index, len(self) - 1)
        value = self.heap.pop()
        self._heapify_down(index)
        return value
