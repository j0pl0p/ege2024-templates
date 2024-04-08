import itertools

letters = 'AB123'
count = 0
for i in itertools.product(letters, repeat=8):
    i = ''.join(i)
    if all([
        i.count('A') + i.count('B') == 2
    ]):
        count += 1
print(count)
