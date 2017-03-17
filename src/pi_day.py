from __future__ import division
from fractions import gcd
import numpy as np


class FindPy(object):

    def __init__(self):
        pass

    def pi(self, n=500):
        self.coprimes = 0
        num_arr = zip(np.random.randint(1, 1000, n),
                      np.random.randint(1, 1000, n))
        map(self._coprime, num_arr)
        return (6 / (self.coprimes / n)) ** 0.5

    def _coprime(self, nums):
        if gcd(nums[0], nums[1]) == 1:
            self.coprimes += 1
