l =[5,3,8,6,7,2]
for i in range(len(l)-1):
    minpos = i
    for j in range(i,len(l)):
        if l[j]<l[minpos]:
            minpos=j
    temp=l[i]
    l[i]=l[minpos]
    l[minpos]=temp
print(l)