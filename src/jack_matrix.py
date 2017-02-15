class Matrix(object):

    def __init__(self, arr):
        self.arr = arr
        self.shape = (len(arr), len(arr[0]))

    def __add__(self, other):
        if self.shape != other.shape:
            return "Matrices must have same shape."
        new_mat = []
        for i, row in enumerate(self.arr):
            tmp_row = []
            for j, n in enumerate(row):
                tmp_row.append(n + other.arr[i][j])
            new_mat.append(tmp_row)
        return Matrix(new_mat)

    def __mul__(self, other):
        if self.shape[1] != other.shape[0]:
            return "Matrix shapes not compatible with multiplicaton."
        new_mat = []
        for i, row in enumerate(self.arr):
            tmp_row = []
            for k in range(self.shape[0]):
                tmp_row.append(sum([self.arr[i][j] * other.arr[j][k]
                                    for j in range(self.shape[1])]))
            new_mat.append(tmp_row)
        return Matrix(new_mat)

    def trace(self):
        if self.shape[0] != self.shape[1]:
            return "Method requries a square matrix."
        total = 0
        for i in range(self.shape[0]):
            total += self.arr[i][i]
        return total
