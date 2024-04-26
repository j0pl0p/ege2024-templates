# 2 heaps, +1 *2, I=5, II=? (II<53), sum >=59

def f(a, b, m):
    if a+b >= 59:
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

a=5
print('N21')
for i in range(53):
    if not f(a, i, 2) and f(a, i, 4):
        print(i)