from pathlib import Path


fibo_path = Path(__file__)


def fibo():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


file_place = fibo_path.parent / 'Fibo_Work'
file_place.mkdir(exist_ok=True, parents=True)

for i in range(1, 101):
    file_number = (f'{i}.txt')
    with open(file_place / file_number, 'w') as fout:
        for fibonacci in file_number:
            fout.write(str(next(fibo())))
