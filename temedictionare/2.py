#2. Creați un dicționar cu numele și notele a trei studenți.
#Calculați media notelor și afișați-o alaturi de numele studentului.

student = {
    'Vlad': [7, 5, 3],
    'Marius': [9, 10, 11],
    'Cristi': [5, 7, 8]
}

for k,v in student.items():
   print(k, sum(v) / len(v))

