def testgen(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    for i in range(5):
        yield weekdays[index]
        index+=1
day = testgen(0)
print(*day)

def check(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    for i in range(val):
        yield weekdays[index]
        index+=1

index=0
val=int(input("Enter the number: "))
day = check(index)
print(*day)