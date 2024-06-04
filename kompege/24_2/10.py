data = list(map(lambda x: x.strip(), open('data/10.txt').readlines()))
count = 0
for i in data:
    count += i.count('B') >= i.count('A') * 1.05
print(count)
