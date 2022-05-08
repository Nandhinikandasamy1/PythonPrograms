'''You are given with a queue. Your task is to reverse the queue elements and print it.


Input Description:
You are given a number ‘n’,denoting size of queue, Next line contains s space separated numbers

Output Description:
Print the reversed queue.

Sample Input :
6
1 2 3 4 5 6
Sample Output :
6 5 4 3 2 1'''

n=input()
val= input() #Getting input
value = val.split()
e=""
for i in value:
    e = i+" "+e
print (e.rstrip(" "))
