import string
from random import choice


class PasswordGenerator:
    _CAPITAL = string.ascii_uppercase
    _LOWER = string.ascii_lowercase
    _NUMBERS = string.digits
    _SPECIAL = string.punctuation

    def __init__(self, cap, lower, number, special, length):
        self.pw = ''
        self.enable_capital_letters = cap
        self.enable_lowercase_letters = lower
        self.enable_numbers = number
        self.enable_special_characters = special
        self.pw_length = length
        self.characters = ''

        self._create_character_list()
    
    def _create_character_list(self):
        if self.enable_capital_letters:
            self.characters += PasswordGenerator._CAPITAL
        if self.enable_lowercase_letters:
            self.characters += PasswordGenerator._LOWER
        if self.enable_numbers:
            self.characters += PasswordGenerator._NUMBERS
        if self.enable_special_characters:
            self.characters += PasswordGenerator._SPECIAL
    
    def create_password(self):
        if len(self.pw) > 0:
            print('\tERR: Password already created, call get()')
            return None
        else:
            for i in range(self.pw_length):
                self.pw += choice(self.characters)
        
            return self.pw
    
    def delete_password(self):
        if len(self.pw) == 0:
            print(f'\tERR: Password is already deleted, create_password')
        else:
            self.pw = ''

    def roll_new_password(self):
        self.pw = ''
        for i in range(self.pw_length):
            self.pw += choice(self.characters)
        
        return self.pw

    def change_pw_settings(self, caps, lower, number, special, length):
        self.enable_capital_letters = caps
        self.enable_lowercase_letters = lower
        self.enable_numbers = number
        self.enable_special_characters = special
        self.pw_length = length

    def get(self):
        if len(self.pw) == 0:
            print('\tERR: No password created')
        else:
            return self.pw


if __name__ == '__main__':
    pw = PasswordGenerator(True, True, True, True, 8)

    print(f'Password Generator >> {pw.create_password()}')

    print(f'Password Generator >> {pw.create_password()}')

    print(f'Password Get >> {pw.get()}')

    print(f'Deleting Password: {pw.delete_password()}')

    print(f'Try Deleting Again: {pw.delete_password()}')

    print(f'Roll New Password: {pw.roll_new_password()}')
