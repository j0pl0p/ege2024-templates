# +1 *2
# 1 > 20 (10)

def f(curr, end):
    if curr > end:
        return 0
    if curr == end:
        return 1
    return f(curr + 1, end) + f(curr * 2, end)


print(f(1, 10) * f(10, 20))
