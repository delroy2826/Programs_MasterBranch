# class Person:
#     NoName="No Name"
#     def __init__(self,name=NoName):
#         self.name = name
#
#     def my_name(self):
#         if self.name!=self.NoName:
#             return f"My Name is {self.name}"
#         else:
#             return "Please enter valid name"
# p1=Person()
# print(p1.my_name())
# p2=Person("Delroy")
# print(p2.my_name())

# class BankAccount:
#     def __init__(self,name,money):
#         self.name=name
#         self.__balance=money
#     def deposit(self,money):
#         self.__balance+=money
#         balance = self.checkBalance()
#         return  balance
#     def withdraw(self,money):
#         if self.__balance > money:
#             self.__balance-=money
#             return money
#         else:
#             return "In Sufficient Money"
#
#     def checkBalance(self):
#         return self.__balance
#
# bankAccont_1 = BankAccount("Delroy",10000)
# print(bankAccont_1.checkBalance())
# print(bankAccont_1.withdraw(500))
# print(bankAccont_1.checkBalance())
# print(bankAccont_1.deposit(4000))
# print(bankAccont_1.withdraw(15000))
# print(bankAccont_1.name)

# import math
#
# class Circle:
#     def __init__(self,radius):
#         self.__radius=radius
#
#     def setRadius(self,radius):
#         self.__radius = radius
#
#     def getRadius(self):
#         return self.__radius
#
#     def area(self):
#         return math.pi * self.__radius **2
#
#     def __add__(self, other):
#         return Circle(self.__radius + other.__radius)
#
# c1 = Circle(5)
# print(c1.getRadius())
# print(c1.area())
# c2 = Circle(10)
# print(c2.getRadius())
# print(c2.area())
# c3 = c1 +c2
# print(c3.getRadius())

# from pathlib import *
# current_dir = Path.cwd()
# home_dir = Path.home()
# print(current_dir)
# print(home_dir)
#
# import os
# current_path = os.path.join(os.getcwd(),"output")
# output_path_file = os.path.join(current_path,"out.xlsx")
#
# os.pathjoin(os.)

# lst = [1,2,3,4]
# print(*lst)
#
#
# print(0.1+0.2)
#
# print(int(2 & 5))

# for i ,j in [[0,3],[1,3]]:
#     print(i,j)

# def insert():
#     l = input(["Next","Gen","Next","Coder"]).lower().split()
#     def dup(l):
#         l2 = sorted(set(l))
#         print(l)
#         print(l2)
#     dup(l)
# insert()
# def function1(variable:str):
#     print(type(variable))
#
# function1(1)
# dict_1 = {"list1":[1,2,3,4],"Name":"Raju"}
# print(dict_1.get("list2","N key"))



import re
# pattern = re.compile(r"\d{1,3}[., ]\d{1,3}")
# str1 = "Withyourexclusivepromocode,yousaveSEK2 111onthisorder."
# matches = pattern.search(str1)
# print(matches.group())

phone = "(123) 999-12321"
print(re.sub('[^0-9]+', '', phone))

