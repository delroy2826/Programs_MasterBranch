#Write a Program Which will take Two arrays as input and will Display Two Arrays with
#Union and intersection of them
#Write a program to display union and intersection of given arrrays
#For Example Input A=[1,3,4,5,6] B=[2,3,4,5,8]
#OutPut = Union [1,2,3,4,5,6,8] Intersection [3,6,8]
list1 = [1,2,3,4,5]
list2 = [3,4,6,7,8]
str2 = ""
str3 = ""
for i in list1:
    if i not in list2:
        str2+=str(i)
        #print(str2)
for i in list2:
    str2+=str(i)
print("Union=",",".join(sorted(str2)))
for i in list1:
    if i in list2:
        str3+=str(i)
print("Intersection=",",".join(sorted(str3)))