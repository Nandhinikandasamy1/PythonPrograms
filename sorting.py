''' Given k sorted arrays of possibly different sizes, merge them and print the sorted output.
Input Size : N<=100 
Example:
INPUT
k = 3
1 3
2 4 6
0 9 10 11
OUTPUT
0 1 2 3 4 6 9 10 11'''

N = int(input())
x =[]
for i in range (N):
    x.extend(input().split())
x = [int(i) for i in x]
x.sort()
print(*x,sep=' ')
