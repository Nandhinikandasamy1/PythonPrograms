''' Write a program to print below pattern:
input:5
output:
1
22
333
4444
5555
'''
input_number=int(input("Input number to print pattern: "))
for i in range(1,input_number+1):
   print(str(i) *i)