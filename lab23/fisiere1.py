# C:\Users\Vlad\Desktop\programare curs\vs code\lab22\atm_project\tests\test_atm_card.py =Cale absoluta
# lab22\atm_project\tests\test_atm_card.py = Cale relativa
from pathlib import Path
from datetime import datetime

working_dir = Path('.')  # current working directory

print(working_dir)
print(f'Curent working directory: {working_dir.absolute()}')
script_path = Path(__file__)
# Direct calea absoluta catre fisierul unde ma aflu
print(f'Script path :{script_path}')
print(f'Parent directory (folder of script): {script_path.parent}')

print(f'Check if the script exist: {script_path.exists()}')

# c:\Users\Vlad\Desktop\programare curs\vs code\lab23\program_data\start_time.txt

start_time_path = script_path.parent / 'program_data' / 'start_time.txt'

# if not start_time_path.parent.exists():
#     start_time_path.parent.mkdir()  # Make directory
#     print(f'Created:  {start_time_path}')

start_time_path.mkdir(exist_ok=True, parents=True)

# print(start_time_path.is_dir())
# print(start_time_path.is_file())


# fis1 = open(start_time_path / 'test.txt', 'w')


# fis1.close()
now = datetime.now()
now_file_name = now.strftime('%Y%m%d_%H%M%S.txt')

with open(start_time_path / now_file_name, 'w') as fout:  # Fout => File descriptor
    fout.write('No Error')

print('file operation done! ')
