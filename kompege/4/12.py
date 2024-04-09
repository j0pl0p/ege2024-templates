def from_base(s, base=2):
    ans = 0
    s = s[::-1]
    for i in range(len(s)):
        ans += int(s[i], base=base) * base ** i
    return ans


for i in range(8,10000):
    if from_base('103', i) == from_base('97', i+2):
        print(i)
        break
