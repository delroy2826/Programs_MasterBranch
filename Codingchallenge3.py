"""Write a program to order any string in (Ascending)
alphabetical Order For Example
NextGenCoder - > CdeeeGNnortx"""
str1 = "NextGenCoder"
b = list(str1)
print(b)
a = sorted(str1.lower())
print(a)
str2 = ""
for i in a:
    if i.upper() in b:
        index = b.index(i.upper())
        b.pop(index)
        str2+=i.upper()
    else:
        str2+=i
print(str1,"->>",str2)

#2
str1 = "NextGenCoder"
list_str1 = list(str1)
sort_list_str1 = sorted(str1.lower())
for i in sort_list_str1:
    if i.upper() in list_str1:
        print(i.upper(),end='')
        list_str1.remove(i.upper())
    else:
        print(i,end='')