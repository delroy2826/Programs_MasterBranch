#Question 7: Given two sets, Checks if One Set is Subset or superset of Another Set.
#if the subset is found delete all elements from that set
#firstSet = {27, 43, 34}
#secondSet = {34, 93, 22, 27, 43, 53, 48} Output: First set is sub set of second set firstSet = {}
firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
print("FirstSet:",firstSet)
print("SecondSet:",secondSet)
print("FirstSet is subset of secondSet:",firstSet.issubset(secondSet))
print("SecondSet is subset of FirstSet:",secondSet.issubset(firstSet))
print("FirstSet is superset of secondSet:",firstSet.issuperset(secondSet))
print("SecondSet is superset of FirstSet:",secondSet.issuperset(firstSet))
if firstSet.issubset(secondSet):
    firstSet.clear()
if secondSet.issubset(firstSet):
    secondSet.clear()
print(firstSet)
print(secondSet)