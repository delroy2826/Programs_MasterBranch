#Take Integer Value as an Input and Display the number of 1's in the Binary of that Number as Output
#For Example: 124 i.e (1111100) Output: 5
'''n = 200
print(bin(n)[2::])
a = bin(n)[2::]
count=0
for i in a:
    if i=="1":
        count+=1
print(count)'''
'''def count(n):
    print("The Binary form for {1} is {0}.".format(bin(n)[2::],n))
    a = bin(n)[2::]
    count=0
    for i in a:
        if i==str(1):
            count+=1
    return count
n=int(input("Enter the number to be checked:"))
print("The number of 1's in {1} is {0}.".format(count(n),n))'''
n=bin(int(input("Enter the number"))).count("1")
print(n)

'''
n1 = 124
for i in range(n1+1):
    str1 = bin(i)[2::]
    count = 0
    for j in str1:
        if j == "1":
            count+=1
    print("Binary of {} and Number of 1's is {}".format(i,count))'''