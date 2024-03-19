from sorts import bubble_sort, quick_sort, selection_sort, insertion_sort


BASE_DATA = [9, 3, 7, 4, 75, 154, 42]
EXPECTED = [3, 4, 7, 9, 42, 75, 154]


def test_bubble_sort():
    data = BASE_DATA[:]
    bubble_sort(data)
    assert data == EXPECTED


def test_quick_sort():
    data = BASE_DATA[:]
    quick_sort(data)
    assert data == EXPECTED


def test_selection_sort():
    data = BASE_DATA[:]
    selection_sort(data)
    assert data == EXPECTED


def test_insertion_sort():
    data = BASE_DATA[:]
    insertion_sort(data)
    assert data == EXPECTED
