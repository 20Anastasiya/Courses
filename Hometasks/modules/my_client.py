"""
3. Вложенные операции импортирования. Создайте второй модуль, my_client.py,
который импортирует модуль my_mod и тестирует его функции.
"""


import my_mod


print(my_mod.count_line('text.txt'))
print(my_mod.count_chars('text.txt'))
print(my_mod.test('text.txt'))
