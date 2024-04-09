def to_base(n, base=10):
    ans = ''
    while n > 0:
        ans += str(n % base)
        n //= base
    return ans[::-1]


for i in range(10000):
    e = 125 ** 200 - 5 ** i + 74
    if to_base(e, 5).count('4') == 100:
        print(i)
        break
