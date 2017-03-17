def product(s):
    punct = {"!": 0, "?": 0}
    for char in s:
        if char in punct:
            punct[char] += 1
    return punct["!"] * punct["?"]
