def find_missing(a,b):
    d_a = counter(a)
    d_b = counter(b)
    missing = []
    for k, v in d_a.iteritems():
        if k not in d_b:
            for n in xrange(0,v):
                missing.append(k)
        elif v != d_b[k]:
            for n in xrange(d_b[k],v):
                missing.append(k)
    return missing


def counter(arr):
    d = {}
    for n in arr:
        if n in d:
            d[n] += 1
        if n not in d:
            d[n] = 1
    return d
