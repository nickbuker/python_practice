def string_suffix(s):
    sim = 0
    for i in xrange(len(s)):
        suffix = s[i:]
        for j in xrange(len(suffix)):
            if suffix[j] == s[j]:
                sim += 1
            else:
                break
    return sim
