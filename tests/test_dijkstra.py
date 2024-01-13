from structures.graphs import WeightedAdjacencyList, WeightedEdge
from searches.dijkstra import shortest_path

GRAPH: WeightedAdjacencyList = [
    [
        WeightedEdge(1, 3),
        WeightedEdge(2, 1),
    ],
    [
        WeightedEdge(0, 3),
        WeightedEdge(2, 4),
        WeightedEdge(4, 1),
    ],
    [
        WeightedEdge(1, 4),
        WeightedEdge(3, 7),
        WeightedEdge(0, 1),
    ],
    [
        WeightedEdge(2, 7),
        WeightedEdge(4, 5),
        WeightedEdge(6, 1),
    ],
    [
        WeightedEdge(1, 1),
        WeightedEdge(3, 5),
        WeightedEdge(5, 2),
    ],
    [
        WeightedEdge(6, 1),
        WeightedEdge(4, 2),
        WeightedEdge(2, 18),
    ],
    [
        WeightedEdge(3, 1),
        WeightedEdge(6, 1),
    ],
]


def test_dijkstra():
    assert shortest_path(GRAPH, 0, 6) == [0, 1, 4, 5, 6]
