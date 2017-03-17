def paren_checker(s):
    p = {"(": 0, "[": 0, "{": 0, ")": 0, "]": 0, "}": 0}
    s_list = list(s)
    for char in s_list:
        if char in p:
            p[char] += 1
            if p["("] < p[")"] or p["["] < p["]"] or p["{"] < p["}"]:
                return False
    if p["("] != p[")"] or p["["] != p["]"] or p["{"] != p["}"]:
        return False
    else:
        return True
