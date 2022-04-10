#Python program to generate Head or Tails

#importing predefined function random
import random

#Giving two numbers to generate random value and assigning it to one variable
random_value = random.randint(0, 1)

#Using if condition generating Head or Tail option
if random_value == 1:
    print('Heads')
else:
    print('Tails')
