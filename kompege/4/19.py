def to_base(n, base=10):
    ans = ''
    while n > 0:
        ans += str(n % base)
        n //= base
    return ans[::-1]


count = 0
for i in range(10000):
    if all([
        len(to_base(i, 5)) <= 4,
        len(to_base(i, 2)) >= 5,
        str(hex(i))[-1] == 'c'
    ]):
        count += 1
print(count)
