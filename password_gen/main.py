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

    meets_cases = False
    has_number = False
    has_special_character = False

    while not meets_cases or len(password) < user_length:
        i = random.choice(all_characters)
        password += i

        if i in digit:
            has_number = True
        elif i in symbol:
            has_special_character = True

        meets_cases = True
        if num:
            meets_cases = has_number
        if special_char:
            meets_cases = meets_cases and has_special_character
    return password


get_user_length = int(input('Password length: '))
get_user_use_digits = input(
    'Do you want to have digits (y/n)? ').lower() == 'y'
get_user_use_symbols = input(
    'Do you want to have digits (y/n)? ').lower() == 'y'

password = password_gen(
    get_user_length, get_user_use_digits, get_user_use_symbols)
print(f'The password is:  {password}')
