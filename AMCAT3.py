#LCM
n1 = 4
n2 = 6
if n1>n2:
    greater=n1
else:
    greater=n2
while 1:
    if greater%n1==0 and greater%n2==0:
        lcm=greater
        break
    greater+=1
print(greater)