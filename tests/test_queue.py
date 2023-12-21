from structures import Queue


def test_queue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)
    assert queue.deque() == 5
    assert queue.length == 2
    assert queue.peek() == 7
