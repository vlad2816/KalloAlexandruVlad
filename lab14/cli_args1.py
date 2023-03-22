import sys
print(sys.version_info.major)

print('Hello')

try:
    print(sys.argv[1] * int(sys.argv[2]))  # noul input
except IndexError:
    print('argumentul nu exista')
    sys.exit(1)
except ValueError:
    print('Argument incorect')
    sys.exit(1)

# sys.exit()
print('It school')
# user_input = input('Write a string here: ')

# print(user_input[::-1])
