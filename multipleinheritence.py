class Person():
    def __init__(self):
        print("One")
        self.name=input("NAME:")
        self.age=input("Age:")
        self.gender=input("Gender:")

    def display(self):
        print("Three")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
class Marks():
    def __init__(self):
        print("Two")
        self.m1=int(input("m1:"))
        self.m2=int(input("m2:"))
        self.m3=int(input("m3:"))
    def display(self):
        print("Four")
        print("M1: ",self.m1)
        print("M2: ",self.m2)
        print("M3: ",self.m3)
        print("Total Marks:{} ".format(self.m1+self.m2+self.m3))
class Student(Person,Marks):
    def __init__(self):
        Person.__init__(self)
        Marks.__init__(self)
    def display(self):
        Person.display(self)
        Marks.display(self)
s=Student()
print(Student.__mro__)
s.display()