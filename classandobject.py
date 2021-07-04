#1
class Demo():
    def __init__(self,age):
        self.age =age
        self.name =input("Name:")
    def method(self):
        print("My name is:",self.name)
        print("Age:",self.age)
d=Demo(5)
d.method()

#2
class Calc():
    def __init__(self):
        self.x=int(input("N1: "))
        self.y=int(input("N2: "))
    def __add__(self):
        print(self.x+self.y)
    def __sub__(self):
        print(self.x-self.y)
c=Calc()
c.__add__()
c.__sub__()

#3
class Person():
    fname = "John"
    lname = "Oliver"
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.id="45215"
    def __str__(self):
        return "First Name: " + self.fname+"\nLast Name: "+self.lname+"\nYour ID: " + self.id
    def Default(self):
        return __class__.fname, __class__.lname
a=input("Enter First Name: ")
b=input("Enter Last Name: ")
p=Person(a,b)
print(p)
print(p.Default())

#4
class Person():
    fname = "Delroy"
    lname = "Oliveira"
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)
    def __str__(self):
        return "First Name: "+self.fname+" Last Name: "+self.lname
p=Person('Sai','Krishna')
p.display()
p1=Person('Gokul','Pai')
p1.display()
print(p)
print(p1)

#5
class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return "Area:{}".format(self.l*self.b)
    def perimeter(self):
        return "Perimeter:{}".format(2*(self.l+self.b))
class Square(Rectangle):
    def __init__(self,l):
        super().__init__(l,l)
r=Rectangle(10,10)
print(r.area())
print(r.perimeter())
s=Square(5)
print(s.area())
print(s.perimeter())

#6
class Robot():
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello, I am {}".format(self.name))
class PhysianRobot(Robot):
    pass
r = Robot("Delroy")
r.say_hi()
p = PhysianRobot("Olive")
p.say_hi()

#7
class Robot():
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello, I am {}".format(self.name))
class PhysianRobot(Robot):
    def say_hi(self):
        print("Everything will be okay")
        print(self.name,"Will take care")

p = PhysianRobot("Olive")
p.say_hi()

#8
class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return "Area: {}".format(self.l*self.b)
    def perimeter(self):
        return "Perimeter: {}".format(2*(self.l+self.b))
class square(Rectangle):
    def __init__(self,l):
        super().__init__(l,l)
class square1(square):
    def __init__(self,l):
        super().__init__(l)
s1=square1(10)
print("Square1: ",s1.area())
s=square(5)
print("Square: ",s.perimeter())
r = Rectangle(5,10)
print("Rectangle {} and {}".format(r.area(),r.perimeter()))

#9
class Student():
    def getStudent(self):
        print("*"*20)
        self.name=input("Enter Your Name: ")
        self.age=input("Enter the Age: ")
        self.gender=input("Enter the Gender: ")
        print("*"*20)
class Test(Student):
    def getMarks(self):
        self.studclass = input("Class: ")
        print("Enter the Marks for")
        print("*"*20)
        self.math = int(input("Math: "))
        self.chemistry=int(input("Chemistry: "))
        self.total = self.math+self.chemistry
class Marks(Test):
    def display(self):
        print("*"*20)
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("*"*20)
        print("Marks obtained ")
        print("Math: {} Chemistry:{} ".format(self.math,self.chemistry))
        print("Total Marks: ",self.total)
        print("*"*20)
m = Marks()
m.getStudent()
m.getMarks()
m.display()

#10
class Student():
    def getStudent(self):
        print("*"*20)
        self.name=input("Enter Your Name: ")
        self.age=input("Enter the Age: ")
        self.gender=input("Enter the Gender: ")
        print("*"*20)
class Test():
    def getMarks(self):
        self.studclass = input("Class: ")
        print("Enter the Marks for")
        print("*"*20)
        self.math = int(input("Math: "))
        self.chemistry=int(input("Chemistry: "))
        self.total = self.math+self.chemistry
class Marks():
    def display(self):
        print("*"*20)
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("*"*20)
        print("Marks obtained ")
        print("Math: {} Chemistry:{} ".format(self.math,self.chemistry))
        print("Total Marks: ",self.total)
        print("*"*20)
class Details(Student,Test,Marks):
    def getInfo(self):
        Student.getStudent(self)
        Test.getMarks(self)
        Marks.display(self)
d=Details()
d.getInfo()

#11
class Student():
    def __init__(self):
        self.fname = input("Enter Your First Name: ")
        self.lname = input("Enter Your Last Name: ")
        self.age   = input("Enter Your Age: ")
    def display(self):
        print("Name:",self.fname,self.lname)
        print("Age: ",self.age)
class Marks():
    def __init__(self):
        print("Enter the Scores")
        self.math=int(input("Math: "))
        self.chemistry = int(input("Chemistry: "))
    def display(self):
        print("Total: {}".format(self.math+self.chemistry))
class Person(Student,Marks):
    def __init__(self):
        Student.__init__(self)
        Marks.__init__(self)
        Student.display(self)
        Marks.display(self)
p=Person()
print(Person.__mro__)

class Error(Exception):
   """Base class for other exceptions"""
   pass
#class ValueTooSmallError(Error):
   #"""Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
# our main program
# user guesses a number until he/she gets it right
# you need to guess this number
number = 10
while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()
print("Congratulations! You guessed it correctly.")