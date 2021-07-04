#Make A function To Insert Items In an Array and another function to remove all
#Repeated Items From an array and Display the array
#For example :["Next","Gen","Next","Coder"] Output: ["Next","Gen","Coder"]
#Write a program to remove all repeated items from an user defined Array
def insert():
    l = input(["Next","Gen","Next","Coder"]).lower().split()
    def dup(l):
        l2 = sorted(set(l))
        print(l)
        print(l2)
    dup(l)
insert()
#2
def insert():
    global l1
    l1= input("Enter the elements:\n").split()
    print(check(l1))
def check(l1):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2
i=insert()

#3
def insert():
    l1 = input("Enter the elements:\n").split()
    def check():
        l2 = []
        for i in l1:
            if i not in l2:
                l2.append(i)
        return l2
    print(check())
insert()

#4
l1 = input().split()
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)