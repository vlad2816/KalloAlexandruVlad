
mystring = ('hello it school')
def doubleChar(mystring):


    result=''
    for char in mystring:
        result += char*2
    return result 

x = doubleChar(mystring)
print(x)

