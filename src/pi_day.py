from __future__ import division
from fractions import gcd
import numpy as np

class FindPy(object):

    def __init__(self):
        pass

    def pi(self, n=500):
        coprimes = 0
        for i in xrange(n):
            nums = np.random.randint(1, 1000, 2)
            if self.coprime(nums):
                coprimes += 1
        return (6 / (coprimes / n)) ** 0.5

    def coprime(self, nums):
        return gcd(nums[0], nums[1]) == 1
