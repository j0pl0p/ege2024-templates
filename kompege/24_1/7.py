s = open('data/7.txt').readline().strip()
s = s.replace('NPO', '*').replace('PNO', '*')
for i in 'NOP':
    s = s.replace(i, ' ')
print(max(len(i) for i in s.split()))