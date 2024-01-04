from recursion.basic_example import natural_sum
import pytest


TEST_PARAMS = [
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (5, 15),
]


@pytest.mark.parametrize("value,expected", TEST_PARAMS)
def test_basic_example(value, expected):
    assert natural_sum(value) == expected
