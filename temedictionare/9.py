# Creați un dicționar cu numele și vârsta a patru persoane.
# Sortați dicționarul în funcție de vârstă și afișați numele și vârsta
# fiecărei persoane în ordine crescătoare de vârstă


dictt = {
    'Vlad': '24',
    'Crina': '30',
    'Razvan': '20',
    'Elena': '15',
    'Marius': '19'
}


sortare = sorted(dictt.items(), key=lambda x: x[1])
print(sortare)  # foarte important.
