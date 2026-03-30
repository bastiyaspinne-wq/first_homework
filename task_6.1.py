import string
user_input = input('')
start_char, end_char = user_input.split('-')
letters = string.ascii_letters
start_index = letters.find(start_char)
end_index = letters.find(end_char)
print(letters[start_index:end_index + 1])
