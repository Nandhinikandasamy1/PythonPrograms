'''Find factorial for the given number N'''
N = int(input())
value = 1
for i in range (1, N+1):
    value *= i
print(value)
