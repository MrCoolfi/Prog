c = []
for m in range(2, 1000, 2):
    for n in range(1, 1000, 2):
        x = 2**m * 3**n
        if x >= 400000000 and x <= 600000000:
            c.append(x)
        if x > 600000000:
            break
c.sort(reverse=False)
for i in c:
    print(i)
