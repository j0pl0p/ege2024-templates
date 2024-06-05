s = open('data/3.txt').readline().strip().lower()
for i in 'qwertyuiopasdfghjklzxcvbnm':
    s = s.replace(i, ' ')
print(max(len(i) for i in s.split()))