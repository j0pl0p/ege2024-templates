import itertools

letters = 'МИМИКРИЯ'
count = 0
combinations = set()
for i in itertools.permutations(letters):
    i = ''.join(i)
    combinations.add(i)
print(len(combinations))
