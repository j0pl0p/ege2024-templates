k = 0
for x in range(-300, 300):
    for y in range(-300, 300):
        if all([
            y < 3 * x,
            y > 0,
            y < 15,
            y > x / 4 - 14,
        ]):
            k += 1
print(k)
