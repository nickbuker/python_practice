def merge_sort(arr):
    if len(arr) > 1:
        split = len(arr) // 2
        left, right = arr[:split], arr[split:]
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        sorted_arr = []
        i, j = 0, 0
        while i < len(sorted_left) and j < len(sorted_right):
            if sorted_left[i] < sorted_right[j]:
                sorted_arr.append(sorted_left[i])
                i += 1
            else:
                sorted_arr.append(sorted_right[j])
                j += 1
        if i < len(sorted_left):
            sorted_arr += sorted_left[i:]
        if j < len(sorted_right):
            sorted_arr += sorted_right[j:]
        return sorted_arr
    return arr
