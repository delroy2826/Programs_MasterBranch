list1 = [1,2,3,4,5]
list2 = [1,2,3,5]
for i in list1:
    if i not in list2:
        print(i)
        break