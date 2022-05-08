'''Using the method of looping, write a program to print the table of 9 till N in the format as follows:
(N is input by the user)

9 18 27...

Print NULL if 0 is input'''

N=int(input())
if N!=0:
  print_value = ""
  for i in range (1,N+1):
    table =str(i*9)
    print_value+=table+" "
  print(print_value.rstrip(' '))
else:
  print('Type positive integer to generate multiples of 9')
