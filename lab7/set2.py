list1 = [22, 34, 56, 65, 45]
list2 = [23, 34, 65, 55]

common = set(list1).intersection(set(list2))
dif = set(list1).difference(set(list2))

print(common)
print(dif)
