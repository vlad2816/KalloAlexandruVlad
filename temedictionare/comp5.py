# 5. Creați o listă cu cinci dicționare, fiecare dicționar conținând numele și
# notele unui student. Iterați prin lista și calculați media notelor fiecărui
# student. Adăugați media ca o intrare suplimentară în fiecare dicționar.
# Sortați lista în funcție de medie și afișați numele și nota fiecărui student
# în ordine crescătoare a mediilor.

my_list = [
    {"nume": "Ana", "nota": [9, 10, 10]},
    {"nume": "Ioan", "nota": [9, 8, 8]},
    {"nume": "Maria", "nota": [7, 8, 7]},
    {"nume": "Andrei", "nota": [9, 9, 9]},
    {"nume": "Elena", "nota": [10, 10, 10]},
]

for i in my_list:
    i["media"] = sum(i["nota"])/len(i["nota"])


lista_sortata = sorted(my_list, key=lambda x: x["media"])


for student in lista_sortata:
    print(
        f"{student['nume']}: {student['nota']}, media este: {student['media']}")
