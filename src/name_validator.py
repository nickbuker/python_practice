from string import uppercase, lowercase

def show_me(name):
    name_split = name.split('-')
    for n in name_split:
        if len(n) <= 1:
            return False
        for i, c in enumerate(n):
            if i == 0 and c not in uppercase:
                return False
            if i > 0 and c not in lowercase:
                return False
    return True
