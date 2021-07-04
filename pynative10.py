#Question 10: Given a two list of ints create a third list such that should
#contain only odd numbers from the first list and even numbers from the second list
def merge_even_odd(listOne,listTwo):
    l=[]
    for i in listOne:
        if i%2!=0:
            l.append(i)
    for i in listTwo:
        if i%2==0:
            l.append(i)
    return l
listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]
print(merge_even_odd(listOne,listTwo))
'''l = [i for i in listOne if i%2!=0]
l2 = [i for i in listTwo if i%2==0]
print(l+l2)'''

listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]
new_list = []
for i in range(len(listOne)):
    if listOne[i]%2!=0:
        new_list.append(listOne[i])
    if listTwo[i]%2==0:
        new_list.append(listTwo[i])
print(new_list)