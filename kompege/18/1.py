# +1, +3, *2
# 1 > 15

def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    if curr < end:
        return f(curr + 1, 15) + f(curr + 3, 15) + f(curr * 2, 15)


print(f(1, 15))
