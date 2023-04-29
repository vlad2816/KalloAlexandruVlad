def appending_file(name, last_name):
    c = open('Newfile.txt', 'a')
    c.write(name + last_name)
    c.close()


appending_file('Vlad', 'Kallo')
