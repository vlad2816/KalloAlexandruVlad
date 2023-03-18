
def zero_one(lst):
    list1 = lst[:]
    list1[0] = 1
    return list1


matrix = [
    [0, 3, 4, 4],
    [2, 34, 24, 43],
]

print(matrix)
m = zero_one(matrix)  # pass by reference
print(matrix)
print(m)
