import string
from enum import Enum


class PasswordChecker:
    MIN_LENGTH = 4

    class STATUS(Enum):
        SUCCESS = 0
        ERROR_MIN_LENGTH = 1
        ERROR_MIN_LENGTH_AT_LEAST4 = 2
        ERROR_LESS_CAP_LETTERS = 3
        ERROR_LESS_LOW_LETTERS = 4
        ERROR_LESS_NUMBERS = 5
        ERROR_LESS_SPECIAL = 6

    def __init__(self, pw, num_cap, num_lower, num_num, num_special, num_length):
        self.password = pw
        self.min_cap_letters = num_cap
        self.min_low_letters = num_lower
        self.min_numbers = num_num
        self.min_special = num_special
        self.min_length = num_length

        self.status = PasswordChecker.STATUS.SUCCESS
        self.result = self.check_password()

    def __str__(self):
        result = f'\t     password: {self.password}\n \
            min_length: {self.min_length} / actual: {len(self.password)}\n \
            min_cap: {self.min_cap_letters} / actual: {self.num_cap_letters}\n \
            min_low: {self.min_low_letters} / actual: {self.num_low_letters}\n \
            min_numbers: {self.min_numbers} / actual: {self.num_numbers}\n \
            min_special: {self.min_special} / actual: {self.num_specials}\n \
            result: {self.result} >> {self.status}'
        return result

    def check_password(self) -> bool:
        result = True

        self.num_cap_letters = 0
        self.num_low_letters = 0
        self.num_numbers = 0
        self.num_specials = 0

        for char in self.password:
            self.num_cap_letters += 1 if char in string.ascii_uppercase else 0
            self.num_low_letters += 1 if char in string.ascii_lowercase else 0
            self.num_numbers += 1 if char in string.digits else 0
            self.num_specials += 1 if char in string.punctuation else 0


        if len(self.password) < self.min_length and self.min_length != 0:
            self.status = PasswordChecker.STATUS.ERROR_MIN_LENGTH
            result = False
        if len(self.password) < PasswordChecker.MIN_LENGTH and self.min_length == 0:
            self.status = PasswordChecker.STATUS.ERROR_MIN_LENGTH_AT_LEAST4
            result = False
        if self.num_cap_letters < self.min_cap_letters and self.min_cap_letters != 0:
            self.status = PasswordChecker.STATUS.ERROR_LESS_CAP_LETTERS
            result = False
        if self.num_low_letters < self.min_low_letters and self.min_low_letters != 0:
            self.status = PasswordChecker.STATUS.ERROR_LESS_LOW_LETTERS
            result = False
        if self.num_numbers < self.min_numbers and self.min_numbers != 0:
            self.status = PasswordChecker.STATUS.ERROR_LESS_NUMBERS
            result = False
        if self.num_specials < self.min_special and self.min_special != 0:
            self.status = PasswordChecker.STATUS.ERROR_LESS_SPECIAL
            result = False

        return result

    def get(self) -> bool:
        return self.result

    def get_status(self):
        return self.status
    

if __name__ == '__main__':
    pw = PasswordChecker('HelloW0rlD', 3, 1, 1, 0, 10)
    print(f'pw: {pw}')
    print(f'result: {pw.get()}')