countries = ('Romania', 'Albania', 'Ungaria')
print(countries)
# print(type(countries))

print(countries[0])

countries_list = list(countries)

print(type(countries_list))

countrie = tuple(countries_list)
print(type(countrie))

for i, j in enumerate(countries):
    print(i, j,  end=' ')
    