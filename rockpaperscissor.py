import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Creating list to club all the img 
game_img = [rock, paper, scissors]
#Getting input from user
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
#Printing user option
print("You chose:\n"+game_img[user_input])
#Generating random value and saving it in variable as computer input
computer_input = random.randint(0, 2)
#Printing Computers choice
print("Computer chose:\n"+game_img[computer_input])
#Displying result based on if conditions
if user_input > 2 or user_input < 0:
    print("Invalid number")
elif user_input == 0 and computer_input == 2:
    print("You Won")
elif computer_input == 0 and user_input == 2:
    print("You Lose")
elif user_input > computer_input:
    print("You Won")
elif computer_input > user_input:
    print("You Lose")
elif user_input == computer_input:
    print("Match Draw")
