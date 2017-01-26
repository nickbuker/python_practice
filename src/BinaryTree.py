class BinaryTree(object):

    def __init__(self, n=None):
        self.value = n
        self.left = None
        self.right = None

    def insert(self, n):
        if self.value is None:
            self.value = n
        if n <= self.value:
            if self.left is None:
                self.left = BinaryTree()
            else:
                self.left.insert(n)
        if n > self.value:
            if self.right is None:
                self.right = BinaryTree()
            else:
                self.right.insert(n)

    def find(self, n):
        if self.value == n:
            return True
        if n < self.value:
            if self.left is None:
                return False
            return self.left.find(n)
        if n > self.value:
            if self.right is None:
                return False
            return self.right.find(n)
