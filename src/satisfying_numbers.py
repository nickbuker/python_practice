def smallest(n):
    if n <= 2:
        return n
    sat = (n * (n - 1)) - 1
    active = True
    while active:
        sat += 1
        for num in range(n // 2, n + 1):
            if sat % num != 0:
                break
            if num == n:
                active = False
    return sat
