#Question 3: Given 2 strings, s1, and s2 return a new string made of the first,
#middle and last char each input string mixString("America", "Japan") = ""AJrpan"
def mixString(str1,str2):
    str3 = ''
    str3+=str1[0]
    str3+=str2[0]
    str3+=str1[len(str1)//2]
    str3+=str2[len(str2)//2]
    str3+=str1[-1]
    str3+=str2[-1]
    return str3

str1 = 'America' #Dry
str2 = 'Japan' #Jpn
str3 = ''
print(mixString(str1,str2))

str1="America"
str2="Japan"
str3=str1[0]+str2[0]+str1[len(str1)//2]+str2[len(str2)//2]+str1[-1]+str2[-1]
print(str3)