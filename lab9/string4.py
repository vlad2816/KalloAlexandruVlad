template = 'Salut <<USER>>! Bine ai venit! <<USER>> nu te-am mai vazut de mult!'

user = input ('Numele tau: ')

greet_msg = template.replace('<<USER>>', user)
print(greet_msg)

