def paren_checker(s):
    lp, lb, lc, rp, rb, rc = 0, 0, 0, 0, 0, 0
    s_list = list(s)
    for char in s_list:
        if char == "(":
            lp += 1
        if char == "[":
            lb += 1
        if char == "{":
            lc += 1
        if char == ")":
            rp += 1
        if char == "]":
            rb += 1
        if char == "}":
            rc += 1
        if lp < rp or lb < rb or lc < rc:
            return False
    if lp != rp or lb != rb or lc != rc:
        return False
    else:
        return True
