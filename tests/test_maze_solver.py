from recursion.maze_solver import solve, Point


def test_maze_solver():
    START = Point(10, 0)
    END = Point(1, 5)
    MAZE = [
        "xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx",
    ]
    path = solve(MAZE, START, END)
    assert path == [
        Point(10, 0),
        Point(10, 1),
        Point(10, 2),
        Point(10, 3),
        Point(10, 4),
        Point(9, 4),
        Point(8, 4),
        Point(7, 4),
        Point(6, 4),
        Point(5, 4),
        Point(4, 4),
        Point(3, 4),
        Point(2, 4),
        Point(1, 4),
        Point(1, 5),
    ]
