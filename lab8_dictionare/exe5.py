
nume_varsta = {
    'Vlad': 24,
    'Marius': 23,
    'Cristi': 18
}

for x, y in nume_varsta.items():
    print(x, y)

print('-' * 25)
# exercitiu2: dict nume + lista note (calc media afisez medie si nume )

nume_note = {
    'Vlad': [7, 8, 9],
    'Marius': [5, 6, 4],
    'Cristi': [1, 2 ,8]
}

for k, v in nume_note.items(): #trecem prin lista luam doar numerele (lista) adaugam media ca variabila si declaram formula
    media = sum(v)/len(v)
    print(k, media)     





