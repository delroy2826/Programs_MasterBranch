#Question 8: Print the following pattern
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''
def right_angle(n):
    for i in range(1,n+1):
        count=0
        for j in range(i):
            count+=1
            print(count,end=' ')
        print()

n = 5
right_angle(n)

n = 6
for i in range(1,n):
    for j in range(1,n):
        if j==0 or i==n-1 or i==j or i>=j:
            print(j," ",end='')
        else:
            print(end='  ')
    print()