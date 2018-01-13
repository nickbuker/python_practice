"""
The depth of an integer n is defined to be how many multiples of 
n it is necessary to compute before all 10 digits have appeared 
at least once in some multiple.

https://www.codewars.com/kata/integer-depth/python
"""


def compute_depth(n):
    bools = 10 * [False]
    depth = 1
    while True:
        digits = map(int, list(str(n * depth)))
        for m in digits:
            bools[m] = True
        if all(bools): 
            return depth
        depth += 1
