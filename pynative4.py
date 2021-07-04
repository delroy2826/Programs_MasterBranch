#Question 4: Given a string and an int n, remove characters from string starting
#from zero upto n and return a new string
def str1_new(str1,n):
    str2 = str1[n::]
    print(str2)
str1 = input("Enter the String: ")
n = int(input("Enter the nuber: "))
str1_new(str1,n)

str1 = "abcdefghi"
n = int(input("Number:"))
print(str1[n::])

str1 = "abcdefghi"
n=int(input("Number: "))
for i in range(len(str1)):
    if i>=n:
        print(str1[i],end='')
print()