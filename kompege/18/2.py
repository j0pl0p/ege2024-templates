# +1 *2 ^2
# 5 > 154

def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    if curr < end: return f(curr + 1, end) + f(curr * 2, end) + f(curr ** 2, end)


print(f(5, 154))
