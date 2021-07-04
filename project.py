n=int(input("Enter the Number to be searched:"))
a = set(map(int,input().split()))
l = list(a)
l.sort()
print(l)
mid = len(l)//2

if n==l[mid]:
    print(mid)

if n > l[mid]:
    new_l = l[mid:]
    for i in range(len(new_l)):
        if new_l[i]==n:
            print(i+mid)

if n < l[mid]:
    new_l = l[:mid]
    for i in range(len(new_l)):
        if new_l[i]==n:
            print(i)


