# 4. Sa se scrie o functie care primeste doua liste de numere si returneaza o \
#     lista care contine suma elementelor de pe aceleasi pozitii. \
#         Folositi functia zip.

lista1 = [1, 2, 4]
lista2 = [1, 2, 3]

lista3 = list(zip(lista1, lista2))

for k, v in lista3:
    print(k + v)
