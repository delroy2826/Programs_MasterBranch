'''Given a list , subtract the last value from first
and put it to first, subtract the second last value from
second and put it to second
Example: [1,4,2,3,8,1,2]
Output: -1 ->3 ->-6 ->3 ->8 ->1 ->2 '''
list1 = [1,4,2,3,8,1,2,8]
list2 = []
len_list1 = len(list1)//2
list3=list1[:len_list1]
for i in range(len(list1)):
    if i < len_list1:
        list2.append(list3[i]-list1[(len(list1)-1)-i])
    else:
        list2.append(list1[i])
print(*(list2) ,sep= ' ->')

'''
list1 = [1,4,2,3,8,1,2];list2 = []
for i in range(len(list1)):
    if i<len(list1)//2:
        list2.append(list1[i]-list1[-i-1])
    else:
        list2.append(list1[i])
print(*(list2),sep=' -> ')'''