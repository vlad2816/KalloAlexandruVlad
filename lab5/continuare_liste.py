user_ids = [324, 345, 536, 64, 4, 345]

# user_ids.insert(1, 44)
print(user_ids)

print(user_ids.index(324))
print(user_ids.index(345, 3)) 

# Toate aparitiile lui 345 

user_ids.insert(user_ids.index(345) +1, 44)
print(user_ids)
index = -1

for i in range(user_ids.count(345)):
    index = user_ids.index(345, index + 1 )
    user_ids.insert(index, + 1,  44)

print(user_ids)
