import tkinter as tk
import random
import string

# The design part
root = tk.Tk()
root.geometry('400x300')
root.title('Password It School')

title = tk.StringVar()
label = tk.Label(root, textvariable=title).pack()
title.set('Password args: ')


def selection():
    selection = choice.get()


# Password choices
choice = tk.IntVar()
R1 = tk.Radiobutton(root, text='Strings', variable=choice,
                    value=1, command=selection).pack(anchor='center')
R2 = tk.Radiobutton(root, text='Str + Num', variable=choice,
                    value=2, command=selection).pack(anchor='center')
R3 = tk.Radiobutton(root, text='Str + Num + Symb', variable=choice,
                    value=3, command=selection).pack(anchor='center')

labelchoice = tk.Label(root)
labelchoice.pack()

lungimelabel = tk.StringVar()
lungimelabel.set('Password length')
lungimetitle = tk.Label(root, textvariable=lungimelabel).pack()

# Password dimension
val = tk.IntVar()
spinlength = tk.Spinbox(root, from_=6, to=24,
                        textvariable=val, width=13).pack()

# The password generator


def callback():

    password_label.config(text=passgen())


passwordButton = tk.Button(root, text='Generate Password',
                           bd=5, height=2, command=callback, pady=3)
passwordButton.pack()
password = str(callback)

password_label = tk.Label(root, text='')
password_label.pack(side='bottom')


# Generating a password
Strings = string.ascii_letters
Str_Num = string.ascii_letters + string.digits
Symbols = string.punctuation
Str_Num_Symbols = Strings + Str_Num + Symbols


def passgen():
    if choice.get() == 1:
        return ''.join(random.sample(Strings, val.get()))
    elif choice.get() == 2:
        return ''.join(random.sample(Str_Num, val.get()))
    elif choice.get() == 3:
        return ''.join(random.sample(Str_Num_Symbols, val.get()))


root.mainloop()
