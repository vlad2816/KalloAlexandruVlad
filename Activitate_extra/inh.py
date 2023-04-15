class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"Hello i'm a {self.tipo} and my sound is: {self.sound}")


class Cat(Animal):
    tipo = 'Cat'


class Dog(Animal):
    tipo = 'Dog'


class Wolf(Animal):
    tipo = 'Wolf'

    def __init__(self, name, sound):
        super().__init__(name, sound)
        print('More functionality')


c1 = Cat('Fluffy', 'miau')
c1.speak()

d1 = Dog('Atos', 'ham')
d1.speak()

w1 = Wolf('Flex', 'aufff')
w1.speak()
