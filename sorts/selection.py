from typing import List


def selection_sort(dataset: List[int]):
    """
    Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration
    and places that element at the beginning of the unsorted list.
    """
    for i, _ in enumerate(dataset):
        minumum_index = i
        for j, value in enumerate(dataset[i:]):
            if value < dataset[minumum_index]:
                minumum_index = j + i
        dataset[i], dataset[minumum_index] = dataset[minumum_index], dataset[i]
