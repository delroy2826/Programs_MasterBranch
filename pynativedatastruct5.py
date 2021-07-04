#Given a two list of equal size create a set such that it shows the element from both lists in the pair
firstList = [1, 2, 3, 4, 5]
secondList = [10, 20, 30, 40, 50]
new_list = []
for i in range(len(firstList)):
    new_list.append((firstList[i],secondList[i]))
print(new_list)