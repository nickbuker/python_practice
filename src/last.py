def last(*args):
    if len(args) == 1:
        return args[0][-1]
    else:
        return args[-1]
