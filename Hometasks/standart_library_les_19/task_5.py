"""
Напишите функцию для создания строки HTML с тегами вокруг слов (использовать шаблону из модуля string).
Пример функции и результата:
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""


from string import Template


def add_tags(tag, message):
    return Template("${name}" + message + "${name_1}").substitute(name=f'<{tag}>', name_1=f'</{tag}>')


if __name__ == '__main__':
    print(add_tags('i', 'hi'))
    print(add_tags('b', 'My friend'))
