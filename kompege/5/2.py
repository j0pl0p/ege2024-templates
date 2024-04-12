from itertools import *


def f(a, b, c):
    return (a and (not c)) or ((not b) and (not c))


for p in permutations('abc'):
    table = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1],
    ]

    if [f(**dict(zip(p, row))) for row in table] == [1, 0, 0, 0, 1, 0, 1, 0]:
        print(p)
