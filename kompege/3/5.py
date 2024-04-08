import itertools

letters = 'САЛО'
count = 0
for i in itertools.product(letters, repeat=6):
    i = ''.join(i)
    if all([
        1 <= i.count('О') <= 3
    ]):
        count += 1
print(count)
