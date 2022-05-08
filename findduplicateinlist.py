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
