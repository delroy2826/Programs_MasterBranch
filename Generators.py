#1
def demo():
    n=1
    yield n
    n+=1
    yield n
    n+=1
    yield n
    n+=1
    yield n
d=demo()
print(next(d))
print(next(d))
print(next(d))
print(next(d))

#2
def demo():
    n=1
    yield n
    n+=1
    yield n
    n+=1
    yield n
    n+=1
    yield n
d=demo()
print(*d)

#3
def demo():
    n=1
    yield n
    n+=1
    yield n
    n+=1
    yield n
    n+=1
    yield n
d=demo()
print(*d)
d1=demo()
print(*d1)

#4
def demo():
    n=1
    yield n
    n+=1
    yield n
    n+=1
    yield n
    n+=1
    yield n
for i in demo():
    print(i)
#5
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
x = simpleGeneratorFun()
print(next(x))
print(next(x))
print(next(x))

#6
l=[1,2,3,4,5,6,7,8,9]
a = (x**2 for x in l)

for i in l:
    print(next(a))
