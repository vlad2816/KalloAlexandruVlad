import time
from datetime import datetime

now = datetime.now()
# print(now)
# print(type(now))  # (now nu este STR este obiect de tip datetime)
print(now.year)
while True:
    now = datetime.now()
    print(f'{now.hour}:{now.minute}:{now.second}')
    time.sleep(2)
