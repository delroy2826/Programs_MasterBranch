#Question 8: Iterate a given list and Check if a given element already exists in a dictionary
#as a key’s value if not delete it from the list
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]  #64,37,83,95,
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
l=[]
for i in rollNumber:
    if i not in sampleDict.values():
        continue
    else:
        rollNumber.remove(i)
print(rollNumber)


rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]  #64,37,83,95,
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
new_l = []
l=[]

for i in sampleDict.items():
    new_l.append(i[1])
print(new_l)
for i in rollNumber:
    if i not in new_l:
        l.append(i)
print(l)