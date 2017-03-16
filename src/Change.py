class Change(object):

    def __init__(self):
        pass

    def make(self, n, *args):
        self.coins = sorted(args)
        self.found = set()
        return self._change(set([n]), 0)

    def _change(self, nums, count):
        count += 1
        layer = set()
        for n in nums:
            for c in self.coins:
                new = n - c
                if new == 0:
                    return count
                if new in self.found or new in nums:
                    continue
                else:
                    self.found.add(new)
                    layer.add(new)
        return self._change(layer, count)
