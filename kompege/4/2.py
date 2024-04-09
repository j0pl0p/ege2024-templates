def to_base(n, base=10):
    ans = ''
    while n > 0:
        ans += str(n % base)
        n //= base
    return ans[::-1]


e = 3 * 16 ** 8 - 4 ** 5 + 3
print(to_base(e, 4).count('3'))
