from typing import List


def linear_search(dataset: List[int], value: int) -> bool:
    """Performs a linear search on a dataset for a given value.

    Args:
        dataset: List[int]
        value: int
    Returns:
        Boolean value dependant on if the value is found in the dataset
    """
    for element in dataset:
        if value == element:
            return True
    return False
