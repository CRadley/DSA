from typing import List


def counting_sort(dataset: List[int]):
    m = max(dataset)
    counts = [0] * (m + 1)
    for d in dataset:
        counts[d] += 1
    cumulative_counts = [sum(counts[: i + 1]) for i in range(len(counts))]
    for _, value in list(enumerate(dataset)):
        cumulative_counts[value] -= 1
        dataset[cumulative_counts[value]] = value
