def sum_dig_pow(a, b):
    results = []
    for num in xrange(a, b + 1):
        num_list = list(str(num))
        num_sum = 0
        for i, dig in enumerate(num_list):
            num_sum += int(dig) ** (i + 1)
        if num_sum == num:
            results.append(num)
    return results
