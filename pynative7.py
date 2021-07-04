#Question 7: Return the number of times that the string
#“Emma” appears anywhere in the given string
def count(str1):
    Emma=0
    for i in str1.split():
        if i=="Emma":
            Emma+=1
    return Emma
str1 = "Emma is a good developer. Emma is also a Emma writer"
print(count(str1))