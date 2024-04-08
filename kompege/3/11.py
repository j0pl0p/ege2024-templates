import itertools

letters = 'ВИШНЯ'
count = 0
for i in itertools.product(letters, repeat=6):
    i = ''.join(i)
    if all([
        i.count('В') < 2,
        i[0] != 'Ш',
        i[-1] not in 'ИЯ'
    ]):
        count += 1
print(count)
