# Creați un dicționar cu numele și numărul de telefon a trei prieteni.
# Afișați numerele de telefon în ordine alfabetică a numelor


nr_tel = {
    'Vlad': '342589',
    'Crina': '199032',
    'Valentin': '11111111111'
}


x = {k: (sorted(v)) for k, v in nr_tel.items()}
print(x)
