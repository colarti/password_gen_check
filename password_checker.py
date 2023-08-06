import string
from enum import Enum

MIN_LENGTH = 4

class ERROR(Enum):
    SUCCESS = 0
    ERROR_MIN_LENGTH = 1
    ERROR_MIN_LENGTH_AT_LEAST_4 = 2
    ERROR_LESS_CAP_LETTERS = 3
    ERROR_LESS_LOWER_LETTERS = 4
    ERROR_LESS_NUMBERS = 5
    ERROR_LESS_SPECIAL = 6



def password_checker(pw, cnt_cap, cnt_lower, cnt_num, cnt_special, cnt_len):
    result = True
    password = pw
    num_of_cap_letters = cnt_cap
    num_of_lower_letters = cnt_lower
    num_of_numbers = cnt_num
    num_of_special_char = cnt_special
    min_length = cnt_len
    error = ERROR.SUCCESS

    sum_cap, sum_lower, sum_num, sum_special = 0,0,0,0

    for char in password:
        sum_cap += 1 if char in string.ascii_uppercase else 0
        sum_lower += 1 if char in string.ascii_lowercase else 0
        sum_num += 1 if char in string.digits else 0
        sum_special += 1 if char in string.punctuation else 0

    if len(password) < min_length and min_length != 0:
        result = False
        error = ERROR.ERROR_MIN_LENGTH
    if len(password) < MIN_LENGTH and min_length == 0:
        result = False 
        error = ERROR.ERROR_MIN_LENGTH_AT_LEAST_4
    if sum_cap < num_of_cap_letters and num_of_cap_letters != 0:
        result = False
        error = ERROR.ERROR_LESS_CAP_LETTERS
    if sum_lower < num_of_lower_letters and num_of_lower_letters != 0:
        result = False
        error = ERROR.ERROR_LESS_LOWER_LETTERS
    if sum_num < num_of_numbers and num_of_numbers != 0:
        result = False
        error = ERROR.ERROR_LESS_NUMBERS
    if sum_special < num_of_special_char and num_of_special_char != 0:
        result = False
        error = ERROR.ERROR_LESS_SPECIAL

    print(f'sum_cap: {sum_cap}\nsum_lower: {sum_lower}\nsum_num: {sum_num}\nsum_special: {sum_special}\nlength: {min_length}')
    
    return result, error



if __name__ == '__main__':
    # pw = 'H*ll$W#rld1'
    pw = '$Tk'
    pw_check = password_checker(pw, 1, 1, 1, 1, 0)
    print(f'pw check: {pw}  > {pw_check[0]}, {pw_check[1]}')