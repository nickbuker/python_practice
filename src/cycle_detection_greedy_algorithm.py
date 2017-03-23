def cycle(s):
    d = {}
    for i, n in enumerate(s):
        if n in d:
            return [d[n], i - d[n]]
        else:
            d[n] = i
    return []
