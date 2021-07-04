#Happy Kite Flying Festival!!!
#Create A program Which Should Give Design of Kite as An OutputDevice
#Program should only contain for loops and no one should Directly
#print any part of kite
#Write a program to design kite and this challenge will only look bestdesigns
#made not for code
n=6
for i in range(1,n):
    print(" "*(n-i)+" *"*i)
for i in range(2,n):
    print(" "*i+" *"*(n-i))
for i in range(1,n):
    for j in range(1,n):
        if n%j==i or (j==5 and i==3):
            print("   *",end='')
        else:
            print(end=' ')
    print()