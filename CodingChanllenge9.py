#Create a program which will accept a string and checks whether string
#is in camelCase or snake_case And also create two Functions getCamelCase() and
# get_snake_case(). To convert snake_case into camelCase or Vice Versa
def snake_case(a):
    global str1
    for i in a:
        if i.isupper():
            #global str1
        #print(i)
            str1+="_"
            str1+=i.lower()
        else:
            str1+=i
def camelCase(a):
    global str1
    d = len(list(a))
    c=0
    while c<d:
        l1=list(a)
        if l1[c]=="_":
            str1+=l1[c+1].upper()
            c+=1
        else:
            str1+=l1[c]
        c+=1
#a="gvs_nikhil_reddy"
#a="gvsNikhilReddy"
print("Example: camelCase  and snake_case")
a=input("Enter the string: ")
str1 = ""
for i in a:
    if i=="_":
        camelCase(a)
        print("Entered String is\n[ {} ](snake_case) and Converted to : \n{} (camelCase)".format(a,str1))
        break
    elif i.isupper():
        snake_case(a)
        print("Entered String is\n[ {} ](camelCase) and Converted to : \n {} (snake_case)".format(a,str1))
        break

'''a="gvsNikhilReddy"
str1 = ""
#gvs_nikhil_reddy
for i in a:
    if i.isupper():
        #print(i)
        str1+="_"
        str1+=i.lower()
    else:
        str1+=i
print(str1) #Output for snake_case gvs_nikhil_reddy
str2="gvs_nikhil_reddy"
str3 = ""
a = len(list(str2))
c=0
while c<a:
    l1 = list(str2)
    if l1[c]=="_":
        str3+=l1[c+1].upper()
        c+=1
    else:
        str3+=l1[c]
    c+=1
print(str3)

def snake_case(a):
    global str1
    for i in a:
        if i.isupper():
            #global str1
        #print(i)
            str1+="_"
            str1+=i.lower()
        else:
            str1+=i
a="gvsNikhilReddy"
str1=""
snake_case(a)
print(str1)'''