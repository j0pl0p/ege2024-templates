def from_base(s, base=2):
    ans = 0
    s = s[::-1]
    for i in range(len(s)):
        ans += int(s[i], base=base) * base ** i
    return ans


for i in range(10000):
    if from_base('33', i + 4) - 15 == 33:
        print(i)
        break
