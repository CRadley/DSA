from heaps.max_heap import MaxHeap


def test_max_heap():
    heap = MaxHeap()
    heap.push(5)
    heap.push(6)
    heap.push(2)
    assert heap.length == 3
    heap.push(1)
    assert heap.peek() == 6
    assert heap.pop() == 6
    assert heap.pop() == 5
    assert heap.pop() == 2
