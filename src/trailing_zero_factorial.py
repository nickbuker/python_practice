from math import log

def count_trailing_zeros(num):
    zeros = 0
    for n in xrange(0, num + 1, 5):
        if n == 0:
            continue
        for m in xrange(1, int(log(n, 5) + 1)):
            if n % (5 ** m) == 0:
                zeros += 1
    return zeros
