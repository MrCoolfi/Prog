#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Papa','Mama','Ya','Sestra']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Papa', 180],
    ['Mama', 175],
    ['Ya', 190],
    ['Sestra', 160]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца -', my_family_height[0][1],'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
obshrost = 0
for i in my_family_height:
    obshrost += i[1]
print('Общий рост моей семьи -', obshrost,'см')