def dict_to_list(data):
    tups = []
    for k, v in data.items():
        tups.append(make_tups(k, v))
    dims = (len(tups), len(tups[0]))
    results = []
    for col in range(dims[1]):
        results.append(make_col(tups, dims, col))
    return results


def make_tups(k, v):
    tup_list = []
    for n in v:
        tup_list.append((k, n))
    return tup_list


def make_col(tups, dims, col):
    col_list = []
    for row in range(dims[0]):
        col_list.append(tups[row][col])
    return dict(col_list)
