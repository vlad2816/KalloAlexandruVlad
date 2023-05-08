from pathlib import Path
import os

ROOT = Path(__file__).parent

input_file_path = ROOT / 'git.txt'


try:
    with open(input_file_path, 'r') as fin:
        print(fin.tell())  # Arata pozitia cursorului in fisierul txts
        fin.read()
        print(fin.tell())
        fin.seek(0, os.SEEK_SET)  # modifica cursorul fisierului
        print(fin.tell())
        print(fin.read(10))
        print(fin.tell())
        fin.seek(0, os.SEEK_CUR)
        print(fin.tell())
except OSError as err:
    print(err)

# 1 chr = 1 byte
