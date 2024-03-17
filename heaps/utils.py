def determine_child_indices(n: int) -> tuple[int, int]:
    return 2 * n + 1, 2 * n + 2


def determine_parent_index(n: int) -> int:
    return (n - 1) // 2
