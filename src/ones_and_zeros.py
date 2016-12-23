def binary_array_to_number(arr):
    rev_arr = reversed(arr)
    base = 1
    num = 0
    for n in rev_arr:
        num += base * n
        base *= 2
    return num
