def approx_root(n):
    base = 0
    for i in xrange(1, n):
        if i ** 2 <= n:
            base = i
        if i ** 2 > n:
            break
    diff_gn = n - (base ** 2)
    diff_lg = ((base + 1) ** 2) - (base ** 2)
    return round(base + (diff_gn / float(diff_lg)), 2)
