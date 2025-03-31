def v(i):
    if i == 1 or i == 2: return 0
    if i == 3: return 1.5
    return ((i+1)/(i**2 +1)) * v(i-1) - v(i-2) * v(i-3)

for i in range(1,10):
    print(v(i))