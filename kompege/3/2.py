import itertools

letters = 'ABCWXYZ'
count = 0
for i in itertools.product(letters, repeat=6):
    i = ''.join(i)
    for j in 'WXYZ': i = i.replace(j, '*')
    if all([
        i[0] == '*',
        '*' not in i[1:-1],
        i[-1] == '*'
    ]):
        count += 1
print(count)
