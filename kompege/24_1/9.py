s = open('data/9.txt').readline().strip()
for i in [
    '11A', '11B',
    '12A', '12B',
    '21A', '21B',
    '22A', '22B',
]:
    s = s.replace(i, '*')
for i in '12AB':
    s = s.replace(i, ' ')
print(max(len(i) for i in s.split()))