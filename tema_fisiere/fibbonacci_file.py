from pathlib import Path
import sys


ROOT = Path(__file__)


def fibo():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b


# Create output dir
output_path = ROOT / 'Fibo_Work'
try:
    output_path.mkdir(exist_ok=True)
except OSError:
    print('Could not create output dir.')
    sys.exit()

fib_gen = fibo()
for i in range(1, 101):
    file_path = output_path / f'{i}.txt'
    try:
        with open(file_path, 'w') as fout:
            fout.write(str(next(fib_gen)))
    except OSError as err:
        print(err)
