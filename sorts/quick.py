from typing import List


def _partition(dataset: List[int], low: int, high: int) -> int:
    pivot = dataset[high]
    index = low - 1
    for j in range(low, high):
        if dataset[j] <= pivot:
            index += 1
            dataset[j], dataset[index] = dataset[index], dataset[j]
    index += 1
    dataset[high], dataset[index] = dataset[index], dataset[high]
    return index


def _quick_sort(dataset: List[int], low: int, high: int):
    if low >= high:
        return
    index = _partition(dataset, low, high)
    _quick_sort(dataset, low, index - 1)
    _quick_sort(dataset, index + 1, high)


def quick_sort(dataset: List[int]):
    _quick_sort(dataset, 0, len(dataset) - 1)
