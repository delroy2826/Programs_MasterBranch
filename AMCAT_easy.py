#Write a program to generate multiplication table
n=10
for i in range(1,10+1):
    print("{} * {} = {}".format(n,i,n*i))

#Write a program to swap two integers
n1 = 10
n2 = 20
print(n1,n2)
temp = n1
n1 = n2
n2 = temp
print(n1,n2)

#Write a program to swap two numbers without using third variable(AMCAT -7 times , Cocubes -11)
n1 = 10
n2 = 20
print(n1,n2)
n1,n2=n2,n1
print(n1,n2)

#Write a program to split number into digits
num = 12334
for i in str(num):
    print(int(i))

#Write a program to count number of digits in a number
num = 12334
print(len(str(num)))

#Write a program to find out sum of digits of given number(AMCAT -2 times , Cocubes -4)
num = 12334
sum = 0
for i in str(num):
    sum+=int(i)
print(sum)
