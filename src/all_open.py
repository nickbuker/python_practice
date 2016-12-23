def is_balanced(phrase, punct):
    items = []
    p_dict = {punct[i]: punct[i+1] for i in xrange(0, len(punct) -1, 2)}
    for char in phrase:
        if char in items:
            items.pop()
            continue
        if char in p_dict:
            items.append(p_dict[char])
            continue
        if char in p_dict.values() and char not in items:
            return False
    if len(items) == 0:
        return True
    else:
        return False
