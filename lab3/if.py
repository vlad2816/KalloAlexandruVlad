# Raspunde la intrebarea daca ( conditie ).

var = 134

if var % 2 == 0:
    print('Acest numar este par')
else:
    print('Acest numar este impar')

print('*' * 10)

varsta = 17

if varsta <= 18:
    print('Nu ai voie sa cumperi alcool')
else:
    print('Ai voie sa cumperi alcool')

print('*' * 10)


if not 1 == 0:
    print('se executa')

print('*' * 8)

# varsta = int(input('In ce an esti nascut?: '))

varsta_calculata = 2023 - varsta

if varsta_calculata <= 20:
    print('Hello')
else:
    print('Hello x2')

print('*' * 10)


# elif mai multe conditii:

ora = int(input('Ce ora este?: '))

if ora >= 5 and ora < 10:
    print('Buna dimineata')

elif ora >= 10 and ora < 17:
    print('Buna ziua')

elif ora >= 17 and ora < 21:
    print('buna seara')

else:
    print('Noapte buna ')
