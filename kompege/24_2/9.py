data = list(map(lambda x: x.strip(), open('data/9.txt').readlines()))
count = 0
for i in data:
    count += i.count('S') == i.count('X')
print(count)
