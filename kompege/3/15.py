import itertools

letters = 'ДЕЙКСТРА'
count = 0
for i in itertools.product(letters, repeat=6):
    i = ''.join(i)
    if len(set(list(i))) == 6:
        for s in 'ДКСТР': i = i.replace(s, 's')
        if all([
            i.count('Йs') == 1,
        ]):
            count += 1
print(count)
