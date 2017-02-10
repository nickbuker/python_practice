def pal_possible(s):
    s = pre_process(s)
    counts = counter(s)
    return check_counts(counts)


def pre_process(s):
    s_list = list(s.lower())
    return [c for c in s_list if c != " "]


def counter(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    return counts


def check_counts(counts):
    mods = 0
    for val in counts.itervalues():
        if val % 2 != 0:
            mods += 1
    return mods <= 1
