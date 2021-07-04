list1 = [5,100,20,40,70,60,390,400]
print(list1)
list2 = []
list1.sort()
print(list1)
for i in range(len(list1)):
    if i < len(list1)-1:
        list2.append(list1[i+1] - list1[i])
print(list2)
print("The maximum difference of two elements:",max(list2))
'''
list1 = [200,100,20,40,70,60,390,400]

my_dict = dict()
for i in range(len(list1)):
    list2 = []
    for j in list1:
        if list1[i]>j:
            list2.append(list1[i]-j)
        else:
            list2.append(j-list1[i])
    my_dict[list1[i]]=list2
print(my_dict)
max_val = 0
for i in my_dict:
    if max(my_dict[i])>max_val:
        max_val=max(my_dict[i])
print(max_val)'''