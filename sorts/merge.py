from typing import List, Tuple


def _divide(dataset: List[int]) -> Tuple[List[int], List[int]]:
    """
    Divides the input dataset in half, into lower and upper lists
    """
    start = 0
    end = len(dataset) - 1
    midpoint = start + (end - start) // 2
    return dataset[: midpoint + 1], dataset[midpoint + 1 :]


def _merge(dataset: List[int], lower: List[int], upper: List[int]):
    """
    Merges the sorted lower and upper lists by overwriting the input dataset
    """
    l = 0
    u = 0
    while l < len(lower) and u < len(upper):
        if lower[l] < upper[u]:
            dataset[l + u] = lower[l]
            l += 1
        else:
            dataset[l + u] = upper[u]
            u += 1
    if l < len(lower):
        for i, v in enumerate(lower[l:]):
            dataset[l + u + i] = v
    else:
        for i, v in enumerate(upper[u:]):
            dataset[l + u + i] = v


def merge_sort(dataset: List[int]):
    if len(dataset) <= 1:
        return
    lower, upper = _divide(dataset)
    merge_sort(lower)
    merge_sort(upper)
    _merge(dataset, lower, upper)
