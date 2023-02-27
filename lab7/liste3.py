# list comprehension
temperaturi = [-2, -3, 91, 71 , 61 , 50 , 12, 32, 41, 40 ,129]

new_list1 = [abs(x) for x in temperaturi if x < 0]

print(new_list1)