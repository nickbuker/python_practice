import numpy as np


def find_max_path(arr):
    windows = {col: make_window(col, arr) for col in range(len(arr)-1)}
    #best_windows = {col: best_window(col, arr, windows) for col in range(1,len(arr))}
    best_windows = best_window(1, arr, windows)
    return windows, best_windows


def make_window(col, arr):
    window = {}
    col_list = [row[col] for row in arr]
    for i in range(len(col_list)):
        for j in range(i, len(col_list)):
            window[((i, col), (j, col))] = sum(col_list[i:j+1])
    return window


def best_window(col, arr, windows):
    best_windows = {}
    col_list = [row[col] for row in arr]
    for i in range(len(col_list)):
        best = (0, 0, -np.inf)
        for k, v in windows[col - 1].iteritems():
            if (k[0] == (i, col - 1) or k[1] == (i, col - 1)) and v > best[2]:
                best = (k[0], k[1], v)
            best_windows[(i, col)] = best
    return best_windows


def max_path(point, best_windows, path):
    if point[1] == 1:
        path += best_windows[1][point][1]
        return path


    start = max_path(best_windows[point[1]][point][0][0])
    stop = max_path(best_windows[point[1]][point][0][1])
