class RecursiveFib(object):

    def __init__(self):
        pass

    def get_fib(self, n):
        if n > 1:
            return self.get_fib(n - 1) + self.get_fib(n - 2)
        return n


if __name__ == '__main__':
    rf = RecursiveFib()
    print '\nrf created'
