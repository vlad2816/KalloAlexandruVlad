numar = int(input('Adauga un numar:'))

if numar < 100 or numar > 999:
    print('erroare')
elif numar % 10 >=5:
    print(numar + numar % 10)
else:
    print(numar - numar % 10)



