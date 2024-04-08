count = 0
for d1 in '0123':
    for d2 in '0123':
        for d3 in '0123':
            for d4 in '0123':
                digits = list(map(int, [d1, d2, d3, d4]))
                if d1 <= d2 <= d3 <= d4:
                    count+=1

print(count)