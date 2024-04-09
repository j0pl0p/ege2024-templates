def to_base(n, base=10):
    ans = ''
    while n > 0:
        ans += str(n % base)
        n //= base
    return ans[::-1]


e = 51 * 7 ** 12 - 7 ** 3 - 22
print(sum(map(int, to_base(e, 7))))
