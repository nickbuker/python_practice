def count_cows(n):
    if type(n) != int:
        return None
    cow_num = 1
    cows = {0: 0}
    cows_temp = {}
    for i in xrange(n):
        for cow in cows:
            cows[cow] += 1
        for age in cows.values():
            if age >= 3:
                cows_temp[cow_num] = 0
                cow_num += 1
        cows.update(cows_temp)
        cows_temp = {}
    return len(cows)
