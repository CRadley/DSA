from typing import List


def binary_search(dataset: List[int], value: int) -> bool:
    """Performs a binary search on a dataset for a given value.

    Args:
        dataset: List[int]
        value: int
    Returns:
        Boolean value dependant on if the value is found in the dataset
    """
    start = 0
    end = len(dataset)

    while start < end:
        midpoint = start + (end - start) // 2
        midpoint_value = dataset[midpoint]
        if midpoint_value == value:
            return True
        elif midpoint_value < value:
            start = midpoint + 1
        else:
            end = midpoint
    return False
