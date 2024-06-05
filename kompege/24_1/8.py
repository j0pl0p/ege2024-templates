s = open('data/8.txt').readline().strip()
for i in [
    'BA', 'BO',
    'CA', 'CO',
    'DA', 'DO',
]:
    s = s.replace(i, '*')
for i in 'ABCDO':
    s = s.replace(i, ' ')
print(max(len(i) for i in s.split()))