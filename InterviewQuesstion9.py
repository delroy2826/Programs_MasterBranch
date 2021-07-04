# #Have the function LetterChanges(str) take the str parameter being passed and modify
# #it using the following algorithm. Replace every letter in the string with
# #the letter following it in the alphabet (ie. c becomes d, z becomes a).
# #Then capitalize every vowel in this new string (a, e, i, o, u)
# #and finally return this modified string.
# def LetterChanges(str):
#     str1="abcdefghijklmnopqrstuvwxyz"
#     l=list(str1)
#     str3=""
#     str4=""
#     for i in str:
#         try:
#             if i in l:
#                 index = l.index(i)
#                 str3+=l[index+1]
#             else:
#                 str3+=i
#         except:
#             str3+=l[0]
#     for i in str3:
#         if i in "aeiou":
#             str4+=i.upper()
#         else:
#             str4+=i
#     return str4
#
# print(LetterChanges(input()))
# '''
# str1="abcdefghijklmnopqrstuvwxyz"
# l=list(str1)
# str2="fun times!".lower()
# str3=""
# for i in str2:
#     try:
#         if i in l:
#             index = l.index(i)
#             str3+=l[index+1]
#         else:
#             str3+=i
#     except:
#         str3+=l[0]
# str4=""
# for i in str3:
#     if i in "aeiou":
#         str4+=i.upper()
#     else:
#         str4+=i
# print(str4)'''

def dictCreator(x,y):
    dict_1[x+y]=dict_1.get(x+y,(x,y))
    return False
List1 = [1,2,3,4,5,6,7,8]
List2 = [1,2,3,8,6,4,7,8]
dict_1 =dict()
New_List= [True if x==y else dictCreator(x,y)  for (x,y) in zip(List1,List2)]
print(New_List)
print(dict_1)

# value = zip(List1,List2)
# print(value)