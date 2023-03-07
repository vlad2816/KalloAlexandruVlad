#Creați un dicționar cu numele și salariul a trei angajați.
#Afișați salariatul cu cel mai mare salariu.


student = {
    'Vlad': 5200,
    'Marius': 8000,
    'Cristi': 3500
}
max = 0
max_name = ""

for k, v in student.items():
    if v > max:
        max = v
        max_name = k
print(max_name)