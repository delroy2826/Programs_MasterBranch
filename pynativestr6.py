#Given two strings, s1 and s2, create a mix String
#mixString("Pynative", "Website") = PeytniastbievWe
def mixstring(str1,str2):
    str3=''
    len_str1 = len(str1) #8
    len_str2 = len(str2) #7
    length = len_str1 if len_str1>len_str2 else len_str2 #8
    for i in range(length):
        if i<len_str1:
            str3+=str1[i]
        if i<len_str2:
            str3+=str2[i]
    return str3
str1 = "Pynative"
str2 = "Website"[::-1]
print(mixstring(str1,str2))

s1="Pynative"
s2="Website"[::-1]
if len(s1)<len(s2):
    length=len(s2)
else:
    length=len(s1)
str3=""
for i in range(length):
    if i<len(s1):
        str3+=s1[i]
    if i<len(s2):
        str3+=s2[i]
print(str3)