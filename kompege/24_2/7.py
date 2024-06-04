line = open('data/7.txt').readline().strip()
count = 0
for i in range(len(line) - 4):
    if line[i] == 'G' and line[i + 2:i + 4] == 'ME':
        count += 1
print(count)
