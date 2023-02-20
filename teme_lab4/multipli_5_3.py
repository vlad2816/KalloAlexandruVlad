n = int(input('Enter number: '))

suma = 0
i = 1

while i < n:
    i+=1
    if i % 3 == 0 and i % 5 == 0:
        suma +=i
print(suma)