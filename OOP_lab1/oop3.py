class Car:
    """Representation of a virtual car."""

    def __init__(self):  # constructor
        self.__cmc = 0
        self.__door = 4
        self.__tank_capacity = 45
        self.__gas_in_tank = 15
        self.__passengers = []  # attribute private cu __

    def start_engine(self):
        pass

    def stop_engine(self):
        pass

    def drive(self):
        pass

    def refill(self):
        pass

    def get_doors(self):
        return self.__door

    def get_gas_percentage(self):
        return self.__gas_in_tank / self.__tank_capacity * 100


class Person:

    def __init__(self):  # constructor
        self.__height = 187  # cm
        self.__weight = 0

    def get_height_cm(self):
        return self.__height

    def get_height_m(self):
        return self.__height / 100


vlad = Person()
maria = Person()


vw = Car()
ford = Car()
print(vw.get_doors())
print(f'Gas for VW: {vw.get_gas_percentage()} %')

print(
    f'Inaltime Vlad in cm: {vlad.get_height_cm()} Inaltime Vlad in m: {vlad.get_height_m()}')
