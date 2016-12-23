def remove(s):
    if len(s) == 0:
        return s
    if s[-1] == "!":
        s = s[:-1]
    return s
