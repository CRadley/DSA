from ._node import _Node


class Stack:
    """Basic Stack Data Structure

    Attributes:
        length (int): The current length of the queue
    """

    def __init__(self):
        self.length = 0
        self._head: _Node = None

    def add(self, value: int):
        """Adds the value to the top of the stack

        Args:
            value (int): The value to be added to the queue
        """
        node = _Node(value)
        if self._head:
            node.next = self._head
        self._head = node
        self.length += 1

    def pop(self) -> int | None:
        """Removes the _Node at the top the stack, returns the value stored within it.
        If the queue is empty, None is returned

        Returns:
            int | None: The value of the dequed head node
        """
        if not self._head:
            return None
        head = self._head
        self._head = head.next
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
