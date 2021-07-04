#Question 9: Given a string, return the sum and average of the digits that
#appear in the string, ignoring all other characters
#sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5
def calc(str1):
    sum=0
    avg = 0
    for i in str1.split():
        if i.isnumeric():
            sum+=int(i)
            avg+=1
    return "Sum is {} and Average is {} ".format(sum,sum/avg)
str1="English = 78 Science = 83 Math = 68 History = 65 Ball = 5"
print(calc(str1))

s1="English = 78 Science = 83 Math = 68 History = 65".split()
sum1=0
count=0
per = 0
for i in s1:
    if i.isdigit():
        count+=1
        sum1+=int(i)
print(sum1)
print(sum1/count)