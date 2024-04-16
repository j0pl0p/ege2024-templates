# -1 -3 //3
# 22 > 2

def f(curr, end):
    if curr < end: return 0
    if curr == end: return 1
    if curr > end: return f(curr - 1, end) + f(curr - 3, end) + f(curr // 3, end)


print(f(22, 2))
