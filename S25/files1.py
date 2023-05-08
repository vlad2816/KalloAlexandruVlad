from pathlib import Path

ROOT = Path(__file__).parent

input_file_path = ROOT / 'ids.txt'


try:
    with open(input_file_path, 'r') as fin:
        print(fin.read(10))
        print(fin.read(10))
        print(fin.read(10))
except OSError as err:
    print(err)
