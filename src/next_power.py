from __future__ import division


def find_next_power(val, power):
    return ((int(val ** (1 / power)) + 1) ** power)
