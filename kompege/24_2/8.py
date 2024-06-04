line = open('data/8.txt').readline().strip()
count = 0
for i in range(len(line) - 5):
    if all([
        line[i]=='A',
        line[i+2]=='A',
        line[i+4]=='A'
    ]):
        count += 1
print(count)
