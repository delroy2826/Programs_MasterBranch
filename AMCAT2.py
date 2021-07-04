# #Prime Numbers
# lower =1
# upper = 20
# for i in range(lower,upper):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
#     else:
#         print(i)

lower = 1
upper = 20

for i in range(lower,upper):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
    else:
        print(i)