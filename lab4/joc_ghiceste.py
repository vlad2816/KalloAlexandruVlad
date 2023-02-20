from random import randint

print('Incepe jocul ')

pc = randint(1, 99)

numar = int(input('Alege un numar intre 1 si 99: '))

while numar != pc:
    if numar < pc:
        print('Alege un numar mai mare')
    else: 
        print('Alege un numar mai mic ')
    numar = int(input('introduceti un numar intre 1 si 99: '))

print('ai terminat jocul ')


    
