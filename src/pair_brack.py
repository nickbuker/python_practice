def bracket_pairs(string):
    lefts = []
    pairs = {}
    for i, char in enumerate(string):
        if char == "(":
            lefts.append(i)
        if char == ")":
            if len(lefts) == 0:
                return False
            pairs[lefts.pop()] = i
    if len(lefts) > 0:
        return False
    return pairs
