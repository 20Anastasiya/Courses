"""
Напишите игру Кости
"""


from random import randint


dice_1 = randint(1, 6)
dice_2 = randint(1, 6)

print('Ваш результат: ', dice_1 + dice_2)

if dice_1 == dice_2:
    print('Дубль!')