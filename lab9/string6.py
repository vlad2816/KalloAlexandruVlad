files = ['mylog.txt', 'audio1.mp3', 'summer.mov', 'notes.txt']

for i in files:
    if i.endswith('.txt'): #cu ce se termina.
        print(i)

py_text = """Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
To find out more, start with The Python Tutorial. The Beginner's Guide to Python links to other introductory tutorials and resources for learning Python."""

for i in py_text.split():
    if i.startswith('a'): #cu ce incepe.
        print(i)


        

    