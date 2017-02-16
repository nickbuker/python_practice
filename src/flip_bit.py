def flip_bit(value, bit_index):
    rev_bin = make_bin(value)
    rev_bin = flip(bit_index, rev_bin)
    return make_dec(rev_bin)


def make_bin(value):
    rev_bin = []
    while value > 0:
        rev_bin.append(value % 2)
        value /= 2
    return rev_bin


def flip(bit_index, rev_bin):
    if bit_index - 1 < len(rev_bin):
        rev_bin[bit_index - 1] = not rev_bin[bit_index - 1]
    else:
        rev_bin = [1] + rev_bin
    return rev_bin


def make_dec(rev_bin):
    dec = 0
    for i, n in enumerate(rev_bin):
        dec += n * (2 ** i)
    return dec
