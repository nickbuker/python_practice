class RecursiveFibMemo(object):

    def __init__(self):
        self.d = {}

    def get_fib(self, n):
        if n in self.d:
            return self.d[n]
        elif n > 1:
            return self.d.setdefault(n, (self.get_fib(n - 1) +
                                         self.get_fib(n - 2)))
        return n


if __name__ == '__main__':
    rfm = RecursiveFibMemo()
    print '\nrfm created'
