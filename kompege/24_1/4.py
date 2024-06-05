s = open('data/4.txt').readline().strip()
for i in ['XZ', 'XY']:
    s = s.replace(i, ' ')
print(len(sorted(s.split(), reverse=True, key=len)[0])+2)