
str1 = "abcdefghijasdasda8qw"
lstr1 = len(str1)
#print(lstr1)
if lstr1%2==0:
    sep=2
else:
    sep=3
a=0
index=0
for i in range(sep,lstr1+1,sep):
    for j in range(i-a):
        print(str1[index],end='')
        index+=1
        a=i
    print()

str1 = "abcdefghijasdasd2a8qw2"
if len(str1)%2==0:
    i=0
    while i<len(str1):
        print(str1[i],end='')
        i+=1
        print(str1[i])
        i+=1
else:
    i=0
    while i<len(str1):
        print(str1[i],end='');i+=1
        print(str1[i],end='');i+=1
        print(str1[i]);i+=1


str1 = "Hel lo  Jac k"
count= 0
for i in str1:
    if i==" ":
        count+=1
print(count)

n = "00-11111".split('-')
#print(n)
for i in n[::-1]:
    print(i,end='')
print()


n = 10101
a = sorted(str(n))
for i in a[::-1]:
    print(i,end='')
print()