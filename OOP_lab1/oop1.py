# Class and object
# Class name need to start with  Caps Lock

class AirplaneTicket:
    pass


# instantiere creare obiect

tk1 = AirplaneTicket()
tk2 = AirplaneTicket()

print(tk1)
print(tk2)

print(type(tk1))
print(type(AirplaneTicket))

print(isinstance(tk1, AirplaneTicket))
# stergere obiect

del tk1
