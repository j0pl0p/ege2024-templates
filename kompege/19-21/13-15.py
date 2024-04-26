def f(a, b, m):
    if a+b >= 68:
        return m%2 == 0
    if m == 0:
        return 0
    h = [
        f(a + 1, b, m - 1),
        f(a + b, b, m - 1),
        f(a, b+1, m - 1),
        f(a, b+a, m - 1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

a = 8
for i in range(60):
    if not f(a, i, 2) and f(a, i, 4):
        print(i)