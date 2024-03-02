from itertools import product, permutations


def f(x, y, z, w):
    return (x or (not y)) and (not (y == z)) and w


for a in product([0, 1], repeat=4):  # repeat = кол-во пробелов в таблице

    table = [  # таблица из условия, где на месте пропусков находятся элементы массива a
        (0, 1, a[0], 0),
        (a[1], 1, 1, 0),
        (1, a[2], 0, a[3]),
    ]

    if len(table) == len(set(table)):  # все строки различны
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(p)  # при верном решении вывод будет единственным
