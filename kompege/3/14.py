count = 0
for d1 in '123456789':
    for d2 in '0123456789':
        for d3 in '0123456789':
            digits = list(map(int, [d1, d2, d3]))
            if d1 <= d2 <= d3:
                count+=1

print(count)