'''
Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
Sample Testcase :
INPUT
5 5
OUTPUT
yes
'''
import math

Ni,Mi = input().split()
N,M = int(Ni),int(Mi)
product = N*M

sqroot = math.sqrt(product)
sqrootint = math.floor(sqroot)

if sqrootint == M and sqrootint == N:
    print('yes')
else:
    print('no')
