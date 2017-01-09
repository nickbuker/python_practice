def is_narcissistic(i):
    nums = map(int, list(str(i)))
    n = len(nums)
    if i == sum(map(lambda x : x ** n, nums)):
        return True
    return False
