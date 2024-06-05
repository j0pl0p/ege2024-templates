s = open('data/5.txt').readline().strip()
while 'PP' in s:
    s=s.replace('PP', 'P P')
print(max(len(i) for i in s.split()))