#Question 6: Given a list of numbers, Iterate it and print only those numbers
#which are divisible of 5
numList = [10, 20, 33, 46, 55]
new_list = [i for i in numList if i%5==0]
print(new_list)


numList = [10, 20, 33, 46, 55,15]
i=0
while i<len(numList):
    if numList[i]%5==0:
        print(numList[i])
        i+=1
    else:
        i+=1