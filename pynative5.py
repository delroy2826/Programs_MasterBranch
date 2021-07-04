#Question 5: Given a list of ints, return True if first and last number of a list is same
def check(numList):
    return numList[0]==numList[-1]
numList = [10, 20, 30, 40, 10]
print(check(numList))

numList = [10, 20, 30, 40, 10]
if numList[0]==numList[-1]:
    print(True)
else:
    print(False)