class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        # return f'Результат сложения: {self.a + self.b}'
        print(f'Результат сложения: {self.a + self.b}')

    def multiplication(self):
        print(f'Результат умножения: {self.a * self.b}')

    def division(self):
        print(f'Результат деления: {self.a / self.b}')

    def subtraction(self):
        print(f'Результат вычитания: {self.a - self.b}')


obj_1 = Math(10, 4)
obj_1.multiplication()
