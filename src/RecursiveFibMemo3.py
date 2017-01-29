class Fib(object):

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n in self.memo:
            return self.memo[n]
        if n < 2:
            return n
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]
