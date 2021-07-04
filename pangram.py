letters = list(" abcdefghijklmnopqrstuvwxyz")
count=0
len_letter=len(letters)
str1 = "the quick brown fox jumps over the lazy dog".lower()
sorted_str1 = sorted(set(str1))
for i in sorted_str1:
    if i in letters:
        #print(i)
        count+=1
if count == len_letter:
    print("Pangram")
else:
    print("Not Pangram")

'''
str1 = "the quick brown fox jumps over the lazy dog".lower()
my_dict = dict()
for i in str1.split():
    for j in i:
        my_dict[j] = my_dict.get(j ,0)+1
if len(my_dict)==26:
    print("Pangram")
else:
    print("Not Pangram")'''