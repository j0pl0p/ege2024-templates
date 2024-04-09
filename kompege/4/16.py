def to_base(n, base=10):
    ans = ''
    while n > 0:
        ans += str(n % base)
        n //= base
    return ans[::-1]


for i in range(41):
    if to_base(i, 2)[-4:] == '1011':
        print(i)
