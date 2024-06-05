s = open('data/6.txt').readline().strip()
s = s.split('XZZY')
s.sort(key=len, reverse=True)
print(len(s[0])+6)