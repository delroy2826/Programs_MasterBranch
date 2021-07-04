#Have the function LongestWord(sen) take the sen parameter being passed and return
#the largest word in the string. If there are two or more words that are the same length,
#return the first word from the string with that length.
#Ignore punctuation and assume sen will not be empty.
def LogestWord(sen):
    my_dict=dict()
    for i in sen.split():
        str1=""
        for j in i:
            if j.isalpha():
                str1+=j
        my_dict[len(str1)]=my_dict.get(len(str1),str1)
    a=max(my_dict)
    return my_dict[a]
sen="I dogstt lovee"
print(LogestWord(sen))
'''
l=sen.split()
my_dict=dict()
for i in l:
    str1=""
    for j in i:
        if j.isalpha():
            str1+=j
    my_dict[len(str1)]=my_dict.get(len(str1),str1)
a=max(my_dict)
print(my_dict[a])'''
