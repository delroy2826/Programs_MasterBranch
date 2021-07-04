#This method is used to save time.It iters through a string only once
#instead of iter One Element with all until we find the Match if not Matches then print Null
str1 = 'abca'
my_dict = dict()
for i in str1:
    my_dict[i]=my_dict.get(i,0)+ 1
    if my_dict[i]>1:
        print("{} is the First Occuring pair".format(i))
        break
dlen = len(my_dict);count=0
for i in my_dict:
    if my_dict[i]==1:
        count+=1
if count==dlen:
    print("Null")
print(my_dict)