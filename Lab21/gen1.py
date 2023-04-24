import time


def get_numbers():
    return [2, 3, 4, 5, 6, 7, 8, 232, 465]


def rand_numbers():
    a = 0
    b = 1

    while True:
        yield b
        a, b = b, a + b


numb_gen = rand_numbers()

# try:
#     print(next(numb_gen))
#     print(next(numb_gen))
# except StopIteration:
#     print('End of gen')

for i in numb_gen:
    time.sleep(1)
    print(i)
