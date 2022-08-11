word = str(input('Enter camel case here:\n'))


print('snake-case: ', end="")
for letter in word:
    if letter.isupper():
        print('_'+letter.lower(), end="")
    else:
        print(letter, end="")
