#1)
#AMCAT QUESTON 1223 = 112233
n = str("Vishhal")
new_str=''
for i in range(len(list(n))):
    if n.count(n[i])<2:
        new_str+=n[i]*2
    else:
        new_str+=n[i]
print("1",new_str)

#2
#Reversing the string
str1 = "Delroy"
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end='')
    pass
#print()

#2
str1 = "Delroy"[::-1]
#print(str1)

#3
#Programs to count frequency of occurrence of digits in a array
n= 11203458760011
strn= str(n)
for i in range(10):
    #print("Frequency of {} = {}".format(i,strn.count(str(i))))
    pass

n= 11203458760011
strn=str(n)
for i in set(strn):
    print("{} is {}".format(i,strn.count(i)))
    pass

#4
#A number is called SPY number If the sum and product of its digits  are equal
#For Example 1+2+3 = (1*2*3)
n = "123"
sum = 0
product = 1
for i in n:
    sum+=int(i)
    product*=int(i)
if sum == product:
    #print("Spy Number:Becasue {} == {}".format(sum,product))
    pass
else:
    #print("Not Spy Number:Becasue {} != {}".format(sum,product))
    pass

#5)
#Dictionary Sorted data according to category
my_info_dict = {'Delroy':'Name','Oliveira':'Surname','Sai':'Name','Gokul':'Name','Malon':'Name','Pai':'Surname'}

my_info = dict()
for values,cat in my_info_dict.items():
    my_info[cat]=my_info.get(cat,[])+[values]
#print(my_info)

#6)
#Merging Two Sorted List
a = [1, 5, 7, 12, 13, 19, 21]
b = [3, 4, 6, 10, 11, 18]
c=[]
while a and b:
    if a[0]<b[0]:
        c.append(a.pop(0))
    else:
        c.append(b.pop(0))
print(a)
print(b)
print(c)
print(c+b+a)

#7)
#word frequency
ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time""".split()
for i in list(set(ss)):
    print(i,"=",list(ss).count(i),end=' , ')

ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""

words = ss.split()
d = dict.fromkeys(words,0)
for w in words:
    d[w] += 1
print("sad" ,d)

#8)
weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat']
list1 = [[x,weekdays.count(x)] for x in set(weekdays)]
print(list1)

weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','mon','mon']
my_dict = dict()
for i in weekdays:
    my_dict[i]=my_dict.get(i,0)+1
print(my_dict)

#9
#Question 3: Accept string from the user and display only those characters which are present
#at an even index
def even(str1):
    for i in range(1,len(str1)):
        if i%2==0:
            print(str1[i])
str1 = input("Enter the String: ")
even(str1)


str1 = "abcdefdhi"
for i in range(1,len(str1)):
    if i%2==0:
        print(str1[i])

#10
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

#11
#Given a list slice it into a 3 equal chunks and rever each list
#sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = []
count=0
for i in range(3):
    count+=1
    print("List:",count,l1[:3][::-1])
    l1=l1[3:]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
len_list1=len(list1)
count = 0
for i in range(len_list1//3):
    l=[]
    for j in range(3):
        l.append(list1[count])
        count+=1
    print(l[::-1])

dict_1 = {"List1":['a','b','c'],"value":"Hellow"}
print(dict_1["List1"][1])

str1 = "Hello Vishal"
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end='')

str1 = 12233
c=str(str1)
s=''

for ch in c:
    if c.count(ch)<2:
        s+=ch
print(s)