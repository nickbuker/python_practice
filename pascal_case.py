def to_underscore(string):
    string = str(string)
    indexes = [i for i, char in enumerate(string) if char.isupper() and i != 0]
    for i in reversed(indexes):
        string = string[:i] + "_" + string[i:]
    return string.lower()
