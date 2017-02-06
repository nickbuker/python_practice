def fib(n):
    memo = {}
    return get_fib(n, memo)


def get_fib(n, memo):
    if n < 2:
        return n
    if n in memo:
        return memo[n]
    results = get_fib(n-1, memo) + get_fib(n-2, memo)
    if results not in memo:
        memo[n] = results
    return results
