import itertools

letters = 'ГЕПАРД'
count = 0
for i in itertools.product(letters, repeat=5):
    i = ''.join(i)
    if all([
        i.count('Г') == 1,
        i[0]!='А',
        i[-1]!='Е'
    ]):
        count += 1
print(count)
