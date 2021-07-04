#Reversing the string
str1 = "Delroy"
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end='')
print()

#2
str1 = "Delroy"[::-1]
print(str1)