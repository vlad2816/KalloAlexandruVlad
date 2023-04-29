def calcul_sfera(r):
    return 4/3 * 3.14 * r ** 3


print(calcul_sfera(4))


def persoana(varsta):
    if varsta >= 40:
        return 'Persoana are o varsta inaintata'
    if varsta < 40 and varsta >= 25:
        return 'Persoana este de varsta medie'
    if varsta < 25 and varsta >= 18:
        return 'Persoana este adolescenta'


vlad = persoana(24)
print(vlad)
