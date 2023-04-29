lista = []
print('Add an int if you want to stop, write exit.')

while True:
    value = input('Int:')
    if value == 'exit'.lower():
        break
    else:
        try:
            value = int(value)
            lista.append(value)
        except:
            print('Invalid date')
            exit()

result = 0

for x in lista:
    result += x
print(result)
