def gap(g, m, n):
    p1, p2 = 0, 0
    for num in xrange(m, n + 1):
        prime = True
        for x in xrange(2, int(num ** 0.5) + 1):
            if num % x == 0:
                prime = False
                break
        if prime == True:
            p1 = p2
            p2 = num
        if p2 - p1 == g:
            return [p1, p2]
    return None
