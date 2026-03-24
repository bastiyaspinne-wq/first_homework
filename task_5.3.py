import string
user_input = input('put u text here:')
hashtag = user_input.title()
print(hashtag)
forbidden = string.punctuation + ' '
for char in forbidden:
    hashtag = hashtag.replace(char, '')
    hashtag = '#' + hashtag
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
print(hashtag)
