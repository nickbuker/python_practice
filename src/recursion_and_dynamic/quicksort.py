def quicksort(arr):
    left, equal, right = [], [], []
    if len(arr) > 1:
        pivot = arr[-1]
        for n in arr:
            if n < pivot:
                left.append(n)
            if n == pivot:
                equal.append(n)
            if n > pivot:
                right.append(n)
        return quicksort(left) + equal + quicksort(right)
    else:
        return arr
