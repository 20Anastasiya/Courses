"""
9. Напишите программу, чтобы создать итератор, который удаляет элементы из итерируемого объекта,
если элемент является положительным целым числом.
"""

from itertools import filterfalse


iter_object = list(filterfalse(lambda i: i > 0 or (i > 0 and type(i) == float), [1, 2, -10, 3, 0, -0.4, 3.2, 4, -7, 5, 1, -1]))
print(iter_object)
