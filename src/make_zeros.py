import numpy as np


def make_zeros(arr):
    m, n = len(arr), len(arr[0])
    zeros = find_zeros(arr)

    if len(zeros) == 0:
        return arr

    for zero in zeros:
        arr[zero[0]] = map(int, list(np.zeros(n)))
        for row in arr:
            row[zero[1]] = 0
    return arr


def find_zeros(arr):
    zeros = []
    for i, r in enumerate(arr):
        for j, c in enumerate(r):
            if c == 0:
                zeros.append((i,j))
    return zeros
