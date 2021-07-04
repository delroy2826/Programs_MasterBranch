#https://pynative.com/python-basic-exercise-for-beginners/
#Question 1: Accept two int values from user and return their product.
#If the product is greater than 1000, then return their sum
def calc(n1,n2):
    if (n1*n2)<1000:
        return n1*n2
    else:
        return n1+n2

n1 = int(input("Enter the Number: "))
n2 = int(input("Enter the Number: "))
print(calc(n1,n2))

n1=int(input("N1:"))
n2=int(input("N2:"))
if n1*n2>1000:
    print(n1+n2)
else:
    print(n1*n2)
