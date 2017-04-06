def fact(n):
    if n < 0:
        return None
    if n <= 2:
        return n
    return n * fact(n - 1)
