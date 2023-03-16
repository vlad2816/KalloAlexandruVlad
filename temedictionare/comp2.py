# Creați o listă cu patru dicționare, fiecare dicționar conținând numele,
# vârsta și salariul unui angajat. Iterați prin lista și afișați numele și
# salariul fiecărui angajat

my_list = [
    {"nume": "Ana", "varsta": 25, "salariu": 3000},
    {"nume": "Ioan", "varsta": 32, "salariu": 4500},
    {"nume": "Maria", "varsta": 41, "salariu": 5000},
    {"nume": "Andrei", "varsta": 19, "salariu": 2500},
]

for i in my_list:
    print(i["nume"], i["salariu"])
