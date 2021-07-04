#Write a program to reverse any number
num = 12334
nstr = str(num)
for i in range(len(nstr)-1,-1,-1):
    print(nstr[i],end='')
print()

#Write a program to check given number is palindrome number or not(AMCAT -46 times , Cocubes -31)
num = 1212
if str(num)==str(num)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Write a program to check given number is prime number or not
n=19
for i in range(2,n):
    if n%i==0:
        print("Not Prime")
        break
else:
    print("Prime")

#Write a program to print all prime numbers up to given number
n = 20
for i in range(1,n):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
    else:
        print(i)
#Write a program to check given number is perfect number or not(AMCAT -7 times )
n = 6
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")