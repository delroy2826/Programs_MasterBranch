str1 = "the quick brown fox jumps over the lazy dog".lower()
for i in sorted(set(str1)):
    if i==" ":
        continue
    else:
        a=str1.count(i)
    print("(",i,"->",a,end=')')
    print()
str1 = "the quick brown fox jumps over the lazy dog".lower()
my_dict = dict()
for i in str1:
    my_dict[i]=my_dict.get(i,0)+1
print(my_dict)