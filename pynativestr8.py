#Question 8: Find all occurrences of “USA” in given string ignoring the case
#countOccurrences("Welcome to USA. usa awesome, isn't it?") = 2
def count(str1,str2):
    return str1.count(str2)
str1 ="Welcome to USA. usa awesome, isn't it?".lower()
str2 = 'USa'.lower()
print(count(str1,str2))

s1="Welcome to USA. usa awesome, isn't it?".split()
count=0
for i in s1:
    if i.lower()=="usa":
        count+=1
print(count)
s1="Welcome to USA . usa awesome, isn't it?".lower()
print(s1.count("usa"))