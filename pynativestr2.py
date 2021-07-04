#Question 2: Given 2 strings, s1 and s2, create a
#new string by appending s2 in the middle of s1 Chrisdem -> ChriIamNewStringsdem
def concatinate_str(str1,str2):
    mid = len(str1)//2
    str1[mid:]
    str1 = str1[:mid] + str2 + str1[mid:]
    return str1

str1 = "Chrisdem"
str2 = "IamNewString"
print(concatinate_str(str1,str2))

s1="Chrisdem"
s2="IamNewStringsdem"
new_str = s1[:len(s1)//2:]+s2+s1[len(s1)//2::]
print(new_str)