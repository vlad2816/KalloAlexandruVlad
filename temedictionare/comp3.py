# 3. Creați un dicționar cu numele și nota a patru studenți. Adăugați o
# nouă intrare în dicționar pentru un nou student și actualizați nota unui
# student existent. Afișați numele studenților si nota in ordine alfabetică.

students_grades = {"Ana": 9.5, "Ioan": 8.0, "Maria": 7.5, "Andrei": 9.0}

students_grades["Vlad"] = 10
students_grades["Ana"] = 8


for k, v in sorted(students_grades.items()):  # (sortare dictionar)
    print(k, v)
