# items returneaza o lista de tupluri.


student_grades = {
    'Ana': 9.5,
    'Ioan': 8.0,
    'Maria': 7.5,
    'Andrei': 9.0,
    'Elena': 10.0
}

# sau doar in o linie  ###########

for k, v in sorted(student_grades.items()):
    print(k, v)

print('-'*20)
# sortare dupa valori in dictionar (tuplu (key-value))

def  extract(x):
    return x[1]

for k, v in sorted(student_grades.items(), key = extract):
    print(k, v)




