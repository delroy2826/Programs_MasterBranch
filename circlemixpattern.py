n = 5
count=0
for row in range(n):
    for col in range(n):
        if ((col>=1 and col<=3) and (row==0 or row==4)) or \
        ((row>1 and row<3) and (col>1 or col<3)) or \
        ((col==0 or col==4) and (row ==1 or row==3)) or (col==2 and (row==1 or row==3) ) :
            print("* ",end='')
        else :
            print(end='  ')
    print()