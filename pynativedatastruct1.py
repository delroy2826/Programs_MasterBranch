#QuestionGiven a two list. Create a third list by picking an odd-index element
#from the first list and even index elements from second.
'''
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28] Output: Expected Outcome: [6, 12, 18, 4, 12, 20, 28]'''
def merge(listOne,listTwo):
    NewList=[]
    for i in range(1,len(listOne),2):
        NewList.append(listOne[i])
    for i in range(0,len(listTwo),2):
        NewList.append(listTwo[i])
    return NewList
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
print(merge(listOne,listTwo))

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree=[]
for i in range(len(listOne)):
    if i%2==0:
        listThree.append(listTwo[i])
    else:
        listThree.append(listOne[i])
print(listThree)