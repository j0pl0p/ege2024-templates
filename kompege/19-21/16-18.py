def f(a, b, m):
    if a * b >= 63:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [
        f(a + 1, b, m - 1),
        f(a * 2, b, m - 1),
        f(a, b + 1, m - 1),
        f(a, b * 2, m - 1),
    ]
    return any(h) if (m-1)%2==0 else all(h)

a = 2
for i in range(32):
    if all([
        not f(a, i, 2),
        f(a, i, 4)
    ]):
        print(i)
