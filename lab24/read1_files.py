from pathlib import Path

ROOT = Path(__file__).parent

input_file_path = ROOT / 'ids.txt'


try:
    with open(input_file_path, 'r') as fin:
        content = fin.read(10)
        print(content)

        content2 = fin.read(6)
        # De fiecare data cand apelam read cu argument el va ramane unde a ramas nu incepe de la inceput
        print(content2)
except OSError as err:
    print(err)
