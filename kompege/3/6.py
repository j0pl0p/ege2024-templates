import itertools

letters = 'ИГРОК'
count = 0
for i in itertools.permutations(letters):
    i = ''.join(i)
    if all([
        i[0] != 'К',
        'РОК' not in i
    ]):
        count += 1
print(count)
