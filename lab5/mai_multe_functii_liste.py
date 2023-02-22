
words = ['python', 'is', 'very', 'easy', 'with', 'Mihai', 'Dinu']

temp = [33, 2, 22, 34, 21 , 22, 21]

print(temp)
temp.remove(22)
print(temp)

# Acum stergem toate valorile 22 din lista
# Pentru a verifica daca to remove este in lista verificam cu print(to_remove in temp)

to_remove = 22
print(to_remove in temp)
print(to_remove, 'Apare de :', temp.count(to_remove))

while to_remove in temp:
    temp.remove(to_remove)
print(temp)


if 21 in temp:
    print('S-a produs inghet')
    if temp.count(21) > 1:
        print('S-a produs inghet mai mare.')


temp.reverse()
print(temp)

print('Temp max', max(temp))
print('Temp min', min(temp))
print(len(temp))


