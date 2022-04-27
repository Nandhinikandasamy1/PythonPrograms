'''
Write a program to generate below pattern:
Input:
3 5
Output:
* * * * *
* * * * *
* * * * *
'''
input_values = input("Input value for Number of rows and number of columns separated by space.eg., 3 5: ")
sR, sC = input_values.split()
R,C = int(sR), int(sC)
for i in range(R):
    print(str("* "*C).rstrip(" "))