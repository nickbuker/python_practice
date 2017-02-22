import numpy as np


def find_max_path(arr):
    shape = (len(arr), len(arr[0]))
    paths = make_paths_matrix(shape)


def make_paths_matrix(shape):
    paths = []
    for i in range(shape[0]):
        tmp_row = shape[1] * [0]
        paths.append(tmp_row)
    return paths


def make_windows(col, arr, shape):
    windows = {}
    col_list = [row[col] for row in arr]
    for i in xrange(shape[1]):
        for j in xrange(i, shape[1]):
            windows[((i, col), (j, col))] = sum(col_list[i: j + 1])
    return windows


def find_best_windows(col, shape, arr, windows, paths):
    best_windows = {}
    for i in xrange(shape[0]):
        best_windows[(i, col)] = -np.inf
        for k, v in windows.iteritems():
            if (
                (
                 k[0] == (i, col - 1) or
                 k[1] == (i, col - 1)
                ) and
                best_windows[(i,col)] < v + max(paths[k[0][0]][k[0][1]],
                                                paths[k[1][0]][k[1][1]])
               ):
               best_windows[(i, col)] = {k: v}
               paths[i][col] = v + max(paths[k[0][0]][k[0][1]],
                                       paths[k[1][0]][k[1][1]])
    return best_windows, paths


def path_to_element(element):
    pass
