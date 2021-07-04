#Trick 1
'''
import os
#print(os.listdir())
python = 0
with open('data.csv') as csv_file:
    csv_reader = iter(csv_file)
    for i in csv_file:
        a = next(csv_reader)
        #print(a)
        if 'python' in a.lower():
            python+=1
print(python)
'''

#Trick 2
'''
from collections import Counter
l = ['Python','Java','Python']
c = Counter(l)
print(c)
l = ['Python','Java','SQL']

c.update(l)
print(c)
''' #Counter({'Python': 2, 'Java': 1})
            #Counter({'Python': 3, 'Java': 2, 'SQL': 1})

#Tricks 3
'''
import csv
from collections import Counter
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))
axis = language_counter.most_common(5)
xlang =[]
yNum = []
for i in axis:
    xlang.append(i[0])
    yNum.append(i[1])
print(xlang)
print(yNum)
'''

#Tricks 4
#The enumerate() function adds a counter to an iterable object.
'''
l = ['a','b','c','d']
subject = enumerate(l)
for i,j in subject:
    print(i,j)
'''

#Trciks 5
'''
sets = set()
l = ['a','b','c','d','e','a','b','c']
for i in l:
    sets.add(i)
print(list(sets))
'''

#Tricks 6
#The following example demonstrates how a function can examine its arguments.
#And do different things depending on their types.
'''
def checkIt(x):
    if type(x)==type(1):
        print("You've entered a Interger")
    else:
        print("You've entered a String")

checkIt(9)
checkIt('9')
'''
#Tricks 7
#Ternary Operation
'''
count = 3
number = count if count%2 else count -1 # if count%2 ==1 then it goes to if block, or it goes to to else block
print(number)               # because 3%2==1 , 1 means True ,if 2%2==0 , 0 is False
'''
#Tricks 8
'''
class Employee():
    def __init__(self,role,salary):
        self.role=role
        self.salary=salary
    def is_contract_emp(self):
        return self.salary <= 1250
    def is_regular_emp(self):
        return self.salary > 1250

emp=Employee('Tester', 2000)

if emp.is_contract_emp():
    print('Contract')
elif emp.is_regular_emp():
    print('Regular')
print('Thank You')
'''
#Tricks 9
#In-place swapping of two numbers.
'''
x, y = 10, 20
print(x,y)
x,y = y,x
print(x,y)'''

#Trick 9
#Chaining of comparison operators
'''
n = 10
result = 1 < n < 20
print(result)
# True
result = 1 > n <= 9
print(result)
# False'''

#Tricks 10
#Storing elements of a list into new variables.
'''
l1 = [1,2,3]
x,y,z = l1
print(x)
print(y)
print(z)'''

#Tricks 11
#List,set,dict comprehension
'''
l = [x for x in range(10)]
print(l)
set1 = {x for x in range(10)}
print(set1)
dict1 = {x : x for x in range(10)}
print(dict1)'''

#Tricks 12
#We can inspect objects in Python by calling the dir() method. Here is a simple example.
'''
l = {'a':1,'b':2}
print(dir(l))
'''

#Tricks 13
#Combining multiple strings.
'''
l = ['I','Like','Python','Automation']
print(" ".join(l))'''

#Tricks 14
#reversing a string or list
'''
str1 = 'Delroy Oliveira'
for a in reversed(str1):
    print(a,end='')'''

'''
list1 = [1,2,3,4]
for a in reversed(list1):
    print(a)'''

'''
str1 = 'Delroy Oliveira'[::-1]
print(str1)'''

#Tricks 15
#We can use the following approach to create enum definitions.
'''
class Alphabets():
    a,b,c,d=range(4)
print(Alphabets.a)
print(Alphabets.b)
print(Alphabets.c)
print(Alphabets.d)'''

#Tricks 16
#Return Multiple value froma function
'''
def x():
    return 1,2,3,4,5
a,b,c,d,e=x()
print(a,b,c,d,e)
'''
#Trciks 17
#The splat operator offers an artistic way to unpack arguments lists
'''
def value(FirstName,LastName,Place):
    print(FirstName, LastName, Place)
testDict = {'FirstName': 'Delroy','LastName':'Oliveira','Place':'Mangalore'}
value(*testDict)
value(**testDict)'''
'''
def value(FirstName,LastName,Place):
    print(FirstName, LastName, Place)
l = ['Delroy','Oliveira','Mangalore']
value(*l)'''

#Trciks 18
#Use a dictionary to store a switch.
'''
calculation = {'sum':lambda x,y:x+y ,'subtraction':lambda x,y:x-y}
print(calculation['sum'](5,4))
print(calculation['subtraction'](5,3))
'''

#Tricks 19
#Find the most frequent value in a list.
'''
test = ['a','b','c','b']
print(max(set(test),key=test.count))'''

#Tricks 20
#Reset recursion limit.
'''
import sys

x=1001
print(sys.getrecursionlimit())

sys.setrecursionlimit(x)
print(sys.getrecursionlimit())

#1-> 1000
#2-> 1001'''

#Tricks 21
#Check the memory usage of an object.
'''
import sys
x=1
print(sys.getsizeof(x))'''

#Tricks 22
#Create a dictionary from two related sequences.
'''
t1 = (1, 2, 3)
t2 = (10, 20, 30)

print(dict (zip(t1,t2)))'''

#Tricks 23
#In line search for multiple prefixes in a string.
'''
str1 = 'Delroy Oliveira'
print(str1.startswith(('el','Del'))) #If two or more parameter are used in startswith then enclose it with two paranthesis
print(str1.endswith(('ira','del')))'''