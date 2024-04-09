def to_base(n, base=10):
    alphabet = '0123456789abcdef'
    ans = ''
    while n > 0:
        ans += alphabet[n % base]
        n //= base
    return ans[::-1]


e = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
print(len(set(to_base(e, 15))))

