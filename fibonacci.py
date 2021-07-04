n = 5
b=0
c=1
count=0
if n <= 0 :
    print("Enter the number greater than zero")
elif n==1:
    print("Fibonacci series of",n,"is 0")
else:
    while count<n:
        print(b,end=' ')
        d= b+c
        b,c=c,d
        count+=1
print()
a=0
b=1
list1=[]
if n<=0:
    print("Enter the number greater than 0")
elif n==1:
    print("Fibonacci Series of",n,"is 0")
else:
    for i in range(n):
        list1.append(a)
        d=a+b
        a=b
        b=d
print(list1)


#2
n=9
l=[]
for i in range(n):
    if i>1:
        l.append(l[i-2]+l[i-1])
    else:
        l.append(i)
print(n in l)