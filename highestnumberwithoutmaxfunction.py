# Find maximum score without using max() function
#Cretaing variable to get input from user and split it to make list
student_scores = input("Input a list of student scores ").split()
#Converting all the values to int using for loop
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#Creating empty variable to store Highest score
highest_value=0
#Finding highest value using for loop
for value in student_scores:
  #Asigning value to empty variable using if condition
  if value>highest_value:
    highest_value=value
#Pring the highest score
print(highest_value)