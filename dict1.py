#Dictionary Sorted data according to category
my_info_dict = {'Jack':'Name','Oliveira':'Surname','Suresh':'Name','Gokul':'Name','Malon':'Name','Pai':'Surname'}

my_info = dict()
for values,cat in my_info_dict.items():
    my_info[cat]=my_info.get(cat,[])+[values]
print(my_info)

for i in my_info:
    list1 = my_info[i]
    count=1
    for j in list1:
        print("{}_{}:{}".format(i,count,j))
        count+=1