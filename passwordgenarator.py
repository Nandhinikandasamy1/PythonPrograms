'''Write program to generate password based on user input.
if user select 2 letters, 2 number, 2 symbols - password should be constructed with 2 letters, 2 numbers, 2 symbols.
Write program in Easy and Hard method. In Easy method print password without randomization. In Hard method print password with Randomization '''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=""

for i in range (1,(nr_letters+1)):
  random_val=random.choice(letters)
  password+=random_val
for i in range (1,(nr_numbers+1)):
  random_val=random.choice(numbers)
  password+=random_val
for i in range (1,(nr_symbols+1)):
  random_val=random.choice(symbols)
  password+=random_val
print(f"Your password is: {password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password=[]

for i in range (1,(nr_letters+1)):
  random_val=random.choice(letters)
  password.append(random_val)
for i in range (1,(nr_numbers+1)):
  random_val=random.choice(numbers)
  password+=random_val
for i in range (1,(nr_symbols+1)):
  random_val=random.choice(symbols)
  password+=random_val
print(password)
random.shuffle(password)
print(password)
new_password=""
for i in password:
  new_password+=i
print(print(f"Your password is: {new_password}"))