#Make a function to insert Items In an array and another Fucntion to
#Display The the most repeated item from an array  Forexmple:
#Input : l1= ['Next', 'Gin', 'Coder', 'Gin', 'Coder', 'Gin', 'Next', 'Next']
#Output : "Gin" "Next"
l1= ['Next', 'Gin', 'Coder', 'Gin', 'Coder', 'Gin', 'Next', 'Next']
l3 = []
for i in sorted(set(l1)):
    a=l1.count(i)
    l3.append(str(a)+i)
#print(l3)
high=max(l3)[:1:]
#print("High:",high)
#print(max(l3)[1::])
for i in l3:
    #print(i[:1:])
    if str(high) == i[:1:]:
        #l4.append(i[1::])
        print(i[1::])
'''l1= input("Enter Item Less than or Equal to  9 Items\nTo check Frequently Appeared Item: ").split()
l3 = []
for i in sorted(set(l1)):
    a=l1.count(i)
    l3.append(str(a)+i)
high=max(l3)[:1:]
for i in l3:
    if str(high) == i[:1:]:
        print(i[1::])'''

#3
l1= input().split()
l2 = sorted(set(l1))
l3 = []
a=0
for i in l2:
    count = a
    if l1.count(i)>=a:
       l3.append(i)
       a=l1.count(i)
    for i in l3:
        if l1.count(i)<a:
            l3.remove(i)
print(l3)