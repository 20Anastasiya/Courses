# Напишите функцию с названием reverse_lookup, которая будет осуществлять поиск
# всех ключей в словаре по заданному значению. Функция должна принимать в
# качестве параметров словарь и значение для поиска и возвращать список ключей
# (он может быть пустым) из этого словаря, соответствующих переданному значению.


def reverse_lookup(_dict, _value):
    result = []

    for key, value in _dict.items():
        if value == _value:
            result.append(key)

    return result

    # return [key for key, value in _dict.items() if value == _value]
    #заменяет всю функцию


if __name__ == '__main__':
    dict_1 = {'d': 4, 'b': 2, 'a': 2, 'c': 3, 'g': 5, 'r': 4}
    print(reverse_lookup(dict_1, 2))
