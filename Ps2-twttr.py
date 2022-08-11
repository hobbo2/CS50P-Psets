n = input('Input: ')
vowels = ['a','i','o','u','e','A','E','I','O','U']

print('Output: ' , end="")

for letter in n:
    if letter in vowels:
        print("",end="")
    else:
        print(letter, end="")
