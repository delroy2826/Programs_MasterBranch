list1 = [5,7,100,20,40,70,60,30,61]
print(list1)
list2 = []
list1.sort()
print(list1)
for i in range(len(list1)):
    if i < len(list1)-1:
        list2.append(list1[i+1] - list1[i])
print(list2)
print("The minimum difference of two elements:",min(list2))
'''
list1 = [5,7,100,20,40,70,60,30,61]
my_dict = dict()
for i in list1:
    l=[]
    for j in list1:
        if i!=j:
            if i<j:
                l.append(j-i)
            else:
                l.append(i-j)
    my_dict[i] = my_dict.get(i,[])+l

a= 0
l2 = []
for i in my_dict:
    print(i,my_dict[i])
    l2.append(min(my_dict[i]))
print(min(l2))
print(l2)'''