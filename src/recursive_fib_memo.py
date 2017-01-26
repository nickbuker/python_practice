def rec_memo_fib(n, _fibs={}):
    if n in _fibs:
        return _fibs[n]
    elif n > 1:
        return _fibs.setdefault(n, rec_memo_fib(n-1)+rec_memo_fib(n-2))
    return n
