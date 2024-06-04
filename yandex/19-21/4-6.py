def g(a, b, m):
    if a+b >= 59:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [
        g(a+1, b, m-1),
        g(a * 2, b, m - 1),
        g(a, b+1, m - 1),
        g(a, b*2, m - 1),
    ]
    return any(h) if (m-1)%2==0 else all(h)

a=5
for i in range(1,53):
    if not g(a, i, 2) and g(a, i, 4):
        print(i)