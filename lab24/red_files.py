from pathlib import Path

ROOT = Path(__file__).parent

input_file_path = ROOT / 'git.txt'


try:
    with open(input_file_path, 'r') as fin:
        # Readline (citeste tot), readlines (varianta de jos citeste mai multe randuri)
        content = fin.readlines()
except OSError as err:
    print(err)
else:
    for i in content:
        # Verificare daca fisierul string incepe cu o anumita litera simbol.
        if i.startswith('#'):
            print(i.strip('\n\r\t '))
