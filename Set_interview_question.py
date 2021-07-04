#1)
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
for i in range(2000,3200+1):
    if i%7==0 and i%5!=0:
        print(i,end=',')

#2)
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320
n1 = 8
count=1
for i in range(8,0,-1):
    count*=i
print(count)

#3)
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
#such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
n = 8
values = {x:x**2 for x in range(1,n+1)}
print(values)

#4)
#Write a program which accepts a sequence of comma-separated numbers
#from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')
l = input().split(',')
t = tuple(input().split(','))
print(l)
print(t)
'''
l = input().split(',')
print(l)
print(tuple(l)) '''

#5
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class UserInput():
    def getString(self):
        self.s = input("Enter the String:")
    def printString(self):
        print(self.s.upper())
u = UserInput()
u.getString()
u.printString()
'''
class UserInput():
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input("Enter the String:")
    def printString(self):
        print(self.s.upper())
u = UserInput()
u.getString()
u.printString()'''

#6
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24
import math
d = input().split(',')
c = 50
h = 30
for i in d:
    print(round(math.sqrt((2*50*int(i))//h)),end=',')
#7
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
#The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#row,col=int(input("Enter the row: ")),int(input("Enter the Col:"))
row=3
col=5
result = [[x*y for x in range(col)] for y in range(row)]
print(result)

'''
row,col=int(input("Enter the row: ")),int(input("Enter the Col:"))
result = [[x*y for x in range(col)] for y in range(row)]
print(result)'''

#8
#Write a program that accepts a comma separated sequence of words as input
#and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world
str1 = input().split()
str1.sort()
print(",".join(str1))
#9
#Write a program that accepts sequence of lines as input and prints the
#lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT
l = []
while True:
    s=input()
    if s:
        l.append(s.upper())
    else:
        break
a=[print(x) for x in l]

#10
#Write a program that accepts a sequence of whitespace separated words as
#input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world
str1 = set(input().split())
print(*str1)

for i in range(1,100+1):
    if i%15==0:
        print("BuzzFuzz",i)
    elif i%5==0:
        print("Fuzz",i)
    elif i%3==0:
        print("Buzz",i)

l = [99,24,34,23,11,33,66,100]
a=0
for i in l:
    if i>a:
        a=i
print(a)

str1 = "mam"
str2=""
for i in range(len(str1)-1,-1,-1):
    str2+=str1[i]
print(str1==str2)

for i in range(10):
    if i<5:
        print("*",end='')
    else:
        print('.',end='')

l = [1,2,3,4,5,6]
n = int(input("Enter the Number: "))
if n==1:
    val=0
    for i in l:
        if i%2==0:
            val+=i
else:
    val=0
    for i in l:
        if i%2!=0:
            val+=i
print(val)

l = [1,2,3,4,5,6,7,8,9,10]
odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("odd ",odd)
print("even ",even)

str1 = "My iname iis Dlroy Olvera".replace(" ","")
print(str1)
for i in str1[::-1]:
    if str1.count(i)>2:
        print(i)
        break

str1 = "Delroy"
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end='')
print()

str1 = "My Name Is Delroy".split()
for i in str1:
    for j in range(len(i)-1,-1,-1):
        print(i[j],end='')
    print(end=' ')
print()
#Write a function to count the sum of even number when user input is 1 and 2 to count the sum of odd number
def fuction1(l,value):
    if value==1:
        count=0
        for i in l:
            if i%2==0:
                count+=i
        return count
    else:
        count=0
        for i in l:
            if i%2!=0:
                count+=i
        return count
value = int(input())
l=[1,2,3,4,5,6,7,8,9]
print(fuction1(l,value))

#Write a fuction1 to count sum of numbers in an list depending upon the condition
def fuction1(l):
    count=0
    for i in l:
        if i%3==0:
            count+=i*2
        elif i%7==0:
            count+=i*3
        elif i%21==0:
            count+=i*7
    return count
l=[1,2,3,4,5,6,23,12,21,34]
print(fuction1(l))

#write a function to display the last charater repeated 3 times
def function1(str1):
    for i in str1[::-1]:
        if str1.count(i)==3:
            return i
str1 = "bbabbacac"
print(function1(str1))