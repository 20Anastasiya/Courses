# Определите класс Circle, представляющий окружность и включающий:
#
# статический метод, переводящий метры в сантиметры или наоборот;
# метод, инициализирующий радиус экземпляра;
# методы получения длины и площади окружности.
# Используя созданный класс, расчитайте и выведите на экран длину и площадь
# окружности в сантиметрах зная, что ее радиус равен 2.55 метра.

from math import pi


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def sm2m(sm):
        return sm * 100

    def get_len(self):
        return 2 * pi * self.radius

    def get_square(self):
        return pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(2.55)
    _len = circle.get_len()
    print(Circle.sm2m(_len))
    print(circle.get_square())
