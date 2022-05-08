'''You are given an array of ids of prisoners. The jail authority found that there are some prisoners of same id. 
Your task is to help the authority in finding the common ids.'''

N=int(input())
list1 = input()
number_list = list1.split()
remove_dup = []
dup=[]
for i in number_list:
    if i not in remove_dup:
        remove_dup.append(i)
    else:
        dup.append(i)
if dup:
    print(*dup,sep=' ')
else:
    print('There is no duplicates')
