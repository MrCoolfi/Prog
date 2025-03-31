from itertools import product
С = 0
for i in product('ВИШНЯ',repeat=6):
    if i.count('В') < 2 and i[0] != 'Ш' and i[5] != 'И' and i[5] != 'Я':
        С = С +1
print(С)

