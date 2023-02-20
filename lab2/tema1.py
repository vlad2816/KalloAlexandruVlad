# . Sa se converteasca in binar (baza 2) urmatoarele numere: 16, 32, 64, 128, 100, 10, 54, 33.

# 128- 64- 32- 16- 8- 4- 2- 1.

# 16 = 1 0 0 0 0 (16 -8 -4 -2 -1)
# 32 = 1 0 0 0 0 0 (32 -16 -8 -4 -2 -1)
# 64 = 1 0 0 0 0 0 0 (64- 32 -16 -8 -4 -2 -1)
# 128 = 1 0 0 0  0 0 0 0 (128- 64- 32 -16 -8 -4 -2 -1)
# 100 = 1 1 0 0 1 0 0 (64- 32- 16- 8- 4- 2- 1)
# 10 = 1 0 1 0 (8-4-2-1)
# 54 = 1 1 0 1 1 0 (32-16-8-4-2-1)
# 33 = 1 0 0 0 0 1 (32-16-8-4-2-1)

# Exercitiul nr 2: 2. Sa se converteasca in decimal (baza 10) urmatoarele numere:  1010 0101,  1111 1111, 0010 0001, 1000 0000

# 128-64-32-16-8-4-2-1 

# 1010 0101 = (1 + 4 + 32 + 128 = 165 )
# 1111 1111 = (1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 = 255)
# 0010 0001 = (1 + 32 = 33 )
# 1000 0000 = 128 


# Exercitii variabile:
# Definiti 2 variabile; prima reprezinta varsta voastra iar a 2-a numele:

varsta = 24 
nume = ' Kallo Alexandru Vlad '


# Exercitiul nr 2:

cos_de_cumparaturi = 0

print(type(cos_de_cumparaturi))

cos_de_cumparaturi =34.56

print(type(cos_de_cumparaturi))

print(int(cos_de_cumparaturi))

print('')
print('Trecem la urmatorul exercitiu:')
print('')

# Exercitiu nr 3:

variabila = None
print(type(variabila))

variabila = True
print(type(variabila))

variabila = 'True'
print(type(variabila))

variabila = 0
print(type(variabila))

print('')
print('Trecem la urmatorul exercitiu:')
print('')


# Exercitiu nr 4:

numar_bin = '00001010' # = 10 

numar_dec = int(numar_bin, 2)

print(numar_dec)




 