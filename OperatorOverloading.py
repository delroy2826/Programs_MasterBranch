#1
class Operation():
    def __init__(self):
        self.n1 = int(input("Enter The Number1: "))
        self.n2 = int(input("Enter the Number 2 :"))
    def __add__(self):
        print("Addition:",self.n1+self.n2)
O=Operation()
O.__add__()

#2
class Operation():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        x = self.x+other.x
        y=self.y+other.y
        return x,y

O=Operation(10,20)
O1=Operation(1,2)
print(O+O1)

#3
class Operation():
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        x = self.x+other.x
        return x

O=Operation(10)
O1=Operation(1)
print(O+O1)

#4
class Operation():
    y=30
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        x = self.x+other.x
        y= self.x +self.y
        return x,y

O=Operation(10)
O1=Operation(1)
print(O+O1)

#5
class Operation():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        x = self.x+other.x
        y=self.y+other.y
        return x,y
    def __gt__(self,other):
        c1 = self.x + self.y
        c2 = other.x +other.y
        return c1>c2

O=Operation(10,20)
O1=Operation(100,2)
print(O+O1)
print(O>O1)

#6
class Operation():
    x = 5
    y = 10
    def __init__(self,a):
        self.a=a
    def __add__(self):
        v=self.x+self.a
        return v
    def __mul__(self):
        v=self.y*self.a
        return v
O1 = Operation(2)
print(O1.__add__())
print(O1.__mul__())
