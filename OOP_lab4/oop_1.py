class Shape:

    def __init__(self, color):

        self.__color = color

    def set_color(self, color):
        self.__color = color

    def __str__(self) -> str:
        return f'<{__class__.__name__} color: {self.__color}>'

    # Metoda abstracte , inca nu este definita, nu face nimic sau este implementata mai tarziu de subclasa.
    def area(self):
        pass


class Square(Shape):
    def __init__(self, length, color='Red'):
        super().__init__(color)  # Constructor clasa mama
        self.__length = length

    def area(self):
        return self.__length ** 2


class Triangle(Shape):
    def __init__(self, l1, l2, l3, color='Blue'):
        super().__init__(color)
        self.__l1 = l1
        self.__l2 = l2
        self.__l3 = l3

    def area(self):
        return self.__l1 * self.__l2 * self.__l3


shapes = [Triangle(1, 2, 3), Triangle(2, 2, 3), Square(3), Square(4)]

for shape in shapes:
    print(shape.area())
