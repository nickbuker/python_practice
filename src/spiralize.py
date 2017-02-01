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
    for n in array[0]:
        n = 1
    for n in array[-1]:
        n = 1
    i = 1
    starts = []
    stops = [-1]
    while i < len(array) - 1:
        if i < len(array) - 1:
            for start in starts:
                array[i][start] = 1
            if len(starts) == 0:
                starts.append(0)
            else:
                starts.append(starts[-1] + 2)
            for stop in stops:
                array[i][stop] = 1
            stops.append(stops[-1] - 2)
        i += 1
        if i < len(array) - 1:
            for start in starts:
                array[-i][start] = 1
            if len(starts) == 0:
                starts.append(0)
            else:
                starts.append(starts[-1] + 2)
            for stop in stops:
                array[-i][stop] = 1
            stops.append(stops[-1] - 2)
        i += 1
        
