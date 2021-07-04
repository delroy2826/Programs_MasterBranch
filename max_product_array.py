l1 = [1,-1112,-3,0,5,66,97,0,-1,-2,-3,0,9,88,9]
l2 = []
for i in l1:
    if i<0:
        l2.append(int(str(i)[1:]))
    else:
        l2.append(i)
listn=[]
final =[]
while True:
    if l2.count(0)==0:
        listn+=[l2]
        break
    else:
        a=l2.index(0)
        listn+=[l2[:a:]]
        l2.pop(l2.index(0))
        l2=l2[a::]
for i in listn:
    result=1
    for j in i:
        result*=j
    final.append(result)
print(max(final))

#2
list1 = [1,-1112,-3,0,5,66,97,0,-1,-2,-3,0,9,88,9]
fil_list = []
new_list = []
for i in list1:
    if i>0:
        fil_list.append(i)
    else:
        fil_list.append(-i-0)
a=1
for i in fil_list:
    if i!=0:
        a*=i
    else:
        new_list.append(a)
        a=1
new_list.append(a)
print(max(new_list))
print(new_list)

#3
list1 = [1,-1112,-3,0,5,66,97,0,-1,-2,-3,0,-9,-888,-9]
new_list = []
a=1
for i in list1:
    b = i if i > 0 else -i   #[on_true] if [expression] else [on_false]
    if b!=0:
        a*=b
    else:
        new_list.append(a)
        a=1
new_list.append(a)
print(max(new_list))
print(new_list)