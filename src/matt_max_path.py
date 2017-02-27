import numpy as np


def find_max_path(arr):
    shape = (len(arr), len(arr[0]))
    paths = make_paths_matrix(shape)
    for col in xrange(1, shape[1]):
        windows = make_windows(col, arr, shape)
        filtered_windows = filter_windows(col, windows, shape)
        paths = find_best_windows(col, filtered_windows, paths, shape)
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


def filter_windows(col, windows, shape):
    filtered_windows = {}
    for i in xrange(shape[0]):
        if (i, col) not in filtered_windows:
            filtered_windows[(i, col)] = []
        for k, v in windows.iteritems():
            if (i, col - 1) == k[0] or (i, col - 1) == k[1]:
                filtered_windows[(i, col)].append((k, v))
    return filtered_windows


def find_best_windows(col, filtered_windows, paths, shape):
    best_windows = {}
    for i in xrange(shape[0]):
        print i, col
        if (i, col) not in best_windows:
            best_windows[(i, col)] = (((-1,-1), (-1,-1)), -np.inf)
        for n in filtered_windows[(i, col)]:
            k0, k1, win_sum = n[0][0], n[0][1], n[1]
            path = max(paths[k0[0]][k0[1]], paths[k1[0]][k1[1]])
            total = win_sum + path
            if best_windows[(i, col)][1] < total:
                paths[i][col] = total
                best_windows[(i, col)] = ((k0, k1), total)
            print k0, k1, win_sum, total
    return paths
