num = int(input('Adauga un numar: '))

n1 = 0
n2 = 1
sum = 0

if num <= 0:
    print('Adauga un numar mai mare ca 0')

else:
    for i in range(0, num):
        n1 = n2
        n2 = sum
        sum = n1 + n2
        print(sum *('*'))

