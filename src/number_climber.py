"""
For every positive integer N, there exists a unique sequence starting with 1 and ending with N and such 
that every number in the sequence is either the double of the preceeding number or the double plus 1.

http://www.codewars.com/kata/number-climber/train/python
"""


def climb(n):
    results = []
    while n > 0:
        results.append(n)
        n = n // 2
    return results[::-1]


def rec_climb(n, nums=[1]):
    if nums[-1] < n:
        result1 = rec_climb(n, nums + [nums[-1] * 2])
        result2 = rec_climb(n, nums + [(nums[-1] * 2) + 1])
        if result1 is None:
            return result2
        else:
            return result1

    if nums[-1] == n:
        return nums
