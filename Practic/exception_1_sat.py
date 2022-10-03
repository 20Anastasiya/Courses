# Напишите функцию по имени oops, которая при вызове явно генерирует исключение
# IndexError.


# def oops():
#     raise IndexError
#
#
# if __name__ == '__main__':
#     oops()

# Измените написанную в упражнении 1 функцию oops, чтобы она генерировала
# определенное вами исключение по имени МуЕrrоr. Идентифицируйте свое исключение
# с помощью класса. Затем расширьте оператор try в перехватывающей функции
# для перехвата этого исключения и его экземпляра в дополнение к IndexError,
# а также вывода перехваченного экземпляра.

from random import randint

class MyError(Exception):
    pass


def oops():
    if randint(0, 1) == 1:
        raise IndexError('ind')
    raise MyError('my')


if __name__ == '__main__':
    try:
        oops()
    except IndexError as e:
        print(e)
    except MyError as e:
        print(e)
