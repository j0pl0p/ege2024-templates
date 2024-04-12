from itertools import *


def f(x, y, z):
    return any([
        (not x) and y and z,
        (not x) and (not y) and z,
        (not x) and (not y) and (not z),
    ])


for p in permutations('xyz'):
    table = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 0, 1]
    ]
    if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
        print(p)
