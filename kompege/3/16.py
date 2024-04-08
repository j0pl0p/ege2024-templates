import itertools

letters = 'ВАЙФУ'
count = 0
for i in itertools.product(letters, repeat=4):
    i = ''.join(i)
    if len(set(list(i))) == 4:
        if all([
            'ФВ' not in i,
            i[0]!='Й',
            'ВФ' not in i
        ]):
            count += 1
print(count)
