str1 = input("Enter the string: ").lower()
if str1 == str1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

'''
str1 = "ma1m"
count= 0
for i in range(len(str1)):
    try:
        if str1[i]==str1[-i-1]:
            count+=1
        else:
            print("Not a Palindrome")
            break
    finally:
        if count==len(str1):
            print("palindrome")'''