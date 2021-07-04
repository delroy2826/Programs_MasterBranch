def  bin_search(list1):
    mid = len(list1)//2
    if x not in list1:
        return -1
    if list1[mid] < x:
        temp = list1[mid:]
        print(temp)
        return bin_search(temp)
    elif list1[mid] > x:
        temp = list1[:mid]
        print(temp)
        return bin_search(temp)
    elif list1[mid]==x:
        temp = list1[mid]
        print(temp)
    return temp
list1 = [11,12,13,14,15,16,17,18,19,20]
list1.sort()
print(list1)
x = 12
b=bin_search(list1)
if b == -1:
    print("Element {}  Not in the list".format(x))
else:
    print("Element {}, Position is {} in the list".format(x,list1.index(x)))