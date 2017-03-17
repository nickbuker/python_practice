def x(n):
    mat = construct_mat(n)
    return add_ones(mat)


def construct_mat(n):
    results = []
    for i in xrange(n):
        row = []
        for j in xrange(n):
            row.append(0)
        results.append(row)
    return results


def add_ones(mat):
    idx = 0
    for i, r in enumerate(mat):
        r[idx], r[-idx - 1] = 1, 1
        idx += 1
    return mat
