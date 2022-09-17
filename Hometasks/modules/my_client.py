"""
3. Вложенные операции импортирования. Создайте второй модуль, my_client.py,
который импортирует модуль my_mod и тестирует его функции.

4. Операции импортирования пакетов. Импортируйте свой файл из пакета. Создайте подкаталог по имени my_pkg внутри
 рабочего каталога, переместите в новый подкаталог файл модуля my_mod.py, созданный в упражнении 1,
  и попробуйте импортировать его с помощью операции импортирования пакета в форме import mypkg.mymod,
  после чего вызовите функции модуля. Попробуйте извлечь функции подсчета и посредством from тоже.
"""

# import my_mod
# from Hometasks.modules.my_pkg import my_mod
# import my_pkg.my_mod  #не работает
# import Hometasks.modules.my_pkg.my_mod #не работает
from my_pkg.my_mod import count_line
from my_pkg.my_mod import count_chars
from my_pkg.my_mod import test


print(count_line('text.txt'))
print(count_chars('text.txt'))
print(test('text.txt'))
