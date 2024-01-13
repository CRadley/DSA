from typing import List
from structures.graphs import WeightedAdjacencyList
from math import inf


def has_unvisited(seen: List[bool], dists: List[int | float]) -> bool:
    return any(dists[i] < inf and not s for i, s in enumerate(seen))


def get_lowest_unvisited(seen: List[bool], dists: List[int | float]) -> int:
    index = -1
    lowest_distance = inf
    for i, s in enumerate(seen):
        if s:
            continue
        if dists[i] < lowest_distance:
            lowest_distance = dists[i]
            index = i
    return index


def shortest_path(graph: WeightedAdjacencyList, source: int, target: int) -> List[int]:
    """
    Slow running time. Should implement a MinHeap so that the "seen" array is not needed.
    """
    prev = [-1 for _ in range(len(graph))]
    seen = [False for _ in range(len(graph))]
    dists = [0 if i == source else inf for i in range(len(graph))]
    while has_unvisited(seen, dists):
        current = get_lowest_unvisited(seen, dists)
        seen[current] = True
        for edge in graph[current]:
            if seen[edge.to]:
                continue
            distance = edge.weight + dists[current]
            if distance < dists[edge.to]:
                dists[edge.to] = distance
                prev[edge.to] = current
    if prev[target] == -1:
        return None
    path = []
    current = target
    while prev[current] != -1:
        path.append(current)
        current = prev[current]
    path.append(current)
    return path[::-1]
