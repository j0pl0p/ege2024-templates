s = open('data/1.txt').readline().strip()
s = s.replace('C', ' ').replace('D', ' ')
print(max(len(i) for i in s.split()))