#Number Pattern
'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1'''
n = 6
for row in range(1,n):
    for col in range(row,0,-1):
        print(col,end=' ')
    print()