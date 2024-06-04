with open('data/26_225.txt') as f:
    data = f.readlines()
sn, data = data[0], list(map(int, data[1:]))
s, n = map(int, sn.split())
print(s)
data.sort(reverse=True)
i = 0
count, minimalFile = 0, -1
while data[i] <= s:
    minimalFile = data[i]
    s -= data[i]
    count += 1
    i += 1
while data[i] > s:
    i += 1
if data[i] <= s:
    count += 1
    minimalFile = data[i]
print(count, minimalFile)
