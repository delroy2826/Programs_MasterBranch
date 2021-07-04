#A number is called Perfect Number,If it's equal to the sum of its proper positive divisor
#excluding the number itself For example 1+2+3 = 6
#Write a program to check if the number is a perfect number or not
n = 6
count=0
l = []
for i  in range(1,n):
    if n%i==0:
        l.append(i)
        count+=i
if count==n:
    print(l,'=',n)
    print("Perfect Number")
else:
    print(l,'!=',n)
    print("Not Perfect Number")

#2
n = 6
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("Perfect Number")
else:
    print("Not Perfect")