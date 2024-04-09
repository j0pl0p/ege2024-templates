import sys

for x in '0123456789abcdefghijk':
    flag = True
    for y in '0123456789abcdefghijk':
        if (int(f'12{y}{x}9', base=21) + int(f'36{y}99', base=21)) % 18 != 0:
            flag=False
            break
    if flag:
        y=5
        print((int(f'12{y}{x}9', base=21) + int(f'36{y}99', base=21)) / 18)
        sys.exit()
