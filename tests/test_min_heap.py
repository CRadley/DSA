from heaps.min_heap import MinHeap


def test_min_heap():
    heap = MinHeap()
    heap.push(5)
    heap.push(6)
    heap.push(2)
    assert heap.length == 3
    assert heap.peek() == 2
    heap.push(200)
    assert heap.pop() == 2
    assert heap.pop() == 5
    assert heap.pop() == 6
