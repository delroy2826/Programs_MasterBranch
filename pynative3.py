#Question 3: Accept string from the user and display only those characters which are present
#at an even index
def even(str1):
    for i in range(1,len(str1)):
        if i%2==0:
            print(str1[i])
str1 = input("Enter the String: ")
even(str1)


# str1 = "abcdefdhi"
# for i in range(1,len(str1)):
#     if i%2==0:
#         print(str1[i])