def f(a, b, m):
    if a + b <= 20:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [
        f(a - 1, b, m - 1),
        f(a // 2 + (a % 2 == 1), b, m - 1),
        f(a, b - 1, m - 1),
        f(a, b // 2 + (b % 2 == 1), m - 1),
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


a = 10
for i in range(11, 100):
    if not f(a, i, 2) and f(a, i, 4):
        print(i)
