def natural_sum(n: int) -> int:
    if n <= 0:
        raise ValueError

    # Base Case
    if n == 1:
        return 1

    # Pre / Recurse Case
    value = n + natural_sum(n - 1)
    # Post
    print(n)
    return value
