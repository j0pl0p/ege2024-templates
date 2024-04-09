def to_base(n, base=10):
    ans = ''
    while n > 0:
        ans += str(n % base)
        n //= base
    return ans[::-1]


for i in range(10000):
    e = 36 ** 17 - 6 ** i + 71
    if sum(map(int, to_base(e, 6))) == 61:
        print(i)
        break
