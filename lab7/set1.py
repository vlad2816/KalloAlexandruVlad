colors = {'red', 'brown', 'blue', 'white'}

# print(colors)
# print(type(colors))

# Pentru set gol set() nu colors = {} (asta este dictionar nu set)

for i in colors:
    print(i)

colors.add('black')
print(colors)
colors.remove('white')
print(colors)


