#Given an input string, count occurrences of all characters within a string
#count("pynativepynvepynative") = {'p': 3, 'y': 3, 'n': 3, 'a': 2, 't': 2, 'i': 2, 'v': 3, 'e': 3}
def count(str1):
    for i in list(set(str1)):
        if i in str1:
            print(i,":",str1.count(i),end=' ,')
    print()
str1 = "pynativepynvepynative"
count(str1)

from collections import Counter
str1 = "pynativepynvepynative"
print(Counter(str1))

str1 = "pynativepynvepynative"
CountDict = dict()
for i in str1:
    count = str1.count(i)
    CountDict[i]=count
print(CountDict)

s1="pynativepynvepynative"
my_dict=dict()
for i in s1:
    my_dict[i]=my_dict.get(i,0)+1
print(my_dict)