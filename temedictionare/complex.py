# Creați o listă cu patru tuple, fiecare tuplă conținând numele
# și vârsta unui angajat. Convertiți lista într-un dicționar unde
# cheia este numele angajatului și valoarea este vârsta acestuia.

lista = (('Vlad', 23), ('Andrei', 25), ('Cristi', 26))


resultDictionary = dict((x, y) for x, y in lista)
print(resultDictionary)
