import string
import keyword
print(string.ascii_lowercase)
print(string.ascii_uppercase)
user_input = ('name:')
forbiden = string.punctuation.replace('_', '') + ' '
is_valid = True
if len(user_input) == 0:
    is_valid = False
elif user_input in keyword.kwlist:
    is_valid = False
elif user_input [0].isdigit():
    is_valid = False
elif user_input.count('_')>1:
    is_valid = False
if is_valid:
    for char in user_input:
        if char.isupper():
            is_valid = False
            break
if char in forbiden:
    is_valid = False
print(is_valid)