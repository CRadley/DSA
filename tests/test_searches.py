from searches import linear_search, binary_search
import pytest


TEST_PARAMS = (
    (25, True),
    (70, False),
    (81, True),
    (9713, False),
    (1, True),
    (0, False),
)

TEST_DATA = [1, 3, 4, 25, 71, 81, 90, 99, 106, 893, 9712]


@pytest.mark.parametrize("value,expected", TEST_PARAMS)
def test_linear_search(value: int, expected: bool):
    assert linear_search(TEST_DATA, value) == expected


@pytest.mark.parametrize("value,expected", TEST_PARAMS)
def test_binary_search(value: int, expected: bool):
    assert binary_search(TEST_DATA, value) == expected
