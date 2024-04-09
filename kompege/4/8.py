def to_base(n, base=10):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    ans = ''
    while n > 0:
        ans += alphabet[n % base]
        n //= base
    return ans[::-1]


e = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
print(to_base(e, 12).count('b'))

