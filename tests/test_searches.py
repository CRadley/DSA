from searches import linear_search
import pytest


params = (
    (25, True),
    (70, False),
    (81, True),
    (9713, False),
    (1, True),
    (0, False),
)


@pytest.mark.parametrize("value,expected", params)
def test_linear_search(value: int, expected: bool):
    data = [1, 3, 4, 25, 71, 81, 90, 99, 106, 893, 9712]
    assert linear_search(data, value) == expected
