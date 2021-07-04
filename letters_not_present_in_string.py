letters = " abcdefghijklmnopqrstuvwxyz".lower()
str1 = "Delroy Oliveira".lower()
str2 = ''.lower()
for i in letters:
    if i in str1:
        continue
    else:
        str2+=i
print(list(str2))
