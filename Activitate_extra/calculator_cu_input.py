
print('The game start now!')
print('If you want to finish, write exit ')
print('The math operations are: sum, rest, multi, and div')

result = ''

while True:
    if not result:
        result = input('First number: ')
        if result.lower() == 'exit':
            break
        result = int(result)
    operation = input('Write the math operation here: ')
    if operation.lower() == 'exit':
        break
    nr2 = input('Write here the second number: ')
    if nr2.lower() == 'Exit':
        break
    nr2 = int(nr2)

    if operation.lower() == 'sum':
        result += nr2
    elif operation.lower() == 'rest':
        result -= nr2
    elif operation.lower() == 'multi':
        result *= nr2
    elif operation.lower() == 'div':
        result /= nr2
    else:
        print('Error 404 invalid math operation')
        break

    print(f'The result is:{result} ')