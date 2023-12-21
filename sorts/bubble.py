from typing import List


def bubble_sort(dataset: List[int]):
    """Performs a mutating bubble sort on an input dataset.

    Args:
        dataset: List[int]
    """
    for i, _ in enumerate(dataset):
        for j in range(len(dataset[i:]) - 1):
            if dataset[j] > dataset[j + 1]:
                dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
