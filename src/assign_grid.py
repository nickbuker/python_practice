from __future__ import division
import numpy as np


def assign(data):
    empty_grid = make_grid(data)
    return assign_grid(empty_grid, data)


def make_grid(data):
    x1 = [x[0] for x in data]
    x2 = [x[1] for x in data]
    x1_min, x1_max = np.min(x1), np.max(x1)
    x2_min, x2_max = np.min(x1), np.max(x2)
    x1_it = (x1_max - x1_min) / 10
    x2_it = (x2_max - x2_min) / 10
    x1_its, x2_its = [], []
    for n in xrange(0,10):
        x1_its.append((x1_min + x1_it*n, x1_min + x1_it*(n+1)))
        x2_its.append((x2_min + x2_it*n, x2_min + x2_it*(n+1)))
    grid = {}
    for x1 in x1_its:
        for x2 in x2_its:
            grid[(x1,x2)] = []
    return grid


def assign_grid(grid, data):
    for point in data:
        for key in grid:
            if (point[0] >= key[0][0] and
                point[0] <= key[0][1] and
                point[1] >= key[1][0] and
                point[1] <= key[1][1]):
                grid[key].append(point)
    return grid
