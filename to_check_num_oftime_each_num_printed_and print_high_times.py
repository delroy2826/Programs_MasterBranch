l1 = [1,1,0,1,0,0,0,0,1,1,0,0,0]
count1 = 0
count0 = 0
for i in l1:
    if i==1:
        count1+=1
    else:
        count0+=1
if count0>count1:
    print(0,'is used',count0,'Times')
elif count0==count1:
    print(0,'and',1,'are printed',count0,'Times' )
else:
    print(1,'is used',count1,'Times')

