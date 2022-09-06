class Student:
    default_name = 'Ivan'
    default_group_number = '10A'
    default_age = 18


    def __init__(self, name='Ivan', group_number='10A', age=18):
        self.name = name or self.default_name
        self.group_number = group_number or self.default_group_number
        self.age = age or self.default_age


    def get_name(self):
        return f'Name: {self.name}.'


    def get_group_number(self):
        return f'Group number: {self.group_number}.'


    def get_age(self):
        return f'Age: {self.age}.'


    def set_name_age(self, new_name, new_age):
        self.name = new_name or self.default_name
        self.age = new_age or self.default_age


    def set_group_number(self, new_group_number):
        self.group_number = new_group_number or self.default_group_number


Anastasiya = Student('Anastasiya', '11A', 17)
Uliya = Student('Uliya', '11A', 17)
Andrey = Student('Andrey', '11Б', 18)
Vitaliy = Student('Vitaliy', '10A', 16)
Sergey = Student('Sergey', '11Б', 18)
Ivan = Student()

print(Sergey.get_name(), Sergey.get_group_number(), Sergey.get_age())
print(Ivan.get_name(), Ivan.get_group_number(), Ivan.get_age())
Ivan.set_name_age('Maksim', 17)
Ivan.set_group_number('11Б')
print('Ivan was', Ivan.get_name(), Ivan.get_group_number(), Ivan.get_age())
