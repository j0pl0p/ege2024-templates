s = open('data/10.txt').readline().strip()
for i in 'NOP':
    s = s.replace(i, '*')
s = s.replace('**', ' ')
print(len(max(s.split(), key=len)))