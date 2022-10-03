# Дано множество целых чисел {-3, 8, 15, -5, 0, 7}. Выведите на экран
# произведение максимального и минимального элементов, сумму элементов не
# превышающих 7.


# sum_under_7 = lambda _set: sum(filter(lambda x: x < 7, _set))
# эта лямбда аналогична функции, написанной ниже


def sum_under_7(_set):
    return sum(filter(lambda x: x < 7, _set))


def print_set_info(_set):
    print(f'Min: {min(_set)}')
    print(f'Max: {max(_set)}')
    print(f'Sum under 7: {sum_under_7(_set)}')


if __name__ == '__main__':
    _set = {-3, 8, 15, -5, 0, 7}
    print_set_info(_set)
