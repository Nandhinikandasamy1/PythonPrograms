# Find Average height without using sum() function.
#Cretaing variable to get input from user and split it to make list
student_heights = input("Input a list of student heights ").split()
#Converting all the values to int using for loop
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#creating one variable to store sum of the heights
n = 0
#Adding the heights using for loop
for i in student_heights:
  n = n+i
#Finding average and storing it in one variable
average_of_height = n/(len(student_heights))
#Printing rounded off average valu
print(round(average_of_height))