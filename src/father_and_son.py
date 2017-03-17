def sc(s):
    uppers = [c for c in s if c == c.upper()]
    lowers = [c for c in s if c == c.lower()]
    return "".join([c for c in s if c.upper() in uppers
                    and c.lower() in lowers])
