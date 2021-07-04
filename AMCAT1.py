#AMCAT QUESTON 1223 = 112233
n = str(9945992234)
new_str=''
for i in range(len(list(n))):
    if n.count(n[i])<2:
        new_str+=n[i]*2
    else:
        new_str+=n[i]
print(new_str)

#2
n = 9945992234
strn = str(n)
strn1 = ""
for i in strn:
    if strn.count(i)<2:
        strn1+=i*2
    else:
        strn1+=i
print(strn1)
