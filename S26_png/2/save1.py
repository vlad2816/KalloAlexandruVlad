import sys
from pathlib import Path

ROOT = Path(__file__).parent

png_file_path = Path(sys.argv[1])  # Cli exec

if not png_file_path.is_file():
    print('File not found')  # Verificare daca este fisier
    sys.exit(1)

try:
    with open(png_file_path, 'rb') as fin:  # rb Read bytes.
        content = fin.read()
except OSError as err:
    print(err)
    sys.exit(1)
else:
    try:
        with open(png_file_path.parent / f'Prima_jumatate{png_file_path.name}', 'wb') as fout:
            fout.write(content[:(len(content) - 1) // 2])
        with open(png_file_path.parent / f'Jumatate_x2{png_file_path.name}', 'wb') as fout:
            fout.write(content[(len(content) - 1) // 2:])
    except OSError as err:
        print(err)
