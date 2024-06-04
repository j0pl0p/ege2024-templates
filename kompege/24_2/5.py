line = open('data/5.txt').readline().strip()
ans = 0
for i in range(len(line)-3):
    s = line[i:i+3]
    if s == 'XIX':
        ans+=1
print(ans)