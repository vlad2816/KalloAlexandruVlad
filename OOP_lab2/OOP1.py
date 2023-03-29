from autos import Car
from users import Person
from autos import Gas_station


gas = Gas_station(1234)

gas.set_price(6.55, 1234)
print(gas.get_price())
ford = Car()
print(f'Aveti de plata: {gas.fill(ford, 10)}')
print(ford.get_gas_percentage())

ford = Car()
vlad = Person()
maria = Person()

print(ford.get_gas_percentage())
print(ford.get_consumption())
ford.add_person(vlad)
ford.add_person(maria)
print(ford.get_gas_percentage())
print(ford.get_consumption())

# ford.start_engine()
# ford.refill(35)
# ford.drive()
# ford.drive(1)
# """Stop engine + pus pompa pe busy si apoi pe free """
