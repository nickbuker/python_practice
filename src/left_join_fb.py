# create a python function to do a left join on two dicts (values = lists)


def left_join(left, right):
    joined = {}
    for key in left:
        joined[key] = left[key]
        if key in right:
            joined[key].extend(right[key])
    return joined
