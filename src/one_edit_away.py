def one_edit_away(a, b):
    if a == b:
        return False
    if (len(a) - len(b)) ** 2 > 1:
        return False
    if len(a) == len(b):
        return same_len(a, b)
    if len(a) > len(b):
        return diff_len(a, b)
    else:
        return diff_len(b, a)


def same_len(a, b):
    diffs = 0
    for i, c in enumerate(a):
        if c != b[i]:
            diffs += 1
        if diffs > 1:
            return False
    return True


def diff_len(longer, shorter):
    diffs = 0
    for i, c in enumerate(shorter):
        if c != longer[i + diffs]:
            diffs += 1
        if diffs > 1:
            return False
    return True
