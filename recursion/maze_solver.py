from typing import List
from collections import namedtuple

Point = namedtuple("Point", "x,y")

DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def walk_maze(
    maze: List[str],
    current: Point,
    end: Point,
    seen: List[Point],
    path: List[Point],
) -> bool:
    if (
        (not 0 <= current.x < len(maze[0]) or not 0 <= current.y < len(maze))
        or maze[current.y][current.x] == "x"
        or current in seen
    ):
        return False
    if current == end:
        path.append(end)
        return True
    path.append(current)
    seen.append(current)
    for direction in DIRECTIONS:
        x, y = direction
        next_point = Point(current.x + x, current.y + y)
        if walk_maze(maze, next_point, end, seen, path):
            return True
    path.pop()
    return False


def solve(maze: List[str], start: Point, end: Point) -> List[Point]:
    path = []
    walk_maze(maze, start, end, [], path)
    return path
