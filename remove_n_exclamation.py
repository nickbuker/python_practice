def remove(s, n):
    new_s = ""
    for char in s:
        if char == "!" and n > 0:
            n -= 1
        else:
            new_s += char
    return new_s
