# 4. Creați un dicționar cu numele și vârsta a trei persoane. Creați o listă
# cu numele acestor persoane și sortați lista în ordine alfabetică inversă.
# Afișați lista sortată.

dictionar = {"Vlad": 24, "Andrei": 25, "Cristi": 30}

lista = list(dictionar.keys())  # transformare din dict in lista.

lista.sort(reverse=True)  # Sortare lista.
print(lista)
