from ._node import _Node


class Queue:
    """Basic Queue Data Structure

    Attributes:
        length (int): The current length of the queue
    """

    def __init__(self):
        self.length = 0
        self._head: _Node = None
        self._tail: _Node = None

    def enqueue(self, value: int):
        """Adds the value to the end of the queue

        Args:
            value (int): The value to be added to the queue
        """
        node = _Node(value)
        if not self._head:
            self._head = node
        if self._tail:
            self._tail.next = node
        self._tail = node
        self.length += 1

    def deque(self) -> int | None:
        """Removes the _Node at the start of the queue, returns the value stored within it.
        If the queue is empty, None is returned

        Returns:
            int | None: The value of the dequed head node
        """
        if not self._head:
            return None
        head = self._head
        self._head = self._head.next
        self.length -= 1
        return head.value

    def peek(self) -> int | None:
        """Looks at the current head value and returns it.

        Returns:
            int | None: The current value at the head of the queue
        """
        if self._head is not None:
            return self._head.value
        return None
