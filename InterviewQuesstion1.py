# #Merging Two Sorted List
# # #Solution 1
# # a = [3, 4, 6, 10, 11, 18]
# # b = [1, 5, 7, 12, 13, 19, 21]
# # print(sorted(a+b))
# #
# # #Solution 2
# # a = [1, 5, 7, 12, 13, 19, 21]
# # b = [3, 4, 6, 10, 11, 18]
# # c = []
# # while a and b:
# #     if a[0]<b[0]:
# #         c.append(a.pop(0))
# #     else:
# #         c.append(b.pop(0))
# # print(a)
# # print(b)
# # print(c)
# # print(c+b+a)
# #
# # #Solution 3
# # a = [3, 4, 6, 10, 11, 18]
# # b = [1, 5, 7, 12, 13, 19, 21]
# # a.extend(b)
# # print(sorted(a))

List1 = [1,2,3,4,10,6,7,8]
List2 = [1,2,3,8,2,4,7,8]
#[True, True, True, False, False, False, True, True]
#{12: (4, 8), 11: (5, 6), 10: (6, 4)}
nl=[]
dit ={}
for i,j in zip(List1,List2):
    if i==j:
        nl.append(True)
    else:
        nl.append(False)
        dit[i+j]=dit.get(i+j,0)+(i+j)
        #dit[i+j]=(i,j)
print(dit)
print(nl)