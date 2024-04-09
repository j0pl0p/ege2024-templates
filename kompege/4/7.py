def to_base(n, base=10):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    ans = ''
    while n > 0:
        ans += alphabet[n % base]
        n //= base
    return ans[::-1]


e = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 **5 - 2 * 25 ** 4 - 2024
print(to_base(e, 25).count('0'))

