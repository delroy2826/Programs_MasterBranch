#Repeated Items From an arra and Display the array
#For example :["Next","Gen","Next","Coder"] Output: ["Next","Gen","Coder"]
#Write a program to remove all repeated items from an user defined Array
l1 = input().split()
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        continue
print(l2)