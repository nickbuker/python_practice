class FindWords:

    def __init__(self, s, vocab):
        self.s = s
        self.vocab = vocab

    def words(self):
        return self._words(self.s)

    def _words(self, s, prev=''):
        for i in range(1, 15):
            if s[:i] in self.vocab:
                tmp = [s[:i]]
                return tmp + self._words(s[i:], s[:i])
