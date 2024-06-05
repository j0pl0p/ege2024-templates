s = open('data/11.txt').readline().strip()
for i in 'XYZ':
    s = s.replace(2*i, ' ')
print(len(max(s.split(), key=len)))