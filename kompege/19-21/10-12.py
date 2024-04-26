# 2 heaps, +1 *2, I=7, II=? (II<70), sum >=77

def f(a, b, m):
    if a+b >= 77:
        return m%2==0
    if m == 0:
        return 0
    h = [
        f(a+1, b, m-1),
        f(a*2, b, m-1),
        f(a, b+1, m-1),
        f(a, b*2, m-1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

a=7
print('N21')
for i in range(70):
    if not f(a, i, 1) and f(a, i, 3):
        print(i)