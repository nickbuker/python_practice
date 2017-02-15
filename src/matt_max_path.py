import numpy as np


def find_max_path(arr):
    windows = {}
    make_windows(arr, windows)
    return windows


def make_windows(arr, windows):
    # Find all windows for each column
    for col in range(len(arr)):
        if col != len(arr):
            col_list = [row[col] for row in arr]
            for i in range(len(col_list)):
                for j in range(i, len(arr)):
                    windows[((i, col), (j, col))] = np.sum(col_list[i:j+1])
        # Last column will have one element windows
        else:
            col_list = [row[len(arr) - 1] for row in arr]
            for i, n in enumerate(col_list):
                windows[((i, len(arr) - 1),(i, len(arr) - 1))] = col_list[i]


def test_paths(windows):
    max_path = -np.inf
    pass
