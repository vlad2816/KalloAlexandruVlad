import random
import string


def password_gen(user_length, num=True, special_char=True):
    alphabetical_char = string.ascii_letters
    digit = string.digits
    symbol = string.punctuation

    all_characters = alphabetical_char
    if num:
        all_characters += digit
    if special_char:
        all_characters += symbol

    password = ""
    prev_char = None
    while len(password) < user_length:
        i = random.choice(all_characters)
        if prev_char != i:
            prev_char = i
        password += i
    return password


get_user_length = int(input('Password length: '))
get_user_use_digits = input(
    'Do you want to have digits (y/n)? ').lower() == str('y')
get_user_use_symbols = input(
    'Do you want to have symbols (y/n)? ').lower() == str('y')

try:
    password = password_gen(
        get_user_length, get_user_use_digits, get_user_use_symbols)
    print(f'The password is:  {password}')
except ValueError:
    print('Error!!!')
