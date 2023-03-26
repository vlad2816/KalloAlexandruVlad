# 2. Sa se scrie o functie care primeste o lista de numere si \
#     verifica daca exista cel putin un numar pozitiv. \
#         Functia trebuie sa returneze True daca exista cel putin un numar pozitiv, si False altfel. Folositi functia any.

def positive_list(*lista):
    if any(lista):
        return True
    else:
        return False


print(positive_list(False, False, False, 0))
