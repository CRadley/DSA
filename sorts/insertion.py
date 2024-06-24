from typing import List


def insertion_sort(dataset: List[int]):
    """
    Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
    """
    for i, _ in enumerate(dataset):
        if not i:
            continue
        for j in range(1, i + 1):
            pointer = i - j
            if dataset[pointer] <= dataset[i]:
                dataset.insert(pointer + 1, dataset.pop(i))
                break
        else:
            dataset.insert(0, dataset.pop(i))
