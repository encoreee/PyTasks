def dice():
    total = 0
    for i in range(2):
        import random
        total += random.randint(1, 6)
    return total


d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

if __name__ == '__main__':
    for j in range(1000):
        val = dice()
        print(val)
        if val == 2:
            d[0] += 1
        elif val == 3:
            d[1] += 1
        elif val == 4:
            d[2] += 1
        elif val == 5:
            d[3] += 1
        elif val == 6:
            d[4] += 1
        elif val == 7:
            d[5] += 1
        elif val == 8:
            d[6] += 1
        elif val == 9:
            d[7] += 1
        elif val == 10:
            d[8] += 1
        elif val == 11:
            d[9] += 1
        elif val == 12:
            d[10] += 1

print(d)
