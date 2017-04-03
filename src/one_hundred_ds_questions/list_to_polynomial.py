"""
Given a list of numbers representing the coefficients in a polynomial
(largest powers first), write a function that returns a pretty string
representation of the polynomial.

[1, 1, 1] => "x^2 + x + 1"
[2, -1, -2] => "2x^2 - x -2"
[0, 9, -10] => "9x - 10"
"""


def poly(nums):
    if len(nums) == 1:
        return str(nums[0])
    expon = 0
    results = []
    revs = nums[::-1]
    joins = find_joins(nums)
    for i, num in enumerate(revs):
        if num == 0:
            expon += 1
            continue
        # First coeff in polynomial should retain negative sign
        if i != len(revs) - 1:
            num = abs(num)
        if expon == 0:
            results.append(str(num))
        elif expon == 1:
            results.append(str(num) + 'x')
        else:
            results.append(str(num) + 'x^' + str(expon))
        expon += 1
    return ''.join(string_constructor(results[::-1], joins))


def find_joins(nums):
    joins = []
    for num in nums[1:]:
        if num > 0:
            joins.append(' + ')
        elif num < 0:
            joins.append(' - ')
    return joins


def string_constructor(results, joins):
    string_list = []
    for i, string in enumerate(results):
        if i > 0:
            string_list.append(joins[i - 1])
        string_list.append(string)
    return string_list
