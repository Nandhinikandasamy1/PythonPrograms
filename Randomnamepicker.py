#This program will pick random name from the list of names who should pay the bill.(without using choice() function)
names=input("Type all names seperated by comma(,) : ")

#Importing random module
import random

#Spliting all the names and making list
all_names = names.split(",")

#Using length function to find the length of list
length_of_list = len(all_names)
#pick one random number to get the name
pick_name = random.randint(1, (length_of_list-1))
#Printing the random name who has to pay the bill
print(all_names[pick_name])
