# +1 +2 *4
# 1 > 13

def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    if curr < end: return f(curr + 1, end) + f(curr + 2, end) + f(curr * 4, end)


print(f(1, 13))
