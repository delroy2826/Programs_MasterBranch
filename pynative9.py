#Question 9: Reverse a given number and return true if it is the same as the original number
def check(n):
    str1=''
    for i in reversed(str(n)):
        str1+=i
    if str1==str(n):
        print(True)
    else:
        print(False)
n=11211
check(n)

n=11211
n1 = str(n)
n2=""
for i in range(len(n1)-1,-1,-1):
    n2+=n1[i]
print(n2)
if n1==n2:
    print(True)
else:
    print(False)