#1
class Student():
    def __init__(self):
        self.name=input("Enter The Name:")
        self.__grade = "A+"
    def display(self):
        print("Name: {} ".format(self.name))
        print("Grade: {}".format(self.__grade))
s=Student()
s.display()

#2
class Student():
    def __init__(self,__grade):
        self.name=input("Enter The Name:")
        self.__grade = "A+"
    def display(self):
        print("Name: {} ".format(self.name))
        print("Grade: {}".format(self.__grade))
s=Student("B+")
s.display()

#3
class Student():
    def __init__(self):
        self.name=input("Enter The Name:")
        self.__grade = "A+"
    def display(self):
        print("Name: {} ".format(self.name))
        print("Grade: {}".format(self.__grade))
    def change(self):
        self.__grade="B+"
s=Student()
s.change()
s.display()

#4
class Product():
    def __init__(self):
        self.__price = 1000
    def selling(self):
        print("Selling Price: ",self.__price)
    def change(self):
        self.__price=int(input())
p=Product()
p.selling()

#5
class Product():
    def __init__(self):
        self.__price = 1000
    def selling(self):
        print("Selling Price: ",self.__price)
    def change(self):
        self.__price=int(input())
p=Product()
p.change()
p.selling()

#6
class Product():
    def __init__(self):
        self.price = 1000
    def selling(self):
        print("Selling Price: ",self.price)
    def change(self):
        self.price=int(input())
p=Product()
p.price="800"
p.selling()

#8
class Product():
    __price = 100
    def __init__(self):
        self.__price = int(input())
    def selling(self):
        print("Selling Price: ",Product.__price)
    def change(self):
        self.price=int(input())
p=Product()
p.__price="800"
p.selling()