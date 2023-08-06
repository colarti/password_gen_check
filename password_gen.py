import string
from random import choice

CAPTIAL_LETTERS = string.ascii_uppercase
LOWER_LETTERS = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL_CHAR = string.punctuation


def create_password(caps, lower, num, special, length):
    CHARACTERS = ''
    if caps:
        CHARACTERS += CAPTIAL_LETTERS
    if lower:
        CHARACTERS += LOWER_LETTERS
    if num:
        CHARACTERS += NUMBERS
    if special:
        CHARACTERS += SPECIAL_CHAR

    password = []
    for i in range(length):
        password.append(choice(CHARACTERS))
    
    password = ''.join(password)

    print(f'Password Generator: {password}')


if __name__ == '__main__':
    create_password(True, True, True, True, 16)