#Question 9: Given a dictionary get all values from the dictionary
#and add it in a list but don’t add duplicates
#speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
l = []
for i in speed.values():
    l.append(i)
print(list(set(l)))

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
l = []
for i in speed.values():
    if i not in l:
        l.append(i)
print(l)