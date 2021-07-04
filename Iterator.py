#1
l=[1,2,3,4,5]
a=iter(l)
print(next(a))
print(next(a))

#2
l=[1,2,3,4,5]
a=iter(l)
print(*a)

#3
l=[1,2,3,4,5]
a=iter(l)
for i in range(len(l)):
    print(next(a))

#4
l=[1,2,3,4,5,6]
a=iter(l)
while True:
    try:
        print(next(a))
    except Exception:
        break

#5
l=[1,2,3,4,5,6]
a=iter(l)
for i in l:
    print(2**next(a))

#6
a = iter(int,2)
print(next(a))
print(next(a))
print(next(a))
print(next(a))