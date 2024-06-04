def game(s, m):
    if s > 33:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [
        game(s+1, m-1),
        game(s+2, m-1),
        game(s+3, m-1),
        game(s*2, m-1)
    ]
    return any(h) if (m-1)%2==0 else all(h)

for i in range(33):
    if all([
        not game(i, 2),
        game(i, 4)
    ]):
        print(i)