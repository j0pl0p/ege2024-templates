line = open('data/6.txt').readline().strip()
count = 0
for i in range(len(line)-4):
    if line[i:i+4] == 'XXXX':
        count+=1
print(count)