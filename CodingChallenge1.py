#A number is called SPY number If the sum and product of its digits  are equal
#For Example 1+2+3 = (1*2*3)
n = "123"
sum = 0
product = 1
for i in n:
    sum+=int(i)
    product*=int(i)
if sum == product:
    print("Spy Number:Becasue {} == {}".format(sum,product))
else:
    print("Not Spy Number:Becasue {} != {}".format(sum,product))