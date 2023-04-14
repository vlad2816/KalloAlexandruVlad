# Error and exceptions

x = -5

# if x < 0:
# raise Exception('x should be positive')

# assert (x >= 0), 'x is not positive'

try:
    a = 5/1  # 5/0 zero div
    b = a + 10  # int + str type error
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print('Error!!!', e)
else:
    print('Everything is fine ')  # if we dont have errors.
