'''
Напишите программу, которая содержит генератор calculation(),
который принимает два параметра и вычисляет сумму и разность.
Сперва возвращается сумма, потом разность. Результат вывести на
экран.

'''

def calculation(x, y):
    yield f'Сумма: {x + y}'
    yield f'Разность: {x - y}'
    
calculation = calculation(3, 5)
print(next(calculation))
print(next(calculation))
