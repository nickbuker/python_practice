def max_path(data):
    """
    Input: list of lists of positive numbers shaped like a pyramid
    Output: sum for max path through pyramid
    """
    zero_memo = make_memo(data)
    memo = paths(data, zero_memo)
    return find_best(data, memo)


def make_memo(data):
    """
    Input: list of lists of positive numbers shaped like a pyramid
    Output: list of lists of zeros with same shape as data
    """
    zero_memo = []
    for row in data:
        temp_row = []
        for n in row:
            temp_row.append(0)
        zero_memo.append(temp_row)
    return zero_memo


def paths(data, memo):
    """
    Input: list of lists of postive numbers and of zeros shaped like a pyramid
    Output: list of lists containing max path to each element
    """
    for i, row in enumerate(data):
        if i == 0:
            continue
        for j, n in enumerate(row):
            temp_vals = []
            if j - 1 >= 0:
                temp_vals.append(data[i - 1][j - 1] + memo[i - 1][j - 1])
            if j <= len(row) - 2:
                temp_vals.append(data[i - 1][j] + memo[i - 1][j])
            memo[i][j] = max(temp_vals)
    return memo


def find_best(data, memo):
    """
    Input: list of lists of positive numbers and max paths shaped like a pyramid
    Output: value for best path
    """
    best_list = []
    for j, n in enumerate(data[-1]):
        best_list.append(n + memo[-1][j])
    return max(best_list)
