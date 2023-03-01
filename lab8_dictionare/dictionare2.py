student_grades = {
    'Ana': 9.5,
    'Ioan': 8.0,
    'Maria': 7.5,
    'Andrei': 9.0,
    'Elena': 10.0
}

print(student_grades['Ana'])

print(student_grades.get('Ana')) #Obtinerea unei valori dintr un dictionar.
#cu metoda get nu obtinem erroare in cazul in care key search nu este corecta.

nota = student_grades.get('Ionut')

if nota is not None:
    print(nota)
else:
    print('Studentul nu este in aceasta grupa')
