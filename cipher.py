class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        lets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z']
        nums = [x for x in xrange(1,27)]
        self.let_dict = dict(zip(lets, nums))
        self.num_dict = dict(zip(nums, lets))

    def encode(self, word):
        self.word = list(word.upper())
        ind = [self.let_dict[x] if x in self.let_dict else x for x in self.word]
        shf = map(lambda x: x + self.shift if type(x) == int else x, ind)
        adj = map(lambda x: x - 26 if type(x) == int and x > 26 else x, shf)
        return ''.join([self.num_dict[x] if x in self.num_dict else x for x in adj])

    def decode(self, word):
        self.word = list(word)
        ind = [self.let_dict[x] if x in self.let_dict else x for x in self.word]
        shf = map(lambda x: x - self.shift if type(x) == int else x, ind)
        adj = map(lambda x: x + 26 if type(x) == int and x <= 0 else x, shf)
        return ''.join([self.num_dict[x] if x in self.num_dict else x for x in adj])
