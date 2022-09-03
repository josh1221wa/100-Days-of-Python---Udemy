#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easypassword = ''
for i in range(nr_letters):
    easypassword += random.choice(letters)
for i in range(nr_symbols):
    easypassword += random.choice(symbols)
for i in range(nr_numbers):
    easypassword += random.choice(numbers)

print("Easy password is " + easypassword)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hardpass_list = []
for i in range(nr_letters):
    hardpass_list.insert(random.randint(0, nr_letters+nr_numbers+nr_symbols-1), random.choice(letters))
for i in range(nr_symbols):
    hardpass_list.insert(random.randint(0, nr_letters+nr_numbers+nr_symbols-1), random.choice(symbols))
for i in range(nr_numbers):
    hardpass_list.insert(random.randint(0, nr_letters+nr_numbers+nr_symbols-1), random.choice(numbers))

hardpassword = ''.join(hardpass_list)
print("Hard password is " + hardpassword)