#Remove duplicate from a list and create a tuple and find the minimum and maximum number
l = [87, 45, 41, 65, 94, 41, 99, 94]
dup = tuple(set(l))
print(max(dup))
print(min(dup))