import itertools

letters = 'АБИКОЛУН'
count = 0
for i in itertools.permutations(letters):
    i = ''.join(i)
    for s in 'БКЛН': i = i.replace(s, 's')
    for s in 'АИОУ': i = i.replace(s, 'g')
    if all([
        'ss' not in i,
        'gg' not in i
    ]):
        count += 1
print(count)
