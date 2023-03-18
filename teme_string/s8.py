# Using commit variable, print short-version commit number (11 chars) alongside username
#     EX: tester b84fc4703e7

commit = """commit 30c06bce50eeb7a8856e18df2dc64e76fec14cc9
Author: Dinu Mihai <mihai.dinu93@gmail.com>
Date:   Thu Jun 9 18:18:02 2022 +0300

    shuffle method"""

lines = commit.split('\n')
new_line = lines[0].split(' ')[1]
a1 = lines[1].find(':')
a2 = lines[1].find('<')

print(lines[1][a1:a2].lstrip(': '), new_line[0:11])
