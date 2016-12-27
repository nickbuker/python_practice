def super_size(n):
    return int(''.join(map(str, sorted(list(str(n)), reverse=True))))
