s = open('data/2.txt').readline().strip()
for i in 'ABC':
    s = s.replace(i, ' ')
print(max(len(i) for i in s.split()))