def sub_sort(arr):
    lefts, rights = lefts_rights(arr)
    return start_stop(arr, lefts, rights)


def lefts_rights(arr):
    left, right = arr[0], arr[-1]
    lefts, rights = [], []
    # Create increasing list for comparison
    for n in arr:
        if n > left:
            left = n
        lefts.append(left)
    # Create decreasing list for comparison
    for m in arr[::-1]:
        if m < right:
            right = m
        rights.append(right)
    # Reverse lists for easier use in next function
    return lefts[::-1], rights[::-1]


def start_stop(arr, lefts, rights):
    # Find first difference between arr and rights
    for i, n in enumerate(arr):
        if n != rights[i]:
            start = i
            break
    # Find first difference between reversed arr and lefts
    for j, m in enumerate(arr[::-1]):
        if m != lefts[j]:
            stop = len(arr) - 1 - j
            break
    return (start, stop)
