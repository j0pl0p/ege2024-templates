def to_base(n, base=10):
    ans = ''
    while n > 0:
        ans += str(n % base)
        n //= base
    return ans[::-1]


e = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
b = to_base(e, 6)
print(b.count('5') - b.count('0'))
