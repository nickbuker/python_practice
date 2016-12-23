def func_or(a,b):
    if get_val(a, b) > 0:
        return True
    return False


def func_xor(a,b):
    if get_val(a, b) == 1:
        return True
    return False


def get_val(a, b):
    return check_let(a) + check_let(b)


def check_let(x):
    if type(x) == int and x != 0:
        return 1
    if x == True:
        return 1
    else:
        return 0
