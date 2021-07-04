#max_product_array Nikil
k=[1,-2,-3,0,-1,-2,-3,0,5,6,7]
if k[len(k)-1]!=0:
    k.append(0)
l=k
count =0
for i in k :
    if i==0:
      count+=1
b1=0
l3=[]
while b1<count:
    l2=[]
    b=0
    for i in l:
        if i==0:
          break
        else:
          l2.append(i)
        b+=1
    k=1
    for i in l2:
        k*=i
    l3.append(k)
    c=0
    while c<=b:
        del l[0]
        c+=1
    l=l
    b1+=1
print(l3)
print(max(l3))