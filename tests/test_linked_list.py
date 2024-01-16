from structures.linked_list import LinkedList


def test_linked_list():
    linked_list = LinkedList[int]()
    linked_list.append(5)
    linked_list.append(7)
    linked_list.append(9)

    assert linked_list.get(2) == 9
    assert linked_list.remove_at(1) == 7
    assert linked_list.length == 2

    linked_list.append(11)
    assert linked_list.remove_at(1) == 9
    assert linked_list.remove(9) is None
    assert linked_list.remove_at(0) == 5
    assert linked_list.remove_at(0) == 11
    assert linked_list.length == 0

    linked_list.prepend(5)
    linked_list.prepend(7)
    linked_list.prepend(9)

    assert linked_list.get(2) == 5
    assert linked_list.get(0) == 9
    assert linked_list.remove(9) == 9
    assert linked_list.length == 2
    assert linked_list.get(0) == 7
