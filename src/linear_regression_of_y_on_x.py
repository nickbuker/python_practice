def regressionLine(x, y):
    n = len(y)
    x_sum = sum(x)
    y_sum = sum(y)
    xy = zip(x, y)
    xy_sum = sum((n[0] * n[1] for n in xy))
    x2_sum = sum((n ** 2 for n in x))
    b = ((n * xy_sum) - (x_sum * y_sum)) / float(((n * x2_sum) - (x_sum ** 2)))
    a = ((x2_sum * y_sum) - (x_sum * xy_sum)) / float(((n * x2_sum) - (x_sum ** 2)))
    return round(a, 4), round(b, 4)
