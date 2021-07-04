#Python Program to Print Natural Numbers in Reverse Order
#Using For Loop
n = 15
for i in range(n,0,-1):
    print(i,end=' ')
print()
#Using While Loop
while n:
    print(n,end= ' ')
    n-=1

n=10
for i in range(n,-1,-1):
    print(i)