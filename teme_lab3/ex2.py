
raza = int(input('Adauga un numar care reprezinta raza unui cerc: '))

perimetrul = 2 * 3.14 * raza

print('perimetrul este:', perimetrul)

aria = 3.14 * (raza**2)

if perimetrul > 100:
   print('aria totala este', aria)
else:
    print('Nu o depasit valoarea 100')
