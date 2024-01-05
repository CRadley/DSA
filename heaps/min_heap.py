from typing import List


def determine_child_indices(n: int) -> (int, int):
    return 2 * n + 1, 2 * n + 2


def determine_parent_index(n: int) -> int:
    return (n - 1) // 2


class MinHeap:
    def __init__(self):
        self.length = 0
        self._heap: List[int] = []

    def push(self, value: int):
        self.length += 1
        self._heap.append(value)
        if self.length == 1:
            return
        i = self.length - 1
        p = determine_parent_index(i)
        while self._heap[i] < self._heap[p] and i > 0:
            self._swap(i, p)
            i = p

    def pop(self) -> int | None:
        if not self.length:
            return None
        self.length -= 1
        self._swap(0, self.length)
        value = self._heap.pop()
        i = 0
        l, r = determine_child_indices(i)
        while True:
            if self.length > r:
                min_child = min(self._heap[l], self._heap[r])
                min_child_index = l if min_child == self._heap[l] else r
            elif self.length == r:
                min_child = self._heap[l]
                min_child_index = l
            elif self.length <= l:
                break
            if min_child < self._heap[i]:
                self._swap(i, min_child_index)
                i = min_child_index
                l, r = determine_child_indices(i)
                continue
            break
        return value

    def peek(self) -> int | None:
        if not self.length:
            return None
        return self._heap[0]

    def _swap(self, a: int, b: int):
        self._heap[a], self._heap[b] = self._heap[b], self._heap[a]
