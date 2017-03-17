import numpy as np


def knn(k, train, data):
    distances = dist(train, data)
    return assign(k, distances)


def dist(train, data):
    distances = []
    for n in data:
        tmp_dist = []
        for m in train:
            d = ((n[0] - m[1]) ** 2 + (n[1] - m[2]) ** 2) ** 0.5
            tmp_dist.append((d, m[0]))
        distances.append(tmp_dist)
    return distances


def assign(k, distances):
    assignments = []
    for distance in distances:
        tmp_assign = []
        distance.sort()
        for assign in distance[:k]:
            tmp_assign.append(assign[1])
        assignments.append(round(np.mean(tmp_assign[:k])))
    return assignments
