matrix = [
    ["Vlad", [4, 5, 6, 7, 10]],
    ["ionel", [4, 5, 7, 7, 8]],
    ["Andrei", [4, 5, 6, 7, 8]],

]

print(matrix[0][1][0]) # Din primul [0] aleg lista nr 1 vlad. [cu 1] aleg lista din vlad aia cu 4,5,6,7, iar cu 
# [0] aleg indexul din lista 1.

for i in matrix:
    print(i[0], "Cea mai mare nota: ", max(i[1]), sum(i[1])/len(i[1]) )

input_list = []
n = int(input("nr elemente:"))

for i in range(n):
    input_list.append(int(input()))

print(input_list)