import numpy as np


def find_max_path(arr):
    windows = {col: make_window(col, arr) for col in range(len(arr)-1)}
    best_windows = {col: best_window(col, arr, windows) for col in range(1,len(arr))}
    return windows, best_windows


def make_window(col, arr):
    window = {}
    col_list = [row[col] for row in arr]
    for i in range(len(col_list)):
        for j in range(i, len(col_list)):
            window[((i, col), (j, col))] = sum(col_list[i:j+1])
    return window

    # Find all windows for each column
    # for col in range(len(arr)):
    #     if col != len(arr):
    #         col_list = [row[col] for row in arr]
    #         for i in range(len(col_list)):
    #             for j in range(i, len(arr)):
    #                 windows[((i, col), (j, col))] = np.sum(col_list[i:j+1])
    #     # Last column will have one element windows
    #     else:
    #         col_list = [row[len(arr) - 1] for row in arr]
    #         for i, n in enumerate(col_list):
    #             windows[((i, len(arr) - 1),(i, len(arr) - 1))] = col_list[i]

def best_window(col, arr, windows):
    best_window = {}
    col_list = [row[col] for row in arr]
    for i in range(len(col_list)):
        best = -np.inf
        for k, v in windows[col - 1].iteritems():
            if (k[0] == (i, col - 1) or k[1] == (i, col - 1)) and v > best:
                best = v
        best_window[(i,col)] = best
    return best_window


def test_paths(windows):
    max_path = -np.inf
    pass
