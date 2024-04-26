# 1 heap, +1 +2 +3 *2, s >= 34

def f(s, m):
    if s >= 34: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s + 1, m - 1),
        f(s + 2, m - 1),
        f(s + 3, m - 1),
        f(s * 2, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print('\n19')
# 19
for i in range(33):
    print(i, f(i, 2))

print('\n20')
# 20
for i in range(33):
    print(f'{i}')
    if all([
        f(i, 1) == False,
        f(i, 3) == True
    ]):
        print('TRUE')
    else:
        print('false')

print('\n21')
for i in range(33):
    print(i)
    if all([
        f(i, 4),
        not f(i, 2)
    ]):
        print('TRUE')
