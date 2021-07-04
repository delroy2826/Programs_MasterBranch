#Question 4: arrange String characters such that lowercase letters should come first
#lowercaseFirst("PyNaTive") = aeiNPTvy
def Rearrange(str1):
    str2=''
    for i in str1:
        if i.islower():
            str2+=i
    for i in str1:
        if i.isupper():
            str2+=i
    return str2
str1 = "PyNaTive"
print(Rearrange(str1))

str1="PyNaTive"
str2=""
str3=""
for i in str1:
    if i==i.lower():
        str2+=i
    else:
        str3+=i
print(str2+str3)