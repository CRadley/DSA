import pytest
from heaps.maxheap import MaxHeap


@pytest.mark.parametrize("index,expected", [(0, -1), (4, 1), (5, 2)])
def test_determine_parent_index(index: int, expected: int):
    assert MaxHeap.determine_parent_index(index) == expected


@pytest.mark.parametrize("index,expected", [(0, 1), (1, 3), (2, 5)])
def test_determine_left_index(index: int, expected: int):
    assert MaxHeap.determine_left_index(index) == expected


@pytest.mark.parametrize("index,expected", [(0, 2), (1, 4), (2, 6)])
def test_determine_right_index(index: int, expected: int):
    assert MaxHeap.determine_right_index(index) == expected


def test_build_max_heap():
    arr = [10, 20, 25, 6, 12, 15, 4, 16]
    max_heap = MaxHeap(arr)
    assert max_heap.heap == [25, 20, 15, 16, 12, 10, 4, 6]


def test_build_max_heap_2():
    arr = [5, 4, 9, 7, 19, 8, 17, 2, 6, 5, 21]
    max_heap = MaxHeap(arr)
    assert max_heap.heap == [21, 19, 17, 7, 5, 8, 9, 2, 6, 5, 4]


def test_update_max_heap_index():
    max_heap = MaxHeap([21, 19, 17, 7, 5, 8, 9, 2, 6, 5, 4])
    max_heap.update_index(7, 22)
    assert max_heap.heap == [22, 21, 17, 19, 5, 8, 9, 7, 6, 5, 4]


def test_max_heap():
    heap = MaxHeap()
    heap.push(5)
    heap.push(6)
    heap.push(2)
    assert len(heap) == 3
    heap.push(1)
    assert heap.peek() == 6
    assert heap.pop() == 6
    assert heap.pop() == 5
    assert heap.pop() == 2


def test_max_heap_2():
    heap = MaxHeap()
    heap.push(5)
    heap.push(6)
    heap.push(2)
    assert len(heap) == 3
    heap.push(1)
    assert heap.peek() == 6
    assert heap.pop(1) == 5
    assert heap.pop() == 6
    assert heap.pop() == 2
