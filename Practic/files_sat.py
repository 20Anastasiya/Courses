# В данном упражнении вам необходимо написать функцию, проверяющую введенный
# пароль на надежность. Определим как надежный пароль, состоящий минимум из
# восьми символов и включающий хотя бы по одной букве в верхнем и нижнем
# регистрах, как минимум одну цифру и как минимум спец. символ. Функция должна
# возвращать True, если переданный в качестве параметра пароль отвечает
# требованиям надежности. В противном случае возвращаемым значением должно быть
# False. В основной программе необходимо запросить у пользователя пароль и
# оповестить его о том, является ли он достаточно надежным.

from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def password_init(password):
    if len(password) < 8:
        return False
    if len(list(filter(lambda x: x in ascii_lowercase, password))) == 0:
        return False
    if len(list(filter(lambda x: x in ascii_uppercase, password))) == 0:
        return False
    if len(list(filter(lambda x: x.isdigit(), password))) == 0:
        return False
    if len(list(filter(lambda x: x in punctuation, password))) == 0:
        return False
    return True


def get_str(welcom_message):
    _str = input(welcom_message)
    return _str


if __name__ == '__main__':
    password = get_str('Введите пароль: ')
    print(password_init(password))
