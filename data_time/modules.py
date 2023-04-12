import random
import time  # modul de precizie mare (nanosec)
from datetime import datetime  # Formate obisnuite


l1 = [random.randint(1, 99999) for i in range(1000)]


# print(time.time())  # asa vedem in cat timp se face un print
start = time.time()
l1.sort()
stop = (time.time())
print(f'Executia a durat: {stop - start } sec')
