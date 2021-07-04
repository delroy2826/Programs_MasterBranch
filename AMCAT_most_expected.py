#An Armstrong number of three digits is an integer such that the sum of the
#cubes of its digits is equal to the number itself.
#For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371

#Write a program to check given number is Armstrong number or not(AMCAT -12 times)
n = 407
nstrlen= len(str(n))
count=0
for i in str(n):
    count+=int(i)**nstrlen
if count == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

#Write a program to find all Armstrong number in the range of 0 and 999.
for num in range(0,1000):
    count=0
    nlen = len(str(num))
    for i in str(num):
        count+=int(i)**nlen
    if count==num:
        print(num)

#Write a program to check given number is strong number or not
#Strong number is a special number whose sum of factorial of digits is equal to the original number.
#For example: 145 is strong number. Since, 1! + 4! + 5! = 145
n = 40585
nl = list(str(n))
#print(nl)
new_l=[]
for i in nl:
    count=1
    l = []
    for j in range(int(i)-1,-1,-1):
        #print(j)
        #new_l.append(int(i))
        l.append(int(i))
    #print(len(l),l)
    for val in range(len(l),0,-1):
        count*=val
    new_l.append(count)
#print(new_l)
if sum(new_l)==n:
    print("Strong Number")
else:
    print("Not a Strong Number")
#Example 1a
for a in range(100000):
    n = a
    count = 0
    for i in str(n):
        val = 1
        for j in range(int(i),0,-1):
            val*=j
        count+=val
    if count==a:
        print(a)
#Example 2
n = 40585
nstr = str(n)
nlist = []
for i in nstr:
    cal=1
    for j in range(int(i),0,-1):
        cal*=j
    nlist.append(cal)
if sum(nlist)==n:
    print("Strong Number")
else:
    print("Not Strong Number")

#Write a program to print all the strong numbers from 1 to 200
for i in range(1,200):
    nstr= str(i)
    l=[]
    for j in nstr:
        cal=1
        for val in range(int(j),0,-1):
            cal*=int(val)
        l.append(cal)
    if sum(l)==i:
        print(i)

#Write a program to print factorial of given number
n=5
factorial = 1
for i in range(n,0,-1):
    factorial*=i
print(factorial)

#Write a program to print factorial of given number in the given list
l = [5,2,7]
for i in l:
    factorial = 1
    for j in range(i,0,-1):
        factorial*=j
    print("The Factorial of {} is {}".format(i,factorial))
#Example 2
def fact(n):
    val = 1
    for i in range(n,0,-1):
        val*=i
    return val

l = [5,2,7]
for i in range(len(l)):
    print(fact(l[i]))

#Write a program to print Fibonacci series of given range(AMCAT -47 times , Cocubes -11)
l = [0,1]
n = int(input("Enter the Number:"))
for i in range(n):
    l.append((l[i]+l[i+1]))
print(l)
print(l[-2])
#Example
l = []
for i in range(10+1):
    if i>1:
        l.append(l[i-2]+l[i-1])
    else:
        l.append(i)
print(l)
#Write a program to find out power of a number
n1 = 5
n2 = 2
print(n2**n1)

#Write a program to find out largest element of an array (AMCAT -7 times , Cocubes -3)
l = [23,34,12,33,45,56,35,26,13]
lenl = len(l)
count = 0
#print(max(l))
l.sort()
for i in range(len(l)+1,0,-1):
    try:
        if l[count+1]>l[count]:
            l.pop(count)
            lenl=len(l)
    except:
        #print("Completed")
        break
print(l[0])

#Sort the the list
l = ['1','4','2','3','5']
l=[int(x) for x in l]
l.sort()
print(l)