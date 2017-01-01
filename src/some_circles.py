from math import pi

def sum_circles(*args):
    return 'We have this much circle: {}'.format(int(round(sum([(pi * 0.25 * (x ** 2)) for x in args]),0)))
