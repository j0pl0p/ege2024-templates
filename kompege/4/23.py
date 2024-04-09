for y in '0123456789abcdefg':
    for x in '0123456789abcde':
        if (int(f'123{x}5', base=15) + int(f'67{y}9', base=17)) % 131 == 0:
            print(x,y,(int(f'123{x}5', base=15) + int(f'67{y}9', base=17)) / 131)
