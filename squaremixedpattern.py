n = 5
count=0
for row in range(n):
    for col in range(n):
        if (col==row) or (col<=4 and row<=0 ) or (col==4 and row>0) or\
        ((col==0 and row>0) or row == 4) or (col==3 and row==1) or \
        (col==1 and row==3):
            print("+ ",end='')
        else:
            count+=1
            print(count,end=' ')
    print()