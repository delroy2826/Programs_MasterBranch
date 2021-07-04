#Question 2: Given a range of numbers. Iterate from o^th number to the
#end number and print the sum of the (current and previous number)
def calc(num):
    prev = 0
    for i in range(num+1):
        sum = i + prev
        print(sum)
        prev = i
num = int(input("Enter the range: "))
calc(num)

prev = 0
i=0
while prev < 9:
    sum1 = i+prev
    print(sum1)
    prev =i
    i+=1