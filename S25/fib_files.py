from pathlib import Path
import sys

ROOT = Path(__file__).parent


def fib():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b


# create output dir
output_path = ROOT / 'output'

try:
    output_path.mkdir(exist_ok=True)
except OSError:
    print("Could not create output dir.")
    sys.exit(1)

fib_gen = fib()

for i in range(1, 101):
    nume_fisiere = output_path / f"{i}.txt"
    try:
        with open(nume_fisiere, 'w') as fout:
            # with file_path.open('w')
            fout.write(str(next(fib_gen)))
    except OSError as err:
        print(err)
