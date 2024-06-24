from sorts import bubble_sort, quick_sort, selection_sort, insertion_sort, merge_sort, counting_sort


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


def test_merge_sort():
    data = [14, 7, 3, 12, 9, 11, 6, 2]
    merge_sort(data)
    assert data == [2, 3, 6, 7, 9, 11, 12, 14]



def test_counting_sort():
    data = [4, 2, 2, 8, 3, 3, 1]
    counting_sort(data)
    assert data == [1, 2, 2, 3, 3, 4, 8]
