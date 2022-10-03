# Напишите проrрамму, которая бы считала по просьбе пользователя. Надо
# позволить пользователю ввести начало и конец счета, а также интервал между
# называемыми целыми числами.


def get_int(welcome_message):
    while True:
        try:
            _int = int(input(welcome_message))
        except ValueError as e:
            print('Так нельзя!', e)
        else:
            break
    return _int


def my_range(start, end, step):
    for item in range(start, end, step):
        print(item)


if __name__ == '__main__':
    start = get_int('Введите начало диапазона: ')
    end = get_int('Введите конец диапазона: ')
    step = get_int('Введите шаг для прохождения диапазона: ')
    my_range(start, end, step)
