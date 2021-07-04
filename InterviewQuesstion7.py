weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat']
list1 = [[x,weekdays.count(x)] for x in set(weekdays)]
print(list1)

weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','mon','tue','wed','thu','fri','sat','mon','mon']
my_dict = dict()
for i in weekdays:
    my_dict[i]=my_dict.get(i,0)+1
print(my_dict)