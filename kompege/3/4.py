import itertools

letters = 'ЛОДКА'
count = 0
for i in itertools.product(letters, repeat=4):
    i = ''.join(i)
    if all([
        i.count('О') >= 2
    ]):
        count += 1
print(count)
