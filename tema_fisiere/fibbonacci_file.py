from pathlib import Path
import time

fibo_path = Path(__file__)


def fibo():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


file_place = fibo_path.parent / 'Fibo_Work'
file_place.mkdir(exist_ok=True, parents=True)

with open(file_place / 'Tema_fibo.txt', 'w') as fout:
    fout.write('Fibo work')
