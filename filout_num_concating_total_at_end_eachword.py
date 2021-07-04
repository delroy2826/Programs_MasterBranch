str1 = input().lower()
split_str1 = str1.split()
for i in split_str1:
    str2=''
    count = 0
    for j in i:
        if j.isalpha():
            str2+=j
        else:
            count+=int(j)
    print(str2 + str(count),end=' ')
print()

str1 = "I12 L70ove 6y8ou"
str1_list = str1.split()
for i in str1_list:
    count=0
    for j in i:
        if j.isdigit():
            count+=int(j)
        else:
            print(j,end='')
    print(count,end=' ')
print()