# 1 heap, +1 *3, s >= 2163

def f(s, m):
    if s >= 2163:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [
        f(s+1, m-1),
        f(s*3, m-1)
    ]
    return any(h) if (m-1)%2==0 else all(h)


print('N19')
for i in range(2163):
    if all([
        not f(i, 1),
        f(i, 2)
    ]):
        print(i)

print('N20')
for i in range(2163):
    if all([
        not f(i, 1),
        f(i, 3)
    ]):
        print(i)


print('N21')
for i in range(2163):
    if all([
        not f(i, 2),
        f(i, 4)
    ]):
        print(i)