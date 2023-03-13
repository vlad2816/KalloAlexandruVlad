def pret_cutie(h, latime, lungime, carton):
    pret_brut = h * latime * lungime * 25
    if carton == 2:
        return pret_brut * 1.1
    if carton == 3:
        return pret_brut * 1.2
    return pret_brut


print(f'pret_cutie: {pret_cutie(1, 1, 1 , 2)}')
