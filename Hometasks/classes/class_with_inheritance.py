'''
Напишите набор из шести операторов class для моделирования такой иерархической классификации
с помощью наследования Python. Затем добавьте в каждый класс метод speak, выводящий уникальное сообщение,
а в суперкласс верхнего уровня Animal — метод reply, который просто вызывает self. speak,
чтобы запустить инструмент вывода, специфичный для категории, из подкласса ниже в дереве
(это инициирует независимый поиск при наследовании из self). 
Наконец, удалите метод speak из класса Hacker, чтобы он выбирал стандартный метод, находящийся выше.
Animal
Mammal
Cat
Dog
Primate
Hacker
'''

class Animal:
    def reply(self):
        return self.speak()
    
    
class Mammal(Animal):
    def speak(self):
        return print('?')
    
    
class Cat(Mammal):
    def speak(self):
        return print('Meow')
    
    
class Dog(Mammal):
    def speak(self):
        return print('Woof')
    
    
class Primate(Mammal):
    def speak(self):
        return print('U-u-a')
    
    
class Hacker(Primate):
    def speak(self):
        return super().speak()
        
        
spot = Cat()
spot.reply () # Animal. reply: вызывает Cat.speak 

data = Hacker () # Animal. reply: вызывает Primate.speak
data.reply() 
