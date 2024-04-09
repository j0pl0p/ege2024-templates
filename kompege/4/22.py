for i in range(11):
    if int(f'3364{i}', base=11) + int(f'{i}7946', base=12) == int(f'55{i}87', base=14):
        print(int(f'55{i}87', base=14))