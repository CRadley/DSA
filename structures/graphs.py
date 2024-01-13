from dataclasses import dataclass
from typing import List
from structures import Queue


@dataclass
class WeightedEdge:
    to: int
    weight: int


@dataclass
class Edge:
    to: int


WeightedAdjacencyMatrix = List[List[int]]
AdjacencyMatrix = List[List[bool]]
WeightedAdjacencyList = List[List[WeightedEdge]]
AdjacencyList = List[List[Edge]]


def bfs_weighted_adjacency_matrix(
    graph: WeightedAdjacencyMatrix, source: int, target: int
) -> List[int] | None:
    seen = [i == source for i in range(len(graph))]
    prev = [-1 for _ in range(len(graph))]
    queue = Queue()
    queue.enqueue(source)
    while queue:
        current = queue.deque()
        if current == target:
            break
        for index, weight in enumerate(graph[current]):
            if seen[index] or not weight:
                continue
            seen[index] = True
            prev[index] = current
            queue.enqueue(index)
    if prev[target] == -1:
        return None
    path = []
    while prev[current] != -1:
        path.append(current)
        current = prev[current]
    path.append(current)
    return path[::-1]


def walk(
    graph: WeightedAdjacencyList,
    current: int,
    target: int,
    path: List[int],
    seen: List[bool],
) -> bool:
    if seen[current]:
        return False
    path.append(current)
    if current == target:
        return True
    seen[current] = True
    for edge in graph[current]:
        if walk(graph, edge.to, target, path, seen):
            return True
    path.pop()
    return False


def dfs_weighted_adjacency_list(
    graph: WeightedAdjacencyList, source: int, target: int
) -> List[int]:
    path = []
    seen = [False for _ in range(len(graph))]
    walk(graph, source, target, path, seen)
    return path
