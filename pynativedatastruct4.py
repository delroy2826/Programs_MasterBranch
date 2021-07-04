#Question 4: Given a list iterate it and count the occurrence of each
#element and create a dictionary to show the count of each element
#list = [10, 20, 30, 10, 20, 40, 50] output dict = {10: 2, 20: 2, 30: 1, 40: 1, 50: 1}
l = [10, 20, 30, 10, 20, 40, 50]
CountDict = dict()
for i in l:
    count = l.count(i)
    CountDict[i]=count
print(CountDict)

from collections import Counter
l = [10, 20, 30, 10, 20, 40, 50]
print(Counter(l))

dict_1 = {"abc":"[1,2,3,4]","value":"abc"}
print(list(dict_1))
