def validate(m):
    ml = m.split()
    if len(ml) != 8:
        return False
    if ml[0] != 'MDZHB':
        return False
    for i in [1, 2, 4, 5, 6, 7]:
        try:
            int(ml[i])
        except ValueError:
            return False
    lets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in ml[3]:
        if c not in lets:
            return False
    if len(ml[1]) != 2:
        return False
    if len(ml[2]) != 3:
        return False
    for i in xrange(4, 8):
        if len(ml[i]) != 2:
            return False
    return True
