l1 = [1,2,3,4,5,6,7,8,9,10,11]
jump = int((len(l1)-1)**0.5)
print(jump)
find=7
for i in range(0,len(l1),jump):
    #print('First',l1[i],i)
    if l1[i]== find:
        print("Element {} is in position {}".format(l1[i],i))
        break
    elif l1[i] > find:
        #print("Second",l1[i],i)
        for i in range(i,0,-1):
            #print(l1[i])
            if l1[i]==find:
                print("Element {} is in position {}".format(l1[i],i))
                break
        break