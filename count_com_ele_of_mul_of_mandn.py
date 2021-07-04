n1 = 2
n2 = 4
k = 9
array1 = []
array2 = []

for i in range(1,k):
    a=n1*i
    if a <=k:
        array1.append(a)
        print(array1)
for i in range(1,k):
    a = n2*i
    if a <=k:
        array2.append(a)
        print(array2)
common_val = len(list(set(array1)&set(array2)))
print("Number of common elements: ",common_val)

#2
n1 = 2
n2 = 4
k=9
ln1=[]
ln2 = []
for i in range(1,k):
    if n1*i<k:
        ln1.append(n1*i)
for i in range(1,k):
    if n2*i<k:
        ln2.append(n2*i)
print(sorted(set(ln1)&set(ln2)))
print(len(set(ln1)&set(ln2)))