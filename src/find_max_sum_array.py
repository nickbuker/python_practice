import numpy as np


def find_max(arr):
    '''
    Input: list of lists containing integers
    Output: max 3 element sum from list of lists
    Calls make_segs() to find valid indices and calls get_max_sum() to
    find max 3 element sum
    '''
    rows, cols, diags = make_segs(arr)
    return get_max_sum(rows, cols, diags, arr)


def make_segs(arr):
    '''
    Input: list of lists containing integers
    Output: valid indices for row, col and diag sums
    Validates indices for get_max_sum() to avoid IndexErrors
    '''
    rows, cols, diags = [], [], []
    for i, row in enumerate(arr):
        for j in range(0, len(arr)):
            if j + 2 < len(row):
                rows.append((i, j))
            if i + 2 < len(arr):
                cols.append((i, j))
            if j + 2 < len(row) and i + 2 < len(arr):
                diags.append((i, j))
    return rows, cols, diags


def get_max_sum(rows, cols, diags, arr):
    '''
    Input: lists of valid row, col, diag indices from make_segs()
    and list of lists containing integers
    Output: largest 3 element sum from list of lists
    Checks every valid horizontal, vertical, and diagonal 3 element sum
    and returns max_sum
    '''
    max_sum = -np.inf
    for n in rows:
        row_sum = (
            arr[n[0]][n[1]] +
            arr[n[0]][n[1] + 1] +
            arr[n[0]][n[1] + 2]
        )
        if max_sum < row_sum:
            max_sum = row_sum
    for n in cols:
        col_sum = (
            arr[n[0]][n[1]] +
            arr[n[0] + 1][n[1]] +
            arr[n[0] + 2][n[1]]
        )
        if max_sum < col_sum:
            max_sum = col_sum
    for n in diags:
        diag_sum = (
            arr[n[0]][n[1]] +
            arr[n[0] + 1][n[1] + 1] +
            arr[n[0] + 2][n[1] + 2]
        )
        if max_sum < diag_sum:
            max_sum = diag_sum
    return max_sum
