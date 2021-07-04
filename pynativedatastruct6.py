#Question 6: Given a following two sets find the
#intersection and remove those elements from the first set
#firstSet = {10, 30, 40 , 60, 45}
#secondSet = {20, 50, 10 , 40, 55}
#Expected Outcome: firstSet = {30, 60, 45}
fSet = {10, 30, 40 , 60, 45}
sSet = {20, 50, 10 , 40, 55}
newSet = set(fSet&sSet)
for i in newSet:
    fSet.remove(i)
print(fSet)

fSet = {10, 30, 40 , 60, 45}
sSet = {20, 50, 10 , 40, 55}
for i in list(fSet):
    if i in sSet:
        fSet.remove(i)
print(fSet)