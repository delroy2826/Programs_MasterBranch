#Bubble Sort
def bubblesort1(lnum):
    for i in range(len(lnum)-1,0,-1):
        for j in range(i):
            if lnum[j]>lnum[j+1]:
                lnum[j],lnum[j+1]=lnum[j+1],lnum[j]
    print(lnum)
def bubblesort2(lnum):
    for i in range(len(lnum)-1,0,-1):
        for j in range(i):
            if lnum[j]>lnum[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    print(lnum)

l = input("Enter the numbers separated by commas:\n").split(',')
l = list(map(lambda x:int(x),l))
print(l)
#bubblesort1(l)
bubblesort2(l)