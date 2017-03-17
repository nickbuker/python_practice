def square_or_square_root(arr):
    squares = find_squares(arr)
    return [int(x ** 0.5) if x in squares else x ** 2 for x in arr]


def find_squares(arr):
    return [x ** 2 for x in xrange(1, int(max(arr) ** 0.5) + 1)]
