#Create A Program Which Accepts A string And Returns The String With All the
#Surrounding Duplicates Removed From It
#ForExample: Input: "NEEXXxTTGGEENNNCCOODDEER" OutPut: "NEXxTGENCODER"
str1="NEEXXxTTGGEENNNNCCOODDEERR"
len_str1 = len(str1);#print(len_str1)
str2=""
str3=""
c=0
while c<len_str1:
    if c==len(str1)-1:
        str2+=str1[c]
        break
    elif str1[c]==str1[c+1]:
        str2+=str1[c]
        #print(str2)
        c+=1
    else:
        str2+=str1[c]
        #print(str2)
    c+=1
#print("2",str2)
len_str2 = len(str2)
c=0
while c<len_str2:
    if c==len(str2)-1:
        str3+=str2[c]
        break
    elif str2[c]==str2[c+1]:
        str3+=str2[c]
        #print(str2)
        c+=1
    else:
        str3+=str2[c]
        #print(str2)
    c+=1
print(str3)

str2="NEEXXxTTGGEENNNCCOODDEER"
str1=str2+" "
l=[]
for i in range(len(str1)-1):
    if str1[i]!=str1[i+1]:
        print(str1[i],end='')