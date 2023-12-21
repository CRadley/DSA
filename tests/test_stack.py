from structures import Stack


def test_stack():
    stack = Stack()
    stack.add(5)
    stack.add(7)
    stack.add(9)
    assert stack.pop() == 9
    assert stack.length == 2
    assert stack.peek() == 7
