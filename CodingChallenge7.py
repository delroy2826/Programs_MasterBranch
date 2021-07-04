#Create Menu Driven Program which will accept Two
#Matrix of 3*3 (row*column) and perform arithmetic operation depending
#user Input
def Addition(m1,m2,result):
    for i in range(len(m1)):
        for j in range(len(m1)):
            result[i][j]=m1[i][j]+m2[i][j]
    return result
def Subtraction(m1,m2,result):
    for i in range(len(m1)):
        for j in range(len(m1)):
            result[i][j]=m1[i][j]-m2[i][j]
    return result
def Multiplication(m1,m2,result):
    for i in range(len(m1)):
        for j in range(len(m1)):
            result[i][j]=m1[i][j]*m2[i][j]
    return result

print("Matrix Operation")
print("Choose the Operation You want to Perform (3*3) Matrix:\n1)Addition\n2)Subtraction\n3)Multiplication")
a=int(input())
if a==1:
    print("Enter 9 Numbers")
    result=[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    m1=[]
    print("Values for Matrix 1")
    for row in range(3):
        x=[]
        for col in range(3):
            x.append(int(input()))
        m1.append(x)
    print("Matrix 1: ",m1)
    m2=[]
    print("Values for Matrix 2")
    for row in range(3):
        x=[]
        for col in range(3):
            x.append(int(input()))
        m2.append(x)
    print("Matrix 2: ",m2)
    Addition(m1,m2,result)
    print("Result: ",result)
elif a==2:
    print("Enter 9 Numbers")
    result=[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    m1=[]
    print("Values for Matrix 1")
    for row in range(3):
        x=[]
        for col in range(3):
            x.append(int(input()))
        m1.append(x)
    print("Matrix 1: ",m1)
    m2=[]
    print("Values for Matrix 2")
    for row in range(3):
        x=[]
        for col in range(3):
            x.append(int(input()))
        m2.append(x)
    print("Matrix 2: ",m2)
    Subtraction(m1,m2,result)
    print("Result: ",result)
else:
    print("Enter 9 Numbers")
    result=[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    m1=[]
    print("Values for Matrix 1")
    for row in range(3):
        x=[]
        for col in range(3):
            x.append(int(input()))
        m1.append(x)
    print("Matrix 1: ",m1)
    m2=[]
    print("Values for Matrix 2")
    for row in range(3):
        x=[]
        for col in range(3):
            x.append(int(input()))
        m2.append(x)
    print("Matrix 2:",m2)
    Multiplication(m1,m2,result)
    print("Result: ",result)