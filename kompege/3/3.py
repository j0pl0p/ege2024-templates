import itertools

letters = 'ПУЛЯ'
count = 0
for i in itertools.product(letters, repeat=6):
    i = ''.join(i)
    if all([
        i.count('У') == 2
    ]):
        count += 1
print(count)
