def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def add_one(number):
    number += 1


a = 3
x = is_even(a)
print(f'Variabila din functie este nr par? {x}')

print(f'a = {a}')
add_one(a)
print(f'a = {a}')
