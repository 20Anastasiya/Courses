class Car:
    default_color = 'red'
    default_type = 'lorry'
    default_year = 1977
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, color=None, type=None, year=None):
        self.color = color or self.default_color
        self.type = type or self.default_type
        self.year = year or self.default_year

    def start(self):
        print('Автомобиль заведён')

    def end(self):
        print('Автомобиль заглушен')

    def new_year(self, new_year):
        self.year = new_year

    def new_type(self, new_type):
        self.type = new_type

    def new_color(self, new_color):
        self.color = new_color

    def __str__(self):
        return f'{self.color} {self.type} {self.year}'


car = Car()
print(car)
car.start()
car.end()
car.new_year(2002)
car.new_color('black')
print(car)
