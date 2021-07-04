#word frequency
ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time""".split()
for i in list(set(ss)):
    print(i,"=",list(ss).count(i),end=' , ')

#dict.fromkeys(keys, value)
#Required. An iterable specifying the keys of the new dictionary - Keys
#Optional. The value for all keys. Default value is None - Values
ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""

words = ss.split()
d = dict.fromkeys(words,0)
for w in words:
    d[w] += 1
print(d)

from collections import Counter
ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time""".split()

cout = Counter(ss)
print(cout)

#3
ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time""".split()
my_dict=dict()
l1 = sorted(set(ss))
for i in l1:
    my_dict[i]=ss.count(i)
print(my_dict)