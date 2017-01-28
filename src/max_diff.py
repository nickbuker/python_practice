def max_diff(nums):
    if len(nums) <= 1:
        return 0
    min_n, max_n = float('inf'), -float('inf')
    for n in nums:
        if n < min_n:
            min_n = n
        if n > max_n:
            max_n = n
    return abs(min_n - max_n)
