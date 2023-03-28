class Car:
    """Representation of a virtual car."""

    def __init__(self, car_name, cmc, tank_capacity, gas_in_tank, engine_running, km_to_travel):
        self.car_name = car_name
        self.cmc = cmc
        self.tank_capacity = tank_capacity
        self.gas_in_tank = gas_in_tank
        self.engine_running = engine_running
        self.km_to_travel = km_to_travel

    def turn_on(self):
        """Checking if the motor is running."""
        if self.engine_running == True:
            return f'{self.car_name} is running !'
        else:
            self.engine_running = True
            return f'{self.car_name} Turned on! '

    def get_gas_percentage(self):
        """Get current gas level in tank."""
        return self.gas_in_tank / self.tank_capacity * 100

    def get_gas_per_km(self):
        """Gas consumption per km """
        return (self.cmc) / 1000 * 4

    def distance(self):
        if self.km_to_travel < self.get_gas_per_km * self.gas_in_tank:
            raise ValueError('We dont have enough gas')


vw = Car('vw', 3000, 45, 10, False, 200)

print(vw.turn_on())
print(vw.get_gas_percentage())
print(vw.get_gas_per_km())
print(vw.distance())
