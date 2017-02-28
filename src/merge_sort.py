from collections import deque

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr
        else:
            return arr[::-1]
    split = (len(arr) / 2) + 1
    left = deque(merge_sort(arr[:split]))
    right = deque(merge_sort(arr[split:]))
    if left == arr[:split] and right == arr[split:]:
        pass

def merge(left, right):
    sorted_arr = []
    while len(left) > 0 or len(right) > 0:
        if len(right) == 0 and len(left) > 0:
            sorted_arr.append(left.popleft())
        if len(left) == 0 and len(right) > 0:
            sorted_arr.append(right.popleft())
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                sorted_arr.append(left.popleft())
            elif left[0] > right[0]:
                sorted_arr.append(right.popleft())
    return sorted_arr
