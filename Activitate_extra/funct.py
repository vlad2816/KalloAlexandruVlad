
lista = [1, 2, 3, -4, 5, 6]
count = 'init'

for i in lista:
    if count == 'init':
        count = i
    else:
        count = i if i < count else count
print(f'The min number from the list is {count} ')
