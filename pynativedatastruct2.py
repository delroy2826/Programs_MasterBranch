#Question 2: Given an input list removes the element at index 4 and add
#it to the 2nd position and also, at the end of the list
#List = [54, 44, 27, 79, 91, 41] Output : [54, 44, 79, 27, 91, 41, 79].
def rearrange(l1):
    val = l1.pop(4-1)
    l1.insert(2,val)
    l1.append(val)
    return l1

l1 = [54, 44, 27, 79, 91, 41]
print(rearrange(l1))

list1 = [54, 44, 27, 79, 91, 41]
a = list1.pop(4)
list1.insert(2,a)
list1.append(a)
print(list1)