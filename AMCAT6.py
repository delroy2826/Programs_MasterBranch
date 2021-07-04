#Programs to count frequency of occurrence of digits in a array
n= 11203458760011
strn= str(n)
for i in range(10):
    print("Frequency of {} = {}".format(i,strn.count(str(i))))

n= 11203458760011
strn=str(n)
for i in set(strn):
    print("{} is {}".format(i,strn.count(i)))

