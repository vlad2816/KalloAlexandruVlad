# 3. Sa se scrie o functie care primeste o lista de cuvinte si returneaza un dictionar \
#     care contine cuvintele ca si chei, si pozitia \
#         lor in lista ca si valori. Folositi functia enumerate.


lista = ['mere', 'pere', 'castraveti', 'rosii', 'struguri']

print([{k, v} for k, v in enumerate(lista)])
