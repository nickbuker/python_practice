def multiple_split(s, delim=[]):
    for d in delim:
        s = s.replace(d, '`')
    return [x for x in s.split('`') if x != '']
