def to_base(n, base=10):
    ans = ''
    while n > 0:
        ans += str(n % base)
        n //= base
    return ans[::-1]


e = 2 * 27 ** 7 + 3 ** 10 - 9
print(to_base(e, 3).count('0'))
