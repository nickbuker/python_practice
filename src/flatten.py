from itertools import chain


def flatten_me(lst):
    return list(chain.from_iterable(lst))
