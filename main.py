import numbers
import random
import string

print('hello, Welcome to Password generator!')

PasswordLenght = int(input('\n Password Lenght, please: '))

numbers = string.digits
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbol = string.punctuation

together = symbol + upper + lower + numbers

password1 = random.sample(together, PasswordLenght)

password = "".join(password1)

print(password)
