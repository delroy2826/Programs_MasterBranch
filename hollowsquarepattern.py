n = 5
for row in range(n):
    for col in range(n):
        if (col==0 or row==0) or (row==4 or col==4):
            print('* ',end='')
        else:
            print(end='  ')
    print()