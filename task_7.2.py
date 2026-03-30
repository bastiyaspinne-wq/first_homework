def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text
assert correct_sentence('greetings, friends') == 'Greetings, friends.', 'Test1'
assert correct_sentence('Greetings, friends') == 'Greetings, friends.', 'Test2'
assert correct_sentence('Greetings, friends') == 'Greetings, friends.', 'Test3'
assert correct_sentence('hi') == 'Hi.', 'Test4'
assert correct_sentence('welcome.') == 'Welcome.', 'Test5'
print('OK')
