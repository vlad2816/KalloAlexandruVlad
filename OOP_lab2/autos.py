class Car:
    """Representation of a virtual car."""

    def __init__(self):  # constructor
        self.__cmc = 1600
        self.__doors = 4
        self.__tank_capacity = 45
        self.__gas_in_tank = 0
        self.__passengers = []
        self.__engine_running = False

    def add_person(self, person):
        if len(self.__passengers) == self.__doors:
            raise ValueError('Not enough space.')
        self.__passengers.append(person)

    def get_gas_percentage(self):
        """Get current gas level in tank."""
        return self.__gas_in_tank / self.__tank_capacity * 1000

    def start_engine(self):
        """Start the car"""
        if not self.__engine_running:
            self.__engine_running = True

    def stop_engine(self):
        """Stop the car"""
        if self.__engine_running:
            self.__engine_running = False

    def drive(self, km):
        if not self.__engine_running:
            raise ValueError('Engine not running ')

        if not self.can_drive(km):
            raise ValueError('Not enough resources')

        self.__gas_in_tank -= self.get_consumption() * km

    def refill(self, litters):
        if litters > self.__tank_capacity - self.__gas_in_tank:
            raise ValueError("Overflow")
        self.__gas_in_tank = litters

    def get_doors(self):
        return self.__doors

    def can_drive(self, km):
        _range = self.__gas_in_tank / self.get_consumption()
        if _range < km:
            return False
        return True  # if range >= km => True (short version with return True)

    def get_consumption(self):
        return (self.__cmc / 100000 * 4) + 0.5 * len(self.__passengers)


class Gas_station:
    """Making a gas station"""

    def __init__(self, pin):
        self.__price = 0
        self.__busy = False
        self.__pin = pin

    def is_busy(self):
        return self.__busy

    def get_price(self):
        return self.__price

    def set_price(self, price, pin):
        if pin != self.__pin:
            raise ValueError('Wrong pin')
        self.__price = price

    def fill(self, car: Car, litters: int):
        if self.__busy:
            raise ValueError('Is busy')
        car.stop_engine()
        self.__busy = True
        for x in range(1, litters + 1):
            try:
                car.refill(1)
            except ValueError:
                break
        self.__busy = False
        return x * self.__price

    """Stop engine + pus pompa pe busy si apoi pe free """
