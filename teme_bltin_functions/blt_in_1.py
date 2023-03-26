# 1. Sa se scrie o functie care primeste o lista de numere si verifica\
#       daca toate numerele sunt pozitive. Functia trebuie sa returneze \
#         True daca toate numerele sunt pozitive, si False altfel. Folositi functia all.

def positive_list(*lista):
    if all(lista):
        return True
    else:
        return False


print(positive_list(0, 2, 3, 4))
