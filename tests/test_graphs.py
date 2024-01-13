from structures.graphs import (
    bfs_weighted_adjacency_matrix,
    WeightedAdjacencyMatrix,
    WeightedEdge,
    WeightedAdjacencyList,
    dfs_weighted_adjacency_list,
)


MATRIX: WeightedAdjacencyMatrix = [
    [0, 3, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 5, 0, 2, 0],
    [0, 0, 18, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0],
]
#     >(1)<--->(4) ---->(5)
#    /          |       /|
# (0)     ------|------- |
#    \   v      v        v
#     >(2) --> (3) <----(6)


def test_bfs_weighted_adjacency_matrix():
    assert bfs_weighted_adjacency_matrix(MATRIX, 0, 6) == [
        0,
        1,
        4,
        5,
        6,
    ]


#     >(1)<--->(4) ---->(5)
#    /          |       /|
# (0)     ------|------- |
#    \   v      v        v
#     >(2) --> (3) <----(6)

ADJACENCY_LIST: WeightedAdjacencyList = [
    [
        WeightedEdge(1, 3),
        WeightedEdge(2, 1),
    ],
    [
        WeightedEdge(4, 1),
    ],
    [
        WeightedEdge(3, 7),
    ],
    [],
    [WeightedEdge(1, 1), WeightedEdge(3, 5), WeightedEdge(5, 2)],
    [WeightedEdge(2, 18), WeightedEdge(6, 1)],
    [WeightedEdge(3, 1)],
]


def test_dfs_weighted_adjacency_list():
    assert dfs_weighted_adjacency_list(ADJACENCY_LIST, 0, 6) == [
        0,
        1,
        4,
        5,
        6,
    ]
