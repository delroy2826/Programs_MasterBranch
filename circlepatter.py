n = 5
count=0
for row in range(n):
    for col in range(n):
        if ((col>=1 and col<=3) and (row==0 or row==4)) or \
        ((row>0 and row<4) and (col==0 or col==4)):
            print("* ",end='')
        else:
            print(end='  ')
    print()