import numpy as np


class Change(object):

    def __init__(self):
        pass

    def make(self, n, *args):
        self.coins = sorted(args)
        return self._change(n, 0, -1)

    def _change(self, n, coin, count):
        if coin > n:
            return np.inf
        count += 1
        if coin == n:
            return count
        return min([self._change(n - coin, c, count) for c in self.coins
                    if c * self.coins[-1] > n or c == self.coins[-1]])
