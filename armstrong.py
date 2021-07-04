n = 153
nlen = len(str(n))
exp=0
for i in str(n):
    exp +=int(i)**nlen
if exp==n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")