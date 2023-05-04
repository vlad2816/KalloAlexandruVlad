from pathlib import Path

name = str(input('Please enter your name: '))
script_path = Path(__file__)
print(script_path)
print(f'Aici avem folderul in care se afla: {script_path.parent}')
# c:\Users\Vlad\Desktop\programare curs\vs code\tema_fisiere

name_path = script_path.parent / 'name_file_input' / 'my_name.txt'
name_path.mkdir(exist_ok=True, parents=True)

with open(name_path / 'my_name.txt', 'w') as fout:
    fout.write(name)

print('job done')
