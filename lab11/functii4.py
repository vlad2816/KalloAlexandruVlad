def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


for i in range(0, 51):
    if is_even(i):
        print(i)
