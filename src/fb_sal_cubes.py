"""
There is a cube with dimensions n * n * n that is made of smaller
unit cubes. If we paint the outside of larger cube, how many of the
unit cubes will not be painted?
"""


def cubes(n):
    if n <= 2:
        return 0
    side_area = n ** 2
    # subtract corner and edge unit cubes from side
    adj_area = side_area - 4 - (4 * (n - 2))
    inner_edge = int(adj_area ** 0.5)
    return inner_edge ** 3


def simple_cubes(n):
    if n <= 2:
        return 0
    return (n - 2) ** 3
