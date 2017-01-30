def spiralize(size):
    spiral = make_array(size)
    return add_ones(spiral)


def make_array(size):
    array = []
    for r in xrange(size):
        row = []
        for c in xrange(size):
            row.append(0)
        array.append(row)
    return array


def add_ones(array):
    if len(array) == 1:
        return [[1]]
    if len(array) == 2:
        return [[1,1][0,1]]
    pass
    # finish me 
