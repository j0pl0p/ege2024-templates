def to_base(n, base=10):
    ans = ''
    while n > 0:
        ans += str(n % base)
        n //= base
    return ans[::-1]


for i in range(21, 30):
    if to_base(i, 3)[-2:] == '11':
        print(i)
