import numpy as np


def find_max_path(arr):
    shape = (len(arr), len(arr[0]))
    paths = make_paths_matrix(shape)
    for col in xrange(1, shape[1]):
        windows = make_windows(col, arr, shape)
        paths = find_best_windows(col, arr, shape, windows, paths)
        print paths
        if col == shape[1] - 1:
            col_list_arr = [row[col] for row in arr]
            col_list_paths = [row[col] for row in paths]
            return max([sum(x) for x in zip(col_list_arr, col_list_paths)])


def make_paths_matrix(shape):
    paths = []
    for i in range(shape[0]):
        tmp_row = shape[1] * [0]
        paths.append(tmp_row)
    return paths


def make_windows(col, arr, shape):
    windows = {}
    col_list = [row[col - 1] for row in arr]
    for i in xrange(shape[1]):
        for j in xrange(i, shape[1]):
            windows[((i, col - 1), (j, col - 1))] = sum(col_list[i: j + 1])
    return windows


def find_best_windows(col, arr, shape, windows, paths):
    best_windows = {}
    for i in xrange(shape[0]):
        best_windows[(i, col)] = (0, -np.inf)
        for k, v in windows.iteritems():
            if k[0] == (i, col - 1) or k[1] == (i, col - 1):
                if best_windows[(i,col)][1] < v + max(paths[k[0][0]][k[0][1]],
                                                      paths[k[1][0]][k[1][1]]):
                    paths[i][col] = v + max(paths[k[0][0]][k[0][1]],
                                            paths[k[1][0]][k[1][1]])
                    best_windows[(i, col)] = (k, v)
    return paths
