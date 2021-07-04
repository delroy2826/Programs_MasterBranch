#Given a list slice it into a 3 equal chunks and rever each list
#sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = []
count=0
for i in range(3):
    count+=1
    print("List:",count,l1[:3][::-1])
    l1=l1[3:]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
len_list1=len(list1)
count = 0
for i in range(len_list1//3):
    l=[]
    for j in range(3):
        l.append(list1[count])
        count+=1
    print(l[::-1])


