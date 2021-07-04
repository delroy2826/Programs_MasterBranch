# lower = 1
# upper = 20
#
# for i in range(lower,upper):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
#     else:
#         print(i)

# data = "mom"
#
# if data == data[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# userinput = 23
# fact  = 1
#
# for i in range(1,userinput+1):
#     fact *=i
# print(fact)

# n=9
# list_data = []
# for i in range(n):
#     if i>1:
#         list_data.append(list_data[i-2]+list_data[i-1])
#     else:
#         list_data.append(i)
# print(list_data)

# year = 2018
#
# if year%4==0 and year%100!=0 or year%400==0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# n1=4
# n2 = 6
#
# if n1>n2:
#     greater =n1
# else:
#     greater = n2
#
# while 1:
#     if greater%n1==0 and greater%n2==0:
#         lcm=greater
#         break
#     greater+=1
# print(lcm)

# n1 = 12
# n2 = 30
#
# if n1>n2:
#     smaller=n1
# else:
#     smaller=n2
#
# for i in range(1,smaller+1):
#     if n1%i==0 and n2%i==0:
#         hcf=i
# print(hcf)

# lower = 1
# upper = 20
# for i in range(lower,upper):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
#     else:
#         print(i)
#
# data = "mom"
# if data == data[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# n=23
# fact=1
#
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n=9
# list_data = []
# for i in range(n):
#     if i>1:
#         list_data.append(list_data[i-2]+list_data[i-1])
#     else:
#         list_data.append(i)
# print(list_data)

# n1 = 4
# n2 = 6
# if n1>n2:
#     greater = n1
# else:
#     greater = n2
#
# while 1:
#     if greater%n1==0 and greater%n2==0:
#         lcm=greater
#         break
#     greater+=1
# print(lcm)

n1 = 12
n2 = 30

if n1>n2:
    smaller = n1
else:
    smaller = n2

for i in range(1,smaller+1):
    if n1%i==0 and n2%i==0:
        hcf=i

print(hcf)
