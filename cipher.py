import string
from itertools import izip


class CaesarCipher(object):

    def __init__(self, shift):
        self.shift = shift
        lets = list(string.uppercase)
        nums = [x for x in xrange(1,27)]
        self.let_dict = dict(izip(lets, nums))
        self.num_dict = dict(izip(nums, lets))

    def encode(self, word):
        return self.process(word, self.shift, 1)

    def decode(self, code):
        return self.process(code, -self.shift, 0)

    def _process(self, item, slide, direction):
        item = list(item.upper())
        ind = [self.let_dict[x] if x in self.let_dict else x for x in item]
        shf = map(lambda x: x + slide if type(x) == int else x, ind)
        if direction == 1:
            adj = map(lambda x: x - 26 if type(x) == int and x > 26 else x, shf)
        if direction == 0:
            adj = map(lambda x: x + 26 if type(x) == int and x <= 0 else x, shf)
        return ''.join([self.num_dict[x] if x in self.num_dict else x for x in adj])
