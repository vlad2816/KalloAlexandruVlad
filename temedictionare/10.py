nume_note = {
    'Vlad': [7, 8, 9],
    'Marius': [5, 6, 4],
    'Cristi': [1, 2, 8]
}

for k, v in nume_note.items():  # trecem prin lista luam doar numerele (lista) adaugam media ca variabila si declaram formula
    media = sum(v)/len(v)
    print(k, media)
