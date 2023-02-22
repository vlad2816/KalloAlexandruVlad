
user_ids = [ 12, 24, 42, 32, 64]


for i in range(len(user_ids)):
    print('Index:',i, "valoare", user_ids[i])
print('')
print('2 metode diferite')
print('')
for i in enumerate(user_ids):
    print('Index:',i[0], "valoare", i[1])