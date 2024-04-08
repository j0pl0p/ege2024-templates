count = 0
for d1 in '1234567':
    for d2 in '01234567':
        for d3 in '01234567':
            for d4 in '01234567':
                for d5 in '01234567':
                    d = d1+d2+d3+d4+d5
                    if '1' not in d and len(set(list(d))) == 5:
                        for s in '1357': d= d.replace(s, 'n')
                        for s in '0246': d = d.replace(s, 'c')
                        if 'cc' not in d and 'nn' not in d:
                            count += 1

print(count)