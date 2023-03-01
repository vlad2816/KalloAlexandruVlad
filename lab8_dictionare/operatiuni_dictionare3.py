# cum extragem lista keylor:
student_grades = {
    'Ana': 9.5,
    'Ioan': 8.0,
    'Maria': 7.5,
    'Andrei': 9.0,
    'Elena': 10.0
}


lista_chei = student_grades.keys()

print(type(lista_chei))

print(lista_chei)

for key in student_grades.keys():
    print(key)

print('-' * 30)
#cum extragem lista de valori.

for value in student_grades.values():
    print(value)

print('-' *30)

# Cum extragem lista de chei/valori impreuna perechi.

valori = student_grades.items()

for v in valori:
    name, grade = v
    print(name, grade)  #unpacking





