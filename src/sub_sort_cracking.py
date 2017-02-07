def sub_sort(arr):
    diffs = get_diffs(arr)
    return check_sort(diffs, arr)


def get_diffs(arr):
    diffs = []
    for i in xrange(1, len(arr)):
        diffs.append(arr[i] - arr[0])
    return diffs


def check_sort(diffs, arr):
    start, stop = 0, 0
    sort_diffs = sorted(diffs)
    for i, n in enumerate(diffs):
        if n != sort_diffs[i]:
            start = i + 1
            break
    rev_diffs = diffs[::-1]
    rev_sort_diffs = sort_diffs[::-1]
    for j, m in enumerate(rev_diffs):
        if m != rev_sort_diffs[j]:
            stop = len(diffs) - j
            break
    return (start, stop)
